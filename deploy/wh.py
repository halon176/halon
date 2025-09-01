#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os
import logging
import hmac
import hashlib
import sys

SERVER_PORT = int(os.environ.get("BLOG_PORT", 9000))
BLOG_PUBLIC_DIR = os.environ.get("BLOG_PUBLIC_DIR")
GITHUB_BLOG_SECRET = os.environ.get("GITHUB_BLOG_SECRET")

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

if not BLOG_PUBLIC_DIR:
    logger.fatal("BLOG_PUBLIC_DIR environment variable is not set")
    sys.exit(1)

if not GITHUB_BLOG_SECRET:
    logger.fatal("GITHUB_SECRET environment variable is not set")
    sys.exit(1)

def run_cmd(cmd, cwd=None):
    logger.info("Running: %s", ' '.join(cmd))
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.stdout:
        logger.info(result.stdout.strip())
    if result.stderr:
        logger.error(result.stderr.strip())
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}")

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            payload = self.rfile.read(content_length)

            signature = self.headers.get("X-Hub-Signature-256")
            if not signature:
                logger.warning("Missing GitHub signature")
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Missing signature\n")
                return

            mac = hmac.new(GITHUB_BLOG_SECRET.encode(), msg=payload, digestmod=hashlib.sha256)
            expected = "sha256=" + mac.hexdigest()
            if not hmac.compare_digest(expected, signature):
                logger.warning("Invalid GitHub signature")
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Invalid signature\n")
                return

            logger.info("Valid webhook received, starting deploy")
            run_cmd(["git", "checkout", "main"], cwd=REPO_DIR)
            run_cmd(["git", "pull", "--rebase"], cwd=REPO_DIR)
            run_cmd(["hugo", "-d", BLOG_PUBLIC_DIR], cwd=REPO_DIR)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Deploy completed\n")
            logger.info("Deploy completed successfully")

        except Exception as e:
            logger.exception("Deploy failed")
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

if __name__ == "__main__":
    logger.info("Using BLOG_PUBLIC_DIR: %s", BLOG_PUBLIC_DIR)
    logger.info("Starting webhook server on port %d", SERVER_PORT)

    try:
        HTTPServer(("0.0.0.0", SERVER_PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down server")
    except Exception as e:
        logger.exception("Server error: %s", e)

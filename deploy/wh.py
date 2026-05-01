#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os
import logging
import hmac
import hashlib
import sys
import json

SERVER_PORT = int(os.environ.get("BLOG_PORT", 9000))
SERVER_HOST = os.environ.get("BLOG_HOST", "127.0.0.1")
BLOG_PUBLIC_DIR = os.environ.get("BLOG_PUBLIC_DIR")
GITHUB_BLOG_SECRET = os.environ.get("GITHUB_BLOG_SECRET")
DEPLOY_BRANCH = os.environ.get("BLOG_DEPLOY_BRANCH", "refs/heads/main")

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
    logger.fatal("GITHUB_BLOG_SECRET environment variable is not set")
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
            event = self.headers.get("X-GitHub-Event")
            if event != "push":
                logger.info("Ignoring non-push event: %s", event)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Ignored\n")
                return

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

            try:
                data = json.loads(payload)
                ref = data.get("ref", "")
            except json.JSONDecodeError:
                logger.warning("Invalid JSON payload")
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid JSON\n")
                return

            if ref != DEPLOY_BRANCH:
                logger.info("Ignoring push to %s (only %s is deployed)", ref, DEPLOY_BRANCH)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Branch not deployed\n")
                return

            logger.info("Valid push webhook on %s, starting deploy", ref)
            run_cmd(["git", "fetch", "origin", DEPLOY_BRANCH.split("/")[-1]], cwd=REPO_DIR)
            run_cmd(["git", "checkout", "--force", DEPLOY_BRANCH.split("/")[-1]], cwd=REPO_DIR)
            run_cmd(["git", "reset", "--hard", f"origin/{DEPLOY_BRANCH.split('/')[-1]}"], cwd=REPO_DIR)
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
    logger.info("Deploying branch: %s", DEPLOY_BRANCH)
    logger.info("Starting webhook server on %s:%d", SERVER_HOST, SERVER_PORT)

    try:
        HTTPServer((SERVER_HOST, SERVER_PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down server")
    except Exception as e:
        logger.exception("Server error: %s", e)

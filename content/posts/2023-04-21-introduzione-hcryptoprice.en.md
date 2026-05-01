+++
title = "I Created a Creature and Its Name Is HCryptoPrice"
date = 2023-04-21 12:56:12
images = ["/covers/telegram-bot-creation-cover.jpg"]
categories = ["tech"]
translationKey = "2023-04-21-hcryptoprice"
+++

I've given birth to a little creature — a Telegram bot capable of querying CoinGecko's API and returning data on price, market cap, ATH, ATL, and other acronyms in a message.

## Introduction

I've been hanging out in Telegram groups where people discuss cryptocurrencies for years, but it's more of a hobby than fanaticism. Each group had a different bot, and I often didn't like them at all — all with similar features but always some detail that didn't satisfy me. So, as soon as I had the ability to do so, I wrote my own bot.

The bot is open source and [you can find its complete code on GitHub under the MIT license](https://github.com/halon176/h-crypto-price-bot).

There's obviously also a running bot, [which you can reach here](https://t.me/h_crypto_price_bot).

## Features

The bot's main feature at the moment is fetching information about the current and historical price within a maximum 1-year window for the token requested via the `/p` command. Since the query is done by symbol, you easily run into tokens with conflicting symbols — for example, ACS stands for both Access Protocol and Acryptos. In that case, the bot generates a menu with buttons to select the desired token. Here's an example response to `/p btc`:

![](../img/bot-price-response.jpg#center)

Let's break down the response:

1) Overall ranking, name, and symbol of the token, where the name and symbol are links to the project's website and their Twitter account respectively (the good folks at CoinGecko sometimes insert referral links into project sites, which the bot removes with a dedicated function);

2) Historical change relative to the current price;

3) General asset data followed by all-time high and all-time low values with their respective time references.

This feature alone required days of work due to substantial API inconsistency and handling a myriad of exceptions, plus a complex system of mirrors and levers to keep the various columns aligned and make everything presentable.

For now, the other features are few — we have:

- `/dom` which returns the top 10 dominance with relative market percentages
- `/news` which returns the top picks news from CoinTelegraph

## Roadmap

The idea is to add more features, even ones not strictly tied to the API, since it's quite limiting. I'd like at least:

- a function like `/contract` that, by selecting the relevant chain, returns the contract address so it can be used in various wallets or swaps;
- better use of the news feature, like making language selection available (CoinTelegraph has several) or scheduling the news message at a particular time of day;
- calls to other public APIs, though I still need to investigate which ones.

## Feedback highly welcome

Obviously, everything is very experimental, and some tokens still cause problems — problems I try to handle case by case by creating exceptions in the data reading. So I ask those in the field to use it, maybe add it to some groups (it doesn't require admin permissions), and let me know about any issues or ideas that come to mind to improve it.

Cheers!

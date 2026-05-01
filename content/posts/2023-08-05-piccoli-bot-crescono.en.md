+++
title = "Little Bots Grow Up: HCryptoPrice Reaches Version v1.0.0!"
date = 2023-08-05 21:46:12
images = ["/covers/hcryptoprice-first-stable.webp"]
categories = ["tech"]
translationKey = "2023-08-05-hcryptoprice-v1"
+++

Quite some time has passed since our bot's activation, and all the basic features I had in mind during the design phase have been implemented. So, I think the time has come to proudly announce HCryptoPrice's first stable version!

## Features

In the [previous article](/posts/2023-04-21-introduzione-hcryptoprice/) I already described the bot's main features in detail, so I'll keep it short:

- Querying CoinMarketCap and CoinGecko APIs to get real-time prices and historical variations of a cryptocurrency, presented in a slick format.
- Generating charts for different timeframes for a specific cryptocurrency listed on CoinGecko.
- Receiving real-time information about ETH gas.
- Updates on the latest cryptocurrency-related news, sourced from CoinTelegraph.
- The ability to use a CoinMarketCap API key to access their APIs, with a dedicated command to view information about the API key being used (e.g., calls made, calls remaining, etc.).
- Handling of token symbol collisions: when multiple tokens share the same symbol (like ACS standing for both AccessProtocol and Acryptos), the bot will ask to specify the desired token through a menu.

## Some screenshots

![Bitcoin Chart](../img/grafico-bitcoin.webp#center)
Bitcoin price chart over a 1-day timeframe, accessible with the `/c btc` command.

![Multiple Token Selection](../img/selezione-multipla-token.webp#center)
Multiple token selection with the same symbol using the `/p acs` command (same goes for chart collisions).

## Future plans

The goal is to implement database support, allowing the saving of user preferences and managing statistics related to bot interactions. I'm considering using SQLite; however, currently, when the Docker image is regenerated, the database would be lost. Therefore, I'm evaluating the option of using an external database, most likely PostgreSQL.

This implementation would represent added value over standard usage. However, I intend to keep the bot functional even without requiring a database, although some features might be affected.

I'm not entirely convinced about this choice yet, as it limits the ability to add many interesting features. For example, currently it's not possible to store chart colors, which remain unchanged until the application is restarted.

## Conclusion

I'm extremely satisfied with the result. The bot has proven stable and performant — I've never encountered crash issues or the like. I decided to disable info logging due to an issue related to the httpx library, which, after an update, floods the log with Telegram API pooling calls, making the logs practically unusable. However, since this dependency is tied to python-telegram-bot, my options for intervention are limited. I trust this problem will be resolved in the future.

Other than that, the source code is available on [GitHub](https://github.com/halon176/h-crypto-price-bot), and the bot is accessible on Telegram by searching `@h_crypto_price_bot` or clicking [here](https://t.me/h_crypto_price_bot).

Peace and blessings! :heart:

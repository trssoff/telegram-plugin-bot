
<h1 align="center">
  <br>
    <a href="https://github.com/trssoff/telegram-plugin-bot"><img src="https://github.com/trssoff/telegram-plugin-bot/raw/master/.github/logo.png" alt="Telegran Plugin Bot"></a>
  <br>
  Telegram bot with a plugin based architecture
  <br>
</h1>

<h4 align="center">A minimal Telegram bot with a plugin based architecture.</h4>

<p align="center">
  <a href="https://badge.fury.io/for/py/python-telegram-bot">
    <img src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/telegram_plugin_bot/"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/trssoff">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://money.yandex.ru/to/410014872690987">
    <img src="https://img.shields.io/badge/RUB-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#fonfiguration">Configuration</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#contacts">Contacts</a> •
  <a href="#license">License</a>
</p>


<h1 align="center">
  <br>
    <a href="https://github.com/trssoff/telegram-plugin-bot"><img src="https://github.com/trssoff/telegram-plugin-bot/raw/master/.github/intro.gif" alt="Telegran Plugin Bot"></a>
  <br>
  How it works
  <br>
</h1>

## Features

* Plugin based architecture
  - Supports easily adding new features.
  - Reduces the size of an application.
  
* Hot plugging
  - You can enable or disable some features if you want.
  - For adding new features stopping bot is not required.
  
* Logging  

* Easy to deploy
  - Minimum requirements.
* Cross platform
  - Windows, macOS and Linux ready.

## How To Use

To clone and run this application, you need [Git](https://git-scm.com) and [Python 3.7](https://www.python.org/downloads/) (with [pip](https://pip.pypa.io/en/stable/installing/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git https://github.com/trssoff/telegram-plugin-bot

# Go into the repository
$ cd telegram-plugin-bot

# Install dependencies
$ pip3 install -r requirements.txt

# Run the app
$ ./bot.py
```

Note: If you're using different python location use full path for `python` from the command prompt.


## Configuration

You need to create config.yaml in project directory, or run `./bot.py` and then fill out template config.yaml.

```bash
TELEGRAM_API_TOKEN: TELEGRAM_BOT_TOKEN
admin_list:
- 'TELEGRAM_ADMIN_ID'
plugin_list:
- hello
plugin_settings:
  hello:
    test_key: plugin works fine here!
    times_waved: 0
```
Note: If you've created additional plugins, you need to list it in config.yaml.

## Download

You can [download](https://github.com/trssoff/telegram-plugin-bot/archive/master.zip) the latest stable version of Telegram plugin bot for Windows, macOS and Linux.

## Emailware

Telegram plugin bot is an [emailware](https://en.wiktionary.org/wiki/emailware). if you liked using this app or it has helped you in anyway, I'd like you to send me an email on <tarassov.michael@gmail.com> about anything you want to say about this project. I'd really appreciate it!

## Credits

This software uses the following open source packages:

- [Python](https://www.python.org)
- [PyYAML](https://pyyaml.org/)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## Support

<a href="https://money.yandex.ru/to/410014872690987" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


## Contacts

- [Twitter](https://twitter.com/mike_trssoff) 
- [Linkedin](https://www.linkedin.com/in/tarassov-michael/)
- [Instagram](https://www.instagram.com/michael.tarassov/)

## License

MIT

---
<div align="center">
  <sub>The little telegram bot framework that could. Built with ❤︎ by
  <a href="https://github.com/trssoff/">Michael Tarassov</a> and many people who inspire me.
  </sub>
  </a>
</div>

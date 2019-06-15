class Cryptocurrency:
    def __init__(self):
        self.config = []
        self.commands = {
            'crypto': self.cryptocurrency
        }
        self.default_config = {
            'test_key': "plugin works fine here!",
            'times_waved': 0
        }
        self.description = "I'm a Cryptocurrency plugin."
        self.help_text = "Write /crypto pair to receive current price!"

    def __cryptonator__(self, crypto_list=None):
        if crypto_list is None:
            crypto_list = ['btc-usd', 'eth-usd', 'xrp-usd']
        import json
        import requests

        result = ''
        for pair in crypto_list:
            data = json.loads(requests.get('https://api.cryptonator.com/api/ticker/{pair}'.format(pair=pair)).text)
            template = '*Current {base} price:* {price} *{target}*\r\n*Change* {change} *{target}*\r\n\r\n'
            if data['success']:
                msg = template.format(base=data['ticker']['base'],
                                      price=float(data['ticker']['price']),
                                      target=data['ticker']['target'],
                                      change=float(data['ticker']['change']))
            else:
                msg = 'Unknown {pair} currency pair\r\n'.format(pair=pair)
            result += msg
        return result

    def cryptocurrency(self, bot, update, args):
        import telegram

        if args:
            result = self.__cryptonator__(args)
        else:
            result = self.__cryptonator__()
        update.message.reply_text(text=result, parse_mode=telegram.ParseMode.MARKDOWN)
        self.config['times_waved'] += 1

    def on_text(self, bot, update):
        if 'crypto' in update.message.text:
            import telegram

            result = self.__cryptonator__()
            update.message.reply_text(text=result, parse_mode=telegram.ParseMode.MARKDOWN)
            self.config['times_waved'] += 1
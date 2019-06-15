class hello():
    def __init__(self):
        self.config = []
        self.commands = {
            'hello': self.hello
        }
        self.default_config = {
            'test_key': "plugin works fine here!",
            'times_waved': 0
        }
        self.description = "I'm a test plugin."
        self.help_text = "Write /hello to receive a very special greeting from me!"

    def hello(self, bot, update, args):
        update.message.reply_text(f'Hi {update.message.from_user.username}!')
        self.config['times_waved'] += 1

    def on_text(self, bot, update):
        if 'hello' in update.message.text:
            update.message.reply_text(f"Hi! Echo: {update.message.text}")
            self.config['times_waved'] += 1

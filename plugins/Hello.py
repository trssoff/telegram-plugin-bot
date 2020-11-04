class Hello:
    def __init__(self):
        self.config = []
        self.commands = {
            'hello': self.hello
        }
        self.default_config = {
            'test_key': "plugin works fine here!",
            'times_waved': 0
        }
        self.description = "I'm a hello plugin."
        self.help_text = "Write /hello to receive a health information about me!"

    def hello(self, update, context):
        update.message.reply_text(f'Hi {update.message.from_user.username}! I\'m alive!')
        self.config['times_waved'] += 1

    def on_text(self, update, context):
        if 'hello' in update.message.text:
            update.message.reply_text(f"Hi! Echo: {update.message.text}")
            self.config['times_waved'] += 1

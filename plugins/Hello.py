class Health:
    def __init__(self):
        self.config = []
        self.commands = {
            'health': self.health
        }
        self.default_config = {
            'test_key': "plugin works fine here!",
            'times_waved': 0
        }
        self.description = "I'm a health plugin."
        self.help_text = "Write /health to receive a health information about me!"

    def health(self, update, context):
        update.message.reply_text(f'Hi {update.message.from_user.username}! I\'m alive!')
        self.config['times_waved'] += 1

    def on_text(self, update, context):
        if 'health' in update.message.text:
            update.message.reply_text(f"Hi! Echo: {update.message.text}")
            self.config['times_waved'] += 1

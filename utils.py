import threading, yaml, logging

def pprint(s):
    logging.info(f"{'='*len(s)}\n{s}\n{'='*len(s)}")


def generate_config_file():
    sample_settings = {
        "TELEGRAM_API_TOKEN": "",
        "plugin_list": [ "hello" ],
        "admin_list": [],
        "plugin_settings": {}
    }
    with open('config.yaml', 'w') as file:
        yaml.dump(sample_settings, file)


def set_interval(interval, times = -1):
    def outer_wrap(function):
        def wrap(*args, **kwargs):
            stop = threading.Event()
            def inner_wrap():
                i = 0
                while i != times and not stop.isSet():
                    stop.wait(interval)
                    function(*args, **kwargs)
                    i += 1
            t = threading.Timer(0, inner_wrap)
            t.daemon = True
            t.start()
            return stop
        return wrap
    return outer_wrap


def get_admin_ids(bot, chat_id):
    """Returns a list of admin IDs for a given chat. Results are cached for 1 hour."""
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]


def is_bot_admin(bot, chat_id, admin_list):
    return update.message.from_user.id in get_admin_ids(bot, update.message.chat_id)+self.admin_list


def is_chat_admin(bot, chat_id):
    return is_admin(bot, chat_id, None)

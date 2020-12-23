from configparser import ConfigParser


class Config(object):
    def __init__(self):
        super(Config, self).__init__()
        self.config = ConfigParser()
        self.config.read('config.ini')

    def get_api_key(self):
        return self.config['bot']['key']

    def get_results_limit(self):
        return int(self.config['search']['results_limit'])

config = Config()

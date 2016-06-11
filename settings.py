import configparser
import base64

# modified from https://github.com/SexualRhinoceros/MusicBot/blob/develop/musicbot/config.py

class Settings(object):
    def __init__(self,settings):
        config = configparser.ConfigParser()
        config.read(settings)

        self.email = config.get('Credentials', 'Email', fallback=None)
        self.password = config.get('Credentials', 'Password', fallback=None)

        self.owner_id = config.get('Permissions', 'OwnerID', fallback=None)

        if not self.owner_id:
            raise ValueError("An owner is not specified in the configuration file")
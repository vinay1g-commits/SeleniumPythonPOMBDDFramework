from configparser import ConfigParser


def reading_data_ini(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)

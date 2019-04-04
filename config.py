import configparser
import pathlib

config = configparser.ConfigParser()
config.read('config.ini')
datadir = pathlib.Path(config['paths']['datadir']).expanduser()
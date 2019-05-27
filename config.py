import configparser
import pathlib

config = configparser.ConfigParser()
config.read('config.ini')
input_datadir = pathlib.Path(config['paths']['input_datadir']).expanduser()
result_datadir = pathlib.Path(config['paths']['result_datadir']).expanduser()
IMAGES_datadir = pathlib.Path(config['paths']['IMAGES_datadir']).expanduser()

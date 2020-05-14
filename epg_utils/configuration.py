import mysql.connector
import ConfigParser
import yaml
from subprocess      import PIPE
from subprocess      import Popen
from subprocess      import STDOUT


def configuration():

    with open("main.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile , Loader=yaml.FullLoader)
    return cfg

def load_cache():
    with open("cache.yaml", 'r') as ymlfile:
        cache = yaml.load(ymlfile , Loader=yaml.FullLoader)
    return cache
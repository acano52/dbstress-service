import mysql.connector
import ConfigParser
import yaml
from subprocess      import PIPE
from subprocess      import Popen
from subprocess      import STDOUT

from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app


def configuration():

    with open("main.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile , Loader=yaml.FullLoader)
    return cfg
    
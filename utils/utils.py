import mysql.connector
import ConfigParser
import yaml
from subprocess      import PIPE
from subprocess      import Popen
from subprocess      import STDOUT
from mysql.connector import Error



def configuration():

    with open("main.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile , Loader=yaml.FullLoader)
    return cfg

def getConnection(dburi):


    conn = None
    return conn
# system packages
import os
import sys

# logs
import logging
from logging.handlers import RotatingFileHandler

# pip packages
from flask import Flask
from flask_restful import Api
from flask_mysqlpool import MySQLPool

# cache
# https://flask-caching.readthedocs.io/en/latest/
# http://brunorocha.org/python/flask/using-flask-cache.html
# Example
#from flask import current_app
#def some_function():
#    cached = current_app.cache.get('a_key')
#    if cached:
#        return cached
#    result = do_some_stuff()
#    current_app.cache.set('a_key', result, timeout=300)
#    return result
from flask_caching import Cache
from flask import current_app as app


# localpackages
from epg_utils.configuration import *
from epg_api.transactions    import transactions





pathname = os.path.abspath(os.path.dirname(sys.argv[0]))
ACTIVATE_SCRIPT = pathname + '/venv/bin/activate_this.py'
execfile(ACTIVATE_SCRIPT, dict(__file__=ACTIVATE_SCRIPT))

# Read configuration
cfg = configuration()

# config flask aplication
app = Flask(__name__)

# init cache
app.config['CACHE_TYPE'] = 'filesystem'
app.config['CACHE_DIR'] = '/tmp/cache'
#app.config['CACHE_DEFAULT_TIMEOUT'] = 922337203685477580
app.config['CACHE_DEFAULT_TIMEOUT'] = 5
#app.config['CACHE_THRESHOLD'] = 922337203685477580

# db
dbcfg = cfg.get('database')
app.config['MYSQL_HOST']       = dbcfg.get('MYSQL_HOST')
app.config['MYSQL_PORT']       = dbcfg.get('MYSQL_PORT')
app.config['MYSQL_USER']       = dbcfg.get('MYSQL_USER')
app.config['MYSQL_PASS']       = dbcfg.get('MYSQL_PASS')
app.config['MYSQL_DB']         = dbcfg.get('MYSQL_DB')
app.config['MYSQL_POOL_NAME']  = 'dbstress_pool'
app.config['MYSQL_POOL_SIZE']  = dbcfg.get('MYSQL_POOL_SIZE')
app.config['MYSQL_AUTOCOMMIT'] = True

# log
logcfg = cfg.get('logging')
LOG_FILENAME=logcfg.get('LOGFILE')
LEVEL=logcfg.get('LEVEL').upper()
logging.basicConfig(level=eval('logging.' + LEVEL))
formatter = logging.Formatter('[%(asctime)s] - [%(thread)d - %(threadName)s] - [%(levelname)s] - %(message)s')
handler = RotatingFileHandler(LOG_FILENAME, maxBytes=10000000, backupCount=5)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
# examples
# app.logger.info('msg') 
# app.logger.debug('msg') 
# app.logger.error('msg') 
# app.logger.warning('msg') 
# app.logger.critical('msg') 


# init
db       =   MySQLPool(app)
api      =   Api(app)
appcache =   Cache(app)


#with app.app_context():
     #cache_merchants    = load_cache_merchants()
     #cache_transactions = load_cache()
     
     #appcache.set('cache_transactions', load_cache())
     #appcache.set('cache_merchants', load_cache_merchants())


if __name__ == "__main__":
   
   print("http://192.168.52.52:3333/dbstress/api/v1.0/transactions")
   api.add_resource(transactions, '/dbstress/api/v1.0/transactions', endpoint = 'dbstress')
   app.run(host='192.168.52.52', port='3333')   
   

   
   
   

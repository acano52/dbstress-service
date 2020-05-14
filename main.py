# system packages
import os
import sys

# pip packages
from flask import Flask
from flask_restful import Api
from flask_mysqlpool import MySQLPool

# localpackages
from epg_utils.configuration import configuration
from epg_api.transactions    import transactions


app = Flask(__name__)

dbcfg = configuration().get('database')
app.config['MYSQL_HOST']       = dbcfg.get('MYSQL_HOST')
app.config['MYSQL_PORT']       = dbcfg.get('MYSQL_PORT')
app.config['MYSQL_USER']       = dbcfg.get('MYSQL_USER')
app.config['MYSQL_PASS']       = dbcfg.get('MYSQL_PASS')
app.config['MYSQL_DB']         = dbcfg.get('MYSQL_DB')
app.config['MYSQL_POOL_NAME']  = 'dbstress_pool'
app.config['MYSQL_POOL_SIZE']  = dbcfg.get('MYSQL_POOL_SIZE')
app.config['MYSQL_AUTOCOMMIT'] = True

db  = MySQLPool(app)
api = Api(app)

pathname = os.path.abspath(os.path.dirname(sys.argv[0]))
ACTIVATE_SCRIPT = pathname + '/venv/bin/activate_this.py'
execfile(ACTIVATE_SCRIPT, dict(__file__=ACTIVATE_SCRIPT))


if __name__ == "__main__":
   print("http://192.168.52.52:3333/dbstress/api/v1.0/transactions")
   api.add_resource(transactions, '/dbstress/api/v1.0/transactions', endpoint = 'dbstress')
   app.run(host='192.168.52.52', port='3333')   

   
   
   

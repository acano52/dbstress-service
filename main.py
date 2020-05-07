#from __future__ import print_function
import os
import sys
from flask import Flask,abort,jsonify
from flask_restful import Api
from resources.transactions import transactions
#import mysql.connector
#from mysql.connector import Error
#from mysql.connector import pooling
#from flask import g
#from mysql_connection import *

import mysql.connector
from flask_mysqlpool import MySQLPool





app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db01a'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'acano'
app.config['MYSQL_PASS'] = 'Ant23011'
app.config['MYSQL_DB'] = 'easypaym_epg'
app.config['MYSQL_POOL_NAME'] = 'mysql_pool'
app.config['MYSQL_POOL_SIZE'] = 32
app.config['MYSQL_AUTOCOMMIT'] = True

db = MySQLPool(app)
api = Api(app)


@app.route('/')
def index():
    try:
        conn = db.connection.get_connection()  # get connection from pool
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select count(*) from mysql.user")
        result = cursor.fetchall()
        conn.close()  # return connection to pool
    except mysql.connector.ProgrammingError as err:
        print(err)
        abort(500)
    to_json = [dict(row) for row in result]
    return jsonify(to_json)


pathname = os.path.abspath(os.path.dirname(sys.argv[0]))
ACTIVATE_SCRIPT = pathname + '/venv/bin/activate_this.py'
execfile(ACTIVATE_SCRIPT, dict(__file__=ACTIVATE_SCRIPT))


if __name__ == "__main__":

   api.add_resource(transactions, '/dbstress/api/v1.0/transactions', endpoint = 'transactions')
   app.run(host='192.168.52.52', port='3333')   
   
   
   

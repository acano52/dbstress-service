from flask import Flask,abort,jsonify
from flask_restful import Api, Resource, reqparse
import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.configuration import *
from epg_utils.cache import *
from epg_db.t_transactions import *


class transactions(Resource):

       
           def get(self):
               #db = MySQLPool(app)
               # appcache=Cache(app)
               # cache_transactions =  appcache.get('cache_transactions')
               # app.logger.info(cache_transactions)
               # app.logger.debug( appcache.get('cache_merchants'))
               # try:
               #    conn = db.connection.get_connection()  # get connection from pool
               #    cursor = conn.cursor(dictionary=True)
               #    cursor.execute("select * from acano")
               #   
               #    result = cursor.fetchall()
               #    conn.close()  # return connection to pool
               # except mysql.connector.Error as err:
               #    print(format(err))
               #    conn.close()
               #    abort(500) abort(500)
               
               with app.app_context():
                    cache_general    = get_cache_general()
                    cache_merchants  = get_cache_merchants()
                    txid=insert_t_transaction()
               to_json = [cache_merchants]
               return jsonify(to_json) 

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
               with app.app_context():
                    cache_general    = get_cache_general()
                    cache_merchants  = get_cache_merchants()
                    txid=insert_t_transaction()
               to_json = [cache_merchants]
               return jsonify(to_json) 

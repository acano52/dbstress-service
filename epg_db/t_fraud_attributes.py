import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from flask import Flask,abort,jsonify
from epg_utils.cache import *
import random
import json

def insert_t_fraud_atributes(transaction_id):



       txid = None
       s_json = { "cardBinCountry":"RU","cardBinCountryEqCountry":True,"ip":"94.25.172.140","countryIso2":"RU","type":"ECOM","cardBinCountryEqIpCountry":True }
       v_json = s_json
 

       sql= " INSERT INTO t_fraud_attributes ( "\
            " txn_id,                          "\
            " attributes                       "\
            " ) VALUES ( %s , %s )             "
            
       data=(transaction_id,json.dumps(v_json))
       db = MySQLPool(app)
       try:
         conn = db.connection.get_connection()
         cursor = conn.cursor()
         cursor.execute(sql, data)  
         conn.commit
       except mysql.connector.Error as err:
         app.logger.error(format(sql))
         app.logger.error(data)
         raise err 
       finally:
         cursor.close()
         conn.close()


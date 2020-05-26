import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random


def insert_t_optional_parameters(merchant_id , transaction_id):
        
       txid = None
       sql=    "INSERT INTO t_optional_params ( "\
               "     `transaction_id`,"\
               "     `merchant_id`,"\
               "      `1`,"\
               "      `11`,"\
               "      `6`"\
               ") VALUES (%s,%s,%s,%s,%s)"

       data=(transaction_id,
             merchant_id,
             random.choice(["true","false"]),
             "STR_0001",
             "STR_00000000000000000000000000000002"
             )
       db = MySQLPool(app)
       try:
         conn = db.connection.get_connection()
         cursor = conn.cursor()
         cursor.execute(sql, data)  
         txid=cursor.lastrowid
         conn.commit
       except mysql.connector.Error as err:
         app.logger.error(format(sql))
         app.logger.error(data)
         raise err 
       finally:
         cursor.close()
         conn.close()



            
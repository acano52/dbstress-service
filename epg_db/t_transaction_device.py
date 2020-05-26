import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random


def select_t_transaction_device(transaction_id):
        
       
       db = MySQLPool(app)
       try:
          conn = db.connection.get_connection()
          cursor = conn.cursor(dictionary=True)

          sql="select transactio0_.transaction_id as transact1_2_0_, transactio0_.device_type as device_t2_2_0_ from t_transaction_device transactio0_ where transactio0_.transaction_id=%s"
              
          data=(transaction_id,)                
          cursor.execute(sql,data)  
          result = cursor.fetchall()
          c =  [dict(row) for row in result]
          return c
       except mysql.connector.Error as err:
          app.logger.error(format(err))
          app.logger.debug(cursor.statement)
       finally:
          cursor.close()
          conn.close()


def insert_t_transaction_device(transaction_id):

       txid = None
       sql="insert into t_transaction_device (device_type, transaction_id) values (%s, %s)"

       data=(random.choice(["DESKTOP","MOBILE"]),transaction_id,)
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


            
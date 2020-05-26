import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random

def select_t_optional_transactions_params(transaction_id):
               
       db = MySQLPool(app)
       try:
          conn = db.connection.get_connection()
          cursor = conn.cursor(dictionary=True)

          sql="SELECT key_value, value FROM t_optional_transactions_params WHERE transaction_id = %s"
              
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


def insert_t_optional_transactions_params(transaction_id):
        
       txid = None
       sql=    "INSERT INTO t_optional_transactions_params (transaction_id, value, key_value) VALUES (%s, %s, %s)"
       
       db = MySQLPool(app)
       try:
         conn = db.connection.get_connection()
         cursor = conn.cursor()
         data=(transaction_id,"value111111111111111111111111111111111111111111111111111111111111111111","key1")
         cursor.execute(sql, data)  
         data=(transaction_id,"value222222222222222222222222222222222222222222222222222222222222222222","key2")
         cursor.execute(sql, data)  
         data=(transaction_id,"value3","key3")
         cursor.execute(sql, data)  
         data=(transaction_id,"value444444444444444444444","key4")
         cursor.execute(sql, data)  
         data=(transaction_id,"value55555555555","key5")
         cursor.execute(sql, data)  
         data=(transaction_id,"value666666666666666666666666666666666666666666666","key6")
         cursor.execute(sql, data)  
         data=(transaction_id,"value7777777777","key7")
         cursor.execute(sql, data)  
         data=(transaction_id,"value8888888888888888888888888888888888888888888888888888888888888888888","key8")
         cursor.execute(sql, data)  
         data=(transaction_id,"value9999999999999999999999999999999999999999999999999999999999999999999999999","key9")
         cursor.execute(sql, data)  
         data=(transaction_id,"value1000000","key10")
         cursor.execute(sql, data)  
         conn.commit
       except mysql.connector.Error as err:
         app.logger.error(format(sql))
         app.logger.error(data)
         raise err 
       finally:
         cursor.close()
         conn.close()







	


            
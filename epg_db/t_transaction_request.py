import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random
import uuid


def insert_t_transaction_request(transaction_id):

       txid = None
       sql="INSERT INTO t_transaction_request(id, transaction_id,request, date_created) VALUES (%s,%s,%s,NOW())"
       
       v_request=get_random_15kblob()
       v_request.encode('utf-8')
       v_id     = str(uuid.uuid4())      
       v_id     = v_id.replace("-","") 
    
       data=(v_id,transaction_id,v_request)
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


            
import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random
import uuid


def insert_e_merchant_call(txnid):


      appcache=Cache(app)
      dic_txn = appcache.get(str(txnid))
      
      
      sql="INSERT  INTO e_merchant_call (date_created,date_modified,txn_id,merchant_id,url,received,message,object,launcher,reason)"\
          "VALUES (NOW(),NOW(),%s,%s,%s,%s,%s,%s,%s,%s)"
       
      v_url="https://secure-pay.fxclub.org/ext//ps_epg"
      v_message=get_random_4kblob()
      v_object=v_message.encode('utf-8')
      
      data=(dic_txn['id'],
        dic_txn['merchant_id'],
        v_url,
        True,
        v_message,
        v_object,
        True,
        None
       )
      
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

import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random


def insert_t_cart_transactions(transaction_id):

       txid = None
       sql="INSERT INTO `t_cart_transactions`(`date_created`, `gift`, `transaction_id`, `cus_invoice_address_id`, `cus_delivery_method_id`)VALUES (NOW(), %s, %s, %s,%s)"
       data=(False,transaction_id,None,None)
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


            
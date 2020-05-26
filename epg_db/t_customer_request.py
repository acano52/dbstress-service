import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random


def insert_t_customer_request(transaction_id):

       txid = None
       sql="INSERT INTO `t_customer_request`(`date_created`, `transaction_id`, `user_agent`, `timeout`, `rating`) VALUES (NOW(), %s, %s,%s,%s)"
        
       txt=random.choice(["Apache-HttpClient/4.5.8 (Java/11.0.4)",
                          "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G920I Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87 Mobile Safari/537.36",
                          "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1" ])

       data=(transaction_id,txt,None,None,)
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


            
import mysql.connector
import ConfigParser
import yaml
from subprocess      import PIPE
from subprocess      import Popen
from subprocess      import STDOUT

from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app


def get_cache_general():
    appcache=Cache(app)
    c = appcache.get('cache_general')
    if c is None:
       app.logger.info("Loading cache_general ...") 
       with open("cache.yaml", 'r') as ymlfile:
            c = yaml.load(ymlfile , Loader=yaml.FullLoader)
            appcache.set('cache_general',c) 
    return c

def get_cache_merchants():
    
    appcache=Cache(app)
    c = appcache.get('cache_merchants')
    if c is None:
       db = MySQLPool(app)
       app.logger.info("Loading cache_merchants ...")
       try:
          conn = db.connection.get_connection()  # get connection from pool
          cursor = conn.cursor(dictionary=True)
          sql = "select * from e_merchants limit 20"
          app.logger.debug(sql)
          cursor.execute(sql)
          result = cursor.fetchall()
          conn.close()  
          c =  [dict(row) for row in result]
          appcache.set('cache_merchants',c)      
       except mysql.connector.Error as err:
          app.logger.error(format(err))
          conn.close()
    return c
    
    
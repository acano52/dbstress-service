import os
import sys
from mysql.connector import pooling
from flask import g
import mysql.connector
from flask import current_app as app

def createMYSQLConnectionPool():
      mySQLPool = mysql.connector.pooling.MySQLConnectionPool(pool_name="dbpool",
                                                                pool_size=32,
                                                                pool_reset_session=True,
                                                                host='db01a',
                                                                database='easypaym_epg',
                                                                user='acano',
                                                                password='Ant23011')
      print("-I- Created MYSQL database pool...")
      print ("Printing connection pool properties: ")
      print("Connection Pool Name - ", mySQLPool.pool_name)
      print("Connection Pool Size - ", mySQLPool.pool_size)
      return mySQLPool
   
#def getSQLConnection():
#          conn = mySQLPool.get_connection()
#          if conn.is_connected():
#             print("-I- Connected to MySQL Database...")
#          return conn   


#def closeSQLConnection(app):
# with app.app_context():    
#   if(g.conn.is_connected()):
#      g.conn.close()
#      print("-I- MySQL connection is closed...")
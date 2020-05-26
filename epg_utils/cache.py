import mysql.connector
from mysql.connector.errors import Error
import ConfigParser
import yaml
from subprocess      import PIPE
from subprocess      import Popen
from subprocess      import STDOUT

from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
import random
import uuid
from datetime import datetime


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
    cache_merchants = appcache.get('cache_merchants')
    if cache_merchants is None:
       db = MySQLPool(app)
       app.logger.info("Loading cache_merchants ...")
       try:
          conn = db.connection.get_connection()  # get connection from pool
          cursor = conn.cursor(dictionary=True)
          sql = "SELECT a.* "\
                " FROM  e_merchants a"\
                " WHERE  EXISTS (SELECT * "\
                "                 FROM e_customer b "\
                "                WHERE b.active=true AND"\
                "                      b.merchant_id = a.id  )"\
                " LIMIT 5"
#Production "                      b.merchant_id = a.id and merchant_customer_id=532779 )"\
          cursor.execute(sql)
          cache_merchants=dict()
          for row in cursor:
              merchant_id=row["id"]

              # merchant info
              d=dict(row)

              #get e_customer
              l_customers=get_e_customer(merchant_id)
              d['e_customer']=l_customers
              
              #get paysol for merchant
              l_paysol=get_e_merchant_payment_mapping(merchant_id)
              d['e_merchant_payment_mapping']=l_paysol
               
              #get e_products for merchant
              l_products=get_e_products(merchant_id)
              d['e_products']=l_products

              #add merchant to merchantCache 
              cache_merchants[merchant_id]=d    

              app.logger.debug("Merchant_ID: %s .... CACHED with %s e_customer, %s paysol %s products" , merchant_id,len(l_customers),len(l_paysol),len(l_products))
              appcache.set('cache_merchants',cache_merchants)          

       except Error as e:
              app.logger.error(format(e))
       finally:
              cursor.close()
              conn.close()
          
    return cache_merchants
    

def get_e_customer(merchant_id):
       
       db = MySQLPool(app)
       try:
          conn = db.connection.get_connection()  # get connection from pool
          cursor = conn.cursor(dictionary=True)
          sql = " SELECT * "\
                " FROM e_customer "\
                " WHERE merchant_id = %s "\
                " LIMIT 3"   
#production " WHERE merchant_id = %s and MERCHANT_CUSTOMER_ID=532779"\     
#desa       " WHERE merchant_id = %s and MERCHANT_CUSTOMER_ID=5538217"\   
              
          data=(merchant_id,)                
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

def get_e_merchant_payment_mapping(merchant_id):
       
       db = MySQLPool(app)
       try:
          conn = db.connection.get_connection()  # get connection from pool
          cursor = conn.cursor(dictionary=True)
          sql = " SELECT * "\
                " FROM e_merchant_payment_mapping "\
                " WHERE merchant_id = %s "
              
          data=(merchant_id,)                
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

def get_e_products(merchant_id):
       
       db = MySQLPool(app)
       try:
          conn = db.connection.get_connection()  # get connection from pool
          cursor = conn.cursor(dictionary=True)
          sql = " SELECT * "\
                " FROM e_products "\
                " WHERE merchant_id = %s "\
                " LIMIT 100"   
              
          data=(merchant_id,)                
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

  
def get_cache_currency_country():

     currency_country = [["EUR","GB"],
                         ["CNY","CN"],
                         ["EUR","AT"],
                         ["USD","CL"],
                         ["USD","US"],
                         ["USD","CO"],
                         ["USD","KZ"],
                         ["USD","MX"],
                         ["RUB","RU"],
                         ["EUR","IT"],
                         ["CAD","CA"],
                         ["USD","UA"],
                         ["EUR","DE"],
                         ["EUR","FR"],
                         ["USD","RU"],
                         ["GBP","GB"],
                         ["EUR","ES"]]
                        
     return currency_country

def get_random_currency_country():

     c=get_cache_currency_country()
     k=random.choice(c)
     return k


def get_random_date():

    d=datetime.today().strftime('%Y%m%d')
    return d

def get_random_time():

    d=datetime.today().strftime('%H%M%S')
    dd="1" + d
    return dd

def get_random_stringlen(string_length=10):
    random = str(uuid.uuid4())      # Convert UUID format to a Python string.
    random = random.upper()         # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length]  # Return the random string.
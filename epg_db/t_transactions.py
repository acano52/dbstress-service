import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random


def insert_t_transaction():
        
       txid = None
       sql=   "INSERT into t_transactions " \
              "(id,"                        \
              "date_created,"              \
              "date_modified,"\
              "paysol_id,"\
              "amount," \
              "status_id," \
              "operation_id," \
              "merchant_id," \
              "invoice_id,"\
              "currency,"\
              "country,"\
              "product_id,"\
              "message,"\
              "original_txn_id,"\
              "merchant_txn_id, "\
              "customer_id,"\
              "e_customer_id,"\
              "dim_date_created_id,"\
              "dim_date_modified_id,"\
              "dim_time_created_id,"\
              "dim_time_modified_id,"\
              "workflow_step_id,"\
              "workflow_id,"\
              "workflow_version,"\
              "workflow_name,"\
              "workflow_description,"\
              "ip,"\
              "type,"\
              "description,"\
              "dim_ip_country_id,"\
              "dim_ip_city_id,"\
              "status_url,"\
              "kyc_status,"\
              "kyc_message,"\
              "dim_merchant_date_created_id,"\
              "dim_merchant_date_modified_id,"\
              "dim_merchant_time_created_id,"\
              "dim_merchant_time_modified_id,"\
              "account_details_id) "\
              "VALUES (%s, NOW(), NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s )"


       #get random merchant_id
       cache_merchants  = get_cache_merchants()
       k = random.choice(list(cache_merchants))
       m =cache_merchants[k]
       v_merchant_id  = m.get('id')
       v_status_url   = m.get('default_status_url')
       
       #get random e_customer_id from the selected merchant_id
       l_e_customer   = m.get('e_customer') 
       k=random.choice(l_e_customer)
       v_e_customer_id=k.get('id')
       v_customer_id=k.get('payfrex_customer_id')
       v_ip=k.get('ip')

       # random currency&country
       currency_country=get_random_currency_country()
       
       #get random paysol
       l_paysol  = m.get('e_merchant_payment_mapping') 
       k=random.choice(l_paysol)
       v_paysol_id=k.get('paysol_id')

       #get random product_id
       l_products = m.get('e_products') 
       k=random.choice(l_products)
       v_product_id=k.get('id')
   
       app.logger.debug("ramdom() merchant_id  : %s " , v_merchant_id)
       app.logger.debug("ramdom() e_customer_id: %s " , v_e_customer_id)
       app.logger.debug("ramdom() paysol_id: %s "     , v_paysol_id)
       

       id = None
       paysol_id=v_paysol_id
       amount=random.choice([20,100,50,47.30,1000,1346,848,11000,120,130,140,245,400,650,44.7,55.66,135,560,710,1100,2100,3200])
       status_id=random.choice([2,3,5])
       operation_id=random.choice([2,3])
       merchant_id=v_merchant_id
       invoice_id = None
       currency=currency_country[0]
       country=currency_country[1]
       product_id=v_product_id
       message="Transaction was initiated"
       original_txn_id = None
       merchant_txn_id=get_random_stringlen(random.choice([5,10,15,20])) #ramdom string with random len
       customer_id=v_customer_id
       e_customer_id=v_e_customer_id
       dim_date_created_id=get_random_date()
       dim_date_modified_id=get_random_date()
       dim_time_created_id=get_random_time()
       dim_time_modified_id=get_random_time()
       workflow_step_id = None
       workflow_id = None
       workflow_version = None
       workflow_name = None
       workflow_description = None
       ip=v_ip
       type="ECOM"
       description="Transfer to XXXXXXXXXXXX, id YYYYYYYYYY"
       dim_ip_country_id = None
       dim_ip_city_id = None
       status_url=v_status_url
       kyc_status = None
       kyc_message = None
       dim_merchant_date_created_id=get_random_date()
       dim_merchant_date_modified_id=get_random_date()
       dim_merchant_time_created_id=get_random_time()
       dim_merchant_time_modified_id=get_random_time()
       account_details_id = 525252525252
       
       data=(id,paysol_id,amount,status_id,operation_id,merchant_id,invoice_id,currency,country,product_id,message,
             original_txn_id,merchant_txn_id,customer_id,e_customer_id,dim_date_created_id,dim_date_modified_id,dim_time_created_id,
             dim_time_modified_id,workflow_step_id,workflow_id,workflow_version,workflow_name,workflow_description,ip,type,description,
             dim_ip_country_id,dim_ip_city_id,status_url,kyc_status,kyc_message,dim_merchant_date_created_id,dim_merchant_date_modified_id,
             dim_merchant_time_created_id,dim_merchant_time_modified_id,account_details_id)

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
       return txid


            
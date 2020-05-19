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


       #get aleatory merchant_id
       cache_merchants  = get_cache_merchants()
       k = random.choice(list(cache_merchants))
       m =cache_merchants[k]
       v_merchant_id  = m.get('id')
       
       #get aleatory e_customer_id from the selected merchant_id
       l_e_customer   = m.get('e_customer') 
       k=random.choice(l_e_customer)
       v_e_customer_id=k.get('id')

       # aleatory currency&country
       currency_country=get_random_currency_country()

       app.logger.debug("ramdom() merchant_id  : %s " , v_merchant_id)
       app.logger.debug("ramdom() e_customer_id: %s " , v_e_customer_id)
       
       id = None
       #date_created
       #date_modified
       paysol_id=900
       amount=random.randint(1,9)*1000
       status_id=1
       operation_id=2
       merchant_id=v_merchant_id
       invoice_id = None
       currency=currency_country[0]
       country=currency_country[1]
       product_id=101621
       message="Transaction was initiated"
       original_txn_id = None
       merchant_txn_id=17935848
       customer_id=v_e_customer_id
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
       ip="83.149.45.77"
       type="ECOM"
       description="Transfer to 1802727582, id 777777777777"
       dim_ip_country_id = None
       dim_ip_city_id = None
       status_url="https://secure-pay.fxclub.org/ext//ps_epg"
       kyc_status = None
       kyc_message = None
       dim_merchant_date_created_id=get_random_date()
       dim_merchant_date_modified_id=get_random_date()
       dim_merchant_time_created_id=get_random_time()
       dim_merchant_time_modified_id=get_random_time()
       account_details_id = None
       
       data=(id,
             paysol_id,
             amount,
             status_id,
             operation_id,
             merchant_id,
             invoice_id,
             currency,
             country,
             product_id,
             message,
             original_txn_id,
             merchant_txn_id,
             customer_id,
             e_customer_id,
             dim_date_created_id,
             dim_date_modified_id,
             dim_time_created_id,
             dim_time_modified_id,
             workflow_step_id,
             workflow_id,
             workflow_version,
             workflow_name,
             workflow_description,
             ip,
             type,
             description,
             dim_ip_country_id,
             dim_ip_city_id,
             status_url,
             kyc_status,
             kyc_message,
             dim_merchant_date_created_id,
             dim_merchant_date_modified_id,
             dim_merchant_time_created_id,
             dim_merchant_time_modified_id,
             account_details_id
            )

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


            
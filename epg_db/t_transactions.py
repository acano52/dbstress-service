import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random


def insert_t_transaction(merchant , customer):
        
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


       m =merchant
       v_merchant_id  = m.get('id')
       v_status_url   = m.get('default_status_url')
       
       #get random e_customer_id from the selected merchant_id
       l_e_customer   = m.get('e_customer') 
       k=customer
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
       

       dic_txn={
       'id'                              : None,
       'paysol_id'                       : v_paysol_id,
       'amount'                          : random.choice([20,100,50,47.30,1000,1346,848,11000,120,130,140,245,400,650,44.7,55.66,135,560,710,1100,2100,3200]),
       'status_id'                       : random.choice([2,3,5]),
       'operation_id'                    : random.choice([2,3]),
       'merchant_id'                     : v_merchant_id,
       'invoice_id'                      : None,
       'currency'                        : currency_country[0],
       'country'                         : currency_country[1],
       'product_id'                      : v_product_id,
       'message'                         : "Transaction was initiated",
       'original_txn_id'                 : None,
       'merchant_txn_id'                 : get_random_stringlen(random.choice([5,10,15,20])), #ramdom string with random len
       'customer_id'                     : v_customer_id,
       'e_customer_id'                   : v_e_customer_id,
       'dim_date_created_id'             : get_random_date(),
       'dim_date_modified_id'            : get_random_date(),
       'dim_time_created_id'             : get_random_time(),
       'dim_time_modified_id'            : get_random_time(),
       'workflow_step_id'                : None,
       'workflow_id'                     : None,
       'workflow_version'                : None,
       'workflow_name'                   : None,
       'workflow_description'            : None,
       'ip'                              : v_ip,
       'type'                            : "ECOM",
       'description'                     : "Transfer to XXXXXXXXXXXX, id YYYYYYYYYY",
       'dim_ip_country_id'               : None,
       'dim_ip_city_id'                  : None,
       'status_url'                      : v_status_url,
       'kyc_status'                      : None,
       'kyc_message'                     : None,
       'dim_merchant_date_created_id'    : get_random_date(),
       'dim_merchant_date_modified_id'   : get_random_date(),
       'dim_merchant_time_created_id'    : get_random_time(),
       'dim_merchant_time_modified_id'   : get_random_time(),
       'account_details_id'              : 525252525252
       }
              
       txn_data=(dic_txn['id'],
                dic_txn['paysol_id'],
                dic_txn['amount'],
                dic_txn['status_id'],
                dic_txn['operation_id'],
                dic_txn['merchant_id'],
                dic_txn['invoice_id'],
                dic_txn['currency'],
                dic_txn['country'],
                dic_txn['product_id'],
                dic_txn['message'],
                dic_txn['original_txn_id'],
                dic_txn['merchant_txn_id'],
                dic_txn['customer_id'],
                dic_txn['e_customer_id'],
                dic_txn['dim_date_created_id'],
                dic_txn['dim_date_modified_id'],
                dic_txn['dim_time_created_id'],
                dic_txn['dim_time_modified_id'],
                dic_txn['workflow_step_id'],
                dic_txn['workflow_id'],
                dic_txn['workflow_version'],
                dic_txn['workflow_name'],
                dic_txn['workflow_description'],
                dic_txn['ip'],
                dic_txn['type'],
                dic_txn['description'],
                dic_txn['dim_ip_country_id'],
                dic_txn['dim_ip_city_id'],
                dic_txn['status_url'],
                dic_txn['kyc_status'],
                dic_txn['kyc_message'],
                dic_txn['dim_merchant_date_created_id'],
                dic_txn['dim_merchant_date_modified_id'],
                dic_txn['dim_merchant_time_created_id'],
                dic_txn['dim_merchant_time_modified_id'],
                dic_txn['account_details_id'])

       db = MySQLPool(app)
       try:
          conn = db.connection.get_connection()
          cursor = conn.cursor()
          cursor.execute(sql, txn_data)  
          dic_txn['id']=cursor.lastrowid
          conn.commit
          appcache=Cache(app)
          app.logger.debug("TXN: %s .... CACHED" ,  dic_txn['id'])
          appcache.set('cache_txn',dic_txn)          
       except mysql.connector.Error as err:
          app.logger.error(format(sql))
          app.logger.error(txn_data)
          raise err 
       finally:
          cursor.close()
          conn.close()


       return dic_txn





def update_t_transaction():



      sql=" UPDATE t_transactions                                 "\
          "    SET date_modified = NOW(),                         "\
          "         paysol_id = %s,                               "\
          "         amount    = %s,                               "\
          "         status_id = %s,                               "\
          "         operation_id = %s,                            "\
          "         merchant_id= %s,                              "\
          "         invoice_id= %s,                               "\
          "         currency= %s,                                 "\
          "         country= %s,                                  "\
          "         product_id=%s,                                "\
          "         message=%s,                                   "\
          "         original_txn_id=%s,                           "\
          "         merchant_txn_id=%s,                           "\
          "         customer_id=%s,                               "\
          "         e_customer_id=%s,                             "\
          "         dim_date_created_id=%s,                       "\
          "         dim_date_modified_id=%s,                      "\
          "         dim_time_created_id=%s,                       "\
          "         dim_time_modified_id=%s,                      "\
          "         workflow_step_id=%s,                          "\
          "         workflow_id=%s,                               "\
          "         workflow_version=%s,                          "\
          "         workflow_name=%s,                             "\
          "         workflow_description=%s,                      "\
          "         ip=%s,                                        "\
          "         type=%s,                                      "\
          "         description=%s,                               "\
          "         dim_ip_country_id=%s,                         "\
          "         dim_ip_city_id=%s,                            "\
          "         status_url=%s,                                "\
          "         kyc_status=%s,                                "\
          "         kyc_message=%s,                               "\
          "         dim_merchant_date_created_id=%s,              "\
          "         dim_merchant_date_modified_id=%s,             "\
          "         dim_merchant_time_created_id=%s,              "\
          "         dim_merchant_time_modified_id=%s,             "\
          "         account_details_id=%s                         "\
          "  WHERE id = %s"


      #Update txn cache before to update
      appcache=Cache(app)
      dic_txn = appcache.get('cache_txn')

      data=(    dic_txn['paysol_id'],
                dic_txn['amount'],
                dic_txn['status_id'],
                dic_txn['operation_id'],
                dic_txn['merchant_id'],
                dic_txn['invoice_id'],
                dic_txn['currency'],
                dic_txn['country'],
                dic_txn['product_id'],
                dic_txn['message'],
                dic_txn['original_txn_id'],
                dic_txn['merchant_txn_id'],
                dic_txn['customer_id'],
                dic_txn['e_customer_id'],
                dic_txn['dim_date_created_id'],
                dic_txn['dim_date_modified_id'],
                dic_txn['dim_time_created_id'],
                dic_txn['dim_time_modified_id'],
                dic_txn['workflow_step_id'],
                dic_txn['workflow_id'],
                dic_txn['workflow_version'],
                dic_txn['workflow_name'],
                dic_txn['workflow_description'],
                dic_txn['ip'],
                dic_txn['type'],
                dic_txn['description'],
                dic_txn['dim_ip_country_id'],
                dic_txn['dim_ip_city_id'],
                dic_txn['status_url'],
                dic_txn['kyc_status'],
                dic_txn['kyc_message'],
                dic_txn['dim_merchant_date_created_id'],
                dic_txn['dim_merchant_date_modified_id'],
                dic_txn['dim_merchant_time_created_id'],
                dic_txn['dim_merchant_time_modified_id'],
                dic_txn['account_details_id'],
                dic_txn['id'])
      
      db = MySQLPool(app)
      try:
         conn = db.connection.get_connection()
         cursor = conn.cursor()
         cursor.execute(sql, data)  
         app.logger.debug("Rows updated : %s", cursor.rowcount)
         conn.commit
      except mysql.connector.Error as err:
         app.logger.error(format(sql))
         app.logger.error(data)
         raise err 
      finally:
         cursor.close()
         conn.close()
       

import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app



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
              "account_details_id) "\
              "VALUES (%s, NOW(), NOW(), %s, %s, %s, %s, %s, %s, %s )"



#              "currency,"\
#              "country,"\
#              "product_id,"\
#              "message,"\
#              "original_txn_id,"\
#              "merchant_txn_id, "\
#              "customer_id,"\
#              "e_customer_id,"\
#              "dim_date_created_id,"\
#              "dim_date_modified_id,"\
#              "dim_time_created_id,"\
#              "dim_time_modified_id,"\
#              "workflow_step_id,"\
#              "workflow_id,"\
#              "workflow_version,"\
#              "workflow_name,"\
#              "workflow_description,"\
#              "ip,"\
#              "type,"\
#              "description,"\
#              "dim_ip_country_id,"\
#              "dim_ip_city_id,"\
#              "status_url,"\
#              "kyc_status,"\
#              "kyc_message,"\
#              "dim_merchant_date_created_id,"\
#              "dim_merchant_date_modified_id,"\
#              "dim_merchant_time_created_id,"\
#              "dim_merchant_time_modified_id,"\
              

       id = None
       #date_created
       #date_modified
       paysol_id=900
       amount=525252
       status_id=1
       operation_id=2
       merchant_id=10143
       invoice_id = None
       currency="USD"
       country="RU"
       product_id=101621
       message="Transaction was initiated"
       original_txn_id = None
       merchant_txn_id=17935848
       customer_id=101626085327
       e_customer_id=44267514
       dim_date_created_id=20200427
       dim_date_modified_id=20200427
       dim_time_created_id=1174232
       dim_time_modified_id=1174232
       workflow_step_id = None
       workflow_id = None
       workflow_version = None
       workflow_name = None
       workflow_description = None
       ip="83.149.45.77"
       type="ECOM"
       description="Transfer to 1802727582, id 777777777777"
       description = None
       dim_ip_country_id = None
       dim_ip_city_id = None
       status_url="https://secure-pay.fxclub.org/ext//ps_epg"
       kyc_status = None
       kyc_message = None
       dim_merchant_date_created_id=20200427
       dim_merchant_date_modified_id=20200427
       dim_merchant_time_created_id=1184232
       dim_merchant_time_modified_id=1184232
       account_details_id = None
       
       data=(id,
             paysol_id,
             amount,
             status_id,
             operation_id,
             merchant_id,
             invoice_id,
             account_details_id
            )

       app.logger.debug(data)            
            
#            ,amount,status_id,operation_id,merchant_id,currency,country,
#             product_id,message,merchant_txn_id,customer_id,e_customer_id,dim_date_created_id,dim_date_modified_id,
#             dim_time_created_id,dim_time_modified_id,dim_time_created_id,dim_time_modified_id,ip,type,description,
#             status_url,dim_merchant_date_created_id,dim_merchant_date_modified_id,dim_merchant_time_created_id,dim_merchant_time_modified_id)

       db = MySQLPool(app)
       app.logger.info("INSERT t_transactions ...")
       try:
          conn = db.connection.get_connection()
          cursor = conn.cursor()
          cursor.execute(sql, data)  
          app.logger.debug(sql)
          txid=cursor.lastrowid
          conn.commit
       except mysql.connector.Error as err:
          app.logger.error(format(sql))
          raise err 
       finally:
          cursor.close()
          conn.close()
       return txid


            
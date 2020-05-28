from flask import Flask,abort,jsonify
from flask_restful import Api, Resource, reqparse
import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.configuration import *
from epg_utils.cache import *
from epg_db.t_transactions import *
from epg_db.t_optional_parameters import *
from epg_db.t_optional_transactions_params import *
from epg_db.t_transaction_device import *
from epg_db.t_customer_request import *
from epg_db.t_cart_transactions import *
from epg_db.t_fraud_attributes import *
from epg_db.t_transaction_request import *
from epg_db.t_transaction_payment_details import *
from epg_db.e_merchant_call import *
from epg_db.e_customer     import *
from time import sleep



class transactions(Resource):

       
           def get(self):
               with app.app_context():

                    # Select ramdom merchant and client for txn



                    cache_general    = get_cache_general()
                    cache_merchants  = get_cache_merchants()

                    #get random merchant_id
                    k = random.choice(list(cache_merchants))
                    merchant =cache_merchants[k]
                    v_merchant_id  = merchant.get('id')

                    app.logger.debug("ramdom() merchant_id  : %s " , v_merchant_id)
       
            
                    
                    #get random customer_id
                    l_e_customer   = merchant.get('e_customer') 
                    e_customer=random.choice(l_e_customer)
                    v_id                   = e_customer.get('id')
                    v_merchant_customer_id = e_customer.get('merchant_customer_id')
                    v_payfrex_customer_id  = e_customer.get('payfrex_customer_id')
                    app.logger.debug("ramdom() v_payfrex_customer_id: %s " , v_payfrex_customer_id)
                  

                    #12

                    app.logger.debug("STEP 01")
                    v_customer=get_e_customer(v_merchant_id,v_merchant_customer_id)
                    
                    #13
                    app.logger.debug("STEP 02")
                    v_total_success_txn=get_e_customer_success_transactions(v_merchant_id,v_merchant_customer_id)

                    #15 
                    app.logger.debug("STEP 03")
                    v_e_customer_tnx_summary=get_e_customer_tnx_summary(v_merchant_id,v_merchant_customer_id)
                    
                    
                    #16
                    #TODO pendiente account_details_id para que enganche con cus_account_card
                    app.logger.debug("STEP 04")
                    txnid=insert_t_transaction(merchant,e_customer)
                    
                    #18
                    app.logger.debug("STEP 05")
                    insert_t_optional_parameters(v_merchant_id,txnid)

                    #19
                    app.logger.debug("STEP 06")
                    insert_t_optional_transactions_params(txnid)
                    
                    #20
                    app.logger.debug("STEP 07")
                    ret=select_t_transaction_device(txnid)
                    app.logger.debug("STEP 08")
                    insert_t_transaction_device(txnid)

                    #21
                    app.logger.debug("STEP 09")
                    insert_t_customer_request(txnid)

                    #22
                    app.logger.debug("STEP 10")
                    insert_t_cart_transactions(txnid)

                    
                    #23
                    app.logger.debug("STEP 11")
                    x=get_e_customerbyID(e_customer.get('id'))

                    #29
                    app.logger.debug("STEP 12")
                    x=get_e_customerby_payfrex(e_customer.get('payfrex_customer_id'))

                    #30
                    app.logger.debug("STEP 13")
                    x=select_t_optional_transactions_params(txnid)

                    #37
                    appcache=Cache(app)
                    dic_txn = appcache.get(str(txnid))
                    dic_txn['message']= "Transaction was pending"
                    dic_txn['dim_date_modified_id']          = get_random_date()
                    dic_txn['dim_time_modified_id']          = get_random_time()
                    dic_txn['dim_merchant_date_modified_id'] = get_random_date()
                    dic_txn['dim_merchant_time_modified_id'] = get_random_time()
                    dic_txn['sm_action'] = 0
                    dic_txn['threed_enrolment'] = None
                    appcache.set(str(txnid),dic_txn)
                    app.logger.debug("STEP 14")
                    update_t_transaction(txnid)


                    #38
                    app.logger.debug("STEP 15")
                    insert_t_fraud_atributes(txnid)

                    #47
                    appcache=Cache(app)
                    dic_txn = appcache.get(str(txnid))
                    dic_txn['message']                        = 'Transaction was pending' 
                    dic_txn['dim_date_modified_id']           = get_random_date()
                    dic_txn['dim_time_modified_id']           = get_random_time() 
                    dic_txn['workflow_step_id']               = 9999999 
                    dic_txn['workflow_id']                    = 999 
                    dic_txn['workflow_version']               = 9 
                    dic_txn['workflow_name']                  = 'Ecommpay deposit' 
                    dic_txn['dim_merchant_date_modified_id']  = get_random_date() 
                    dic_txn['dim_merchant_time_modified_id']  = get_random_time() 
                    dic_txn['sm_action']                      = 0
                    appcache.set(str(txnid),dic_txn)
                    app.logger.debug("STEP 16")
                    update_t_transaction(txnid)

                    #48
                    app.logger.debug("STEP 17")
                    insert_t_transaction_request(txnid)

                    #50
                    app.logger.debug("STEP 18")
                    insert_t_transaction_payment_details(txnid,1)
                    app.logger.debug("STEP 19")
                    insert_t_transaction_payment_details(txnid,2)
                    app.logger.debug("STEP 20")
                    insert_t_transaction_payment_details(txnid,3)
                    app.logger.debug("STEP 21")
                    insert_t_transaction_payment_details(txnid,4)

                    #54
                    appcache=Cache(app)
                    dic_txn = appcache.get(str(txnid))
                    dic_txn['dim_date_modified_id']           = get_random_date()
                    dic_txn['dim_time_modified_id']           = get_random_time() 
                    dic_txn['dim_merchant_date_modified_id']  = get_random_date() 
                    dic_txn['dim_merchant_time_modified_id']  = get_random_time() 
                    dic_txn['threed_enrolment']  = True
                    appcache.set(str(txnid),dic_txn)
                    app.logger.debug("STEP 22")
                    update_t_transaction(txnid)
                   
                    #56
                    appcache=Cache(app)
                    dic_txn = appcache.get(str(txnid))
                    dic_txn['dim_date_modified_id']           = get_random_date()
                    dic_txn['dim_time_modified_id']           = get_random_time() 
                    dic_txn['dim_merchant_date_modified_id']  = get_random_date() 
                    dic_txn['dim_merchant_time_modified_id']  = get_random_time() 
                    dic_txn['message']= " Transaction is processing" #space to enforce update in #56
                    appcache.set(str(txnid),dic_txn)
                    app.logger.debug("STEP 23")
                    update_t_transaction(txnid)
                    
                    #58
                    appcache=Cache(app)
                    dic_txn = appcache.get(str(txnid))
                    dic_txn['dim_date_modified_id']           = get_random_date()
                    dic_txn['dim_time_modified_id']           = get_random_time() 
                    dic_txn['dim_merchant_date_modified_id']  = get_random_date() 
                    dic_txn['dim_merchant_time_modified_id']  = get_random_time() 
                    dic_txn['message']= "Transaction is processing"
                    app.logger.debug("STEP 24")
                    appcache.set(str(txnid),dic_txn)
                    update_t_transaction(txnid)

                    #61
                    app.logger.debug("STEP 25")
                    insert_e_merchant_call(txnid)

                    #to_json = [cache_merchants]
                    to_json = txnid
                              
               return jsonify(str(to_json)) 

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
from epg_db.e_customer     import *


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
                    v_customer=get_e_customer(v_merchant_id,v_merchant_customer_id)
                    
                    #13
                    v_total_success_txn=get_e_customer_success_transactions(v_merchant_id,v_merchant_customer_id)

                    #15 
                    v_e_customer_tnx_summary=get_e_customer_tnx_summary(v_merchant_id,v_merchant_customer_id)
                    
                    
                    #16
                    #TODO pendiente account_details_id para que enganche con cus_account_card
                    txnid=insert_t_transaction(merchant,e_customer)

                    #18
                    insert_t_optional_parameters(v_merchant_id,txnid)

                    #19
                    insert_t_optional_transactions_params(txnid)
                    
                    #20
                    ret=select_t_transaction_device(txnid)
                    insert_t_transaction_device(txnid)

                    #21
                    insert_t_customer_request(txnid)

                    #22
                    insert_t_cart_transactions(txnid)

                    
                    #23
                    x=get_e_customerbyID(e_customer.get('id'))

                    #29
                    x=get_e_customerby_payfrex(e_customer.get('payfrex_customer_id'))

                    #30
                    x=select_t_optional_transactions_params(txnid)

                    #to_json = [cache_merchants]
                    to_json = x
                              
               return jsonify(str(to_json)) 

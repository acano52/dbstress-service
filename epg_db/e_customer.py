import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random


#11 
def get_e_customer(merchant_id,merchant_customer_id):
       
       db = MySQLPool(app)
       try:
          conn = db.connection.get_connection()
          cursor = conn.cursor(dictionary=True)
          sql = " SELECT * "\
                "   FROM e_customer "\
                "  WHERE merchant_customer_id = %s AND "\
                "        merchant_id = %s AND "\
                "       active = '1' "\
                "  LIMIT 1"
              
          data=(merchant_customer_id,merchant_id,)                
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


#12 
def get_e_customer_success_transactions(merchant_id,merchant_customer_id):
       
       db = MySQLPool(app)
       try:
          conn = db.connection.get_connection()
          cursor = conn.cursor(dictionary=True)

          sql=" SELECT  c . *, "\
              "    count(*) as total_success_transactions, "\
              "    sum(case when operation_id = 2 then 1 else 0 end) as num_success_deposits, "\
              "    sum(case when operation_id = 3 then 1 else 0 end) as num_success_withdraws, "\
              "    sum(case when operation_id = 2 then amount else 0 end) as sum_success_amount_deposit, "\
              "    sum(case when operation_id = 3 then amount else 0 end) as sum_success_amount_withdraws "\
              " FROM t_transactions t join e_customer c ON t.customer_id = c.payfrex_customer_id "\
              " WHERE t.status_id = 3 AND t.merchant_id = %s AND "\
              "   t.customer_id = CONCAT(%s, %s) AND "\
              "   c.merchant_customer_id = %s AND "\
              "   c.merchant_id = %s AND "\
              "   c.active = 1 "
              
          data=(merchant_id,merchant_id,merchant_customer_id,merchant_customer_id,merchant_id,)                
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




#15
def get_e_customer_tnx_summary(merchant_id,merchant_customer_id):
      db = MySQLPool(app)
      try:
          conn = db.connection.get_connection()
          cursor = conn.cursor(dictionary=True)
          sql="SELECT                                           "\
          "    ts.description         AS status,                "\
          "    t.currency             AS currency,              "\
          "    top.operation          AS operation_type,        "\
          "    COUNT(t.id) AS n_transactions,                   "\
          "    SUM(t.amount) AS sum_amount,                     "\
          "    ps.name                AS payment_solution,      "\
          "    ca.card_number_token   AS cav_card_number_token, "\
          "    card_holder_name       AS cav_card_holder_name,  "\
          "    internal_token         AS cav_internal_token,    "\
          "    exp_date               AS cav_expiration_date    "\
          "FROM                                                 "\
          "    t_transactions        t                          "\
          "    INNER JOIN e_payment_solutions   ps ON ( t.paysol_id = ps.id )              "\
          "    INNER JOIN t_status              ts ON ( ts.id = t.status_id )              "\
          "    INNER JOIN t_operations          top ON ( top.id = t.operation_id )         "\
          "    INNER JOIN cus_card_accounts     ca ON ( ca.epg_customer_id = t.customer_id "\
          "                                         AND t.paysol_id = ca.paysol_id         "\
          "                                         AND t.account_details_id = ca.id )     "\
          "WHERE                                                                           "\
          "    t.customer_id = concat(%s, %s)                                              "\
          "    AND t.amount != 0                                                           "\
          "    AND ca.disable = 0                                    "\
          "    AND ps.name IN (                                      "\
          "        'creditcards',                                    "\
          "        'INGDirect',                                      "\
          "        'BANCO COOPERATIVO POS',                          "\
          "        'Bankinter',                                      "\
          "        'CAJA RURAL DE TERUEL POS', "\
          "        'CashU', "\
          "        'CAJA DE CREDITO COOPERATIVO POS', "\
          "        'BANCO FINANTIA SOFINLOC POS', "\
          "        'Lacaixa', "\
          "        'connectum', "\
          "        'CAJA RURAL PROVINCIAL DE GRANADA POS', "\
          "        'NetBanxCreditCard', "\
          "        'Ibercaja', "\
          "        'CAJA RURAL PROVINCIAL DE SORIA POS', "\
          "        'BANCO DE CREDITO SOCIAL COOPERATIVO POS', "\
          "        'CAJA RURAL DE CIUDAD REAL POS', "\
          "        'CAJA RURAL DE ALMENDRALEJO POS', "\
          "        'NetPay', "\
          "        'Vantiv', "\
          "        'Targobank', "\
          "        'CATALUNYA CAIXA POS', "\
          "        'UNO-E POS', "\
          "        'BancoCooperativo', "\
          "        'VOGOGO', "\
          "        'Ecommpay', "\
          "        'CAJA RURAL NUESTRA SENORA DEL ROSARIO POS', "\
          "        'OKPay', "\
          "        'Bankinter', "\
          "        'BANCA MARCH POS', "\
          "        'CAJA RURAL DEL SUR POS', "\
          "        'CAJA RURAL DE BURGOS FP SEG CASTEL POS', "\
          "        'ING DIRECT POS', "\
          "        'SafeCharge', "\
          "        'SecureTrading', "\
          "        'PAYDOO-WIRECARD', "\
          "        'BANCO ALCALA POS', "\
          "        'OchapayDirect', "\
          "        'CashFlows', "\
          "        'Decta', "\
          "        'WireCard', "\
          "        'AlliedWallet', "\
          "        'CAIXA RURAL GALEGA POS', "\
          "        'CAJA RURAL SANTA CRUZ DE TENERIFE POS', "\
          "        'CAIXA POPULAR DE VALENCIA POS', "\
          "        'Commercegate', "\
          "        'CaixaPucPuce', "\
          "        'DEUTSCHE BANK POS', "\
          "        'OnlineDeposit', "\
          "        'Ibercaja', "\
          "        'CAJA RURAL PROVINCIAL DE ASTURIAS POS', "\
          "        'UniversalPay', "\
          "        'KutxaBank', "\
          "        'BANCO CEISS POS', "\
          "        'CAJA RURAL DE ALBACETE CR CUENCA POS', "\
          "        'Cardpay', "\
          "        'ChargebackHunter', "\
          "        'CAJA ESPANA POS', "\
          "        'IpayOptions', "\
          "        'CAIXA RURAL LA VALL POS', "\
          "        'CAIXA POPULAR POS', "\
          "        'Bbva', "\
          "        'Santander', "\
          "        'BANKINTER POS', "\
          "        'EMerchantPayCC', "\
          "        'WorldPay', "\
          "        'CAJA COOPERATIVA DE ARQUITECTOS POS', "\
          "        'CAJARURAL DE CASAS POS', "\
          "        'Unicaja', "\
          "        'RedsysPucPuce', "\
          "        'Clearhaus', "\
          "        'Ecp', "\
          "        'CAJA COLEGIO INGENIEROS CATALUNYA POS', "\
          "        'ElavonDcc', "\
          "        'mercadopagocard', "\
          "        'Bancageral', "\
          "        'BARCLAYS BANK PLC POS', "\
          "        'Paydoo', "\
          "        'Alliance', "\
          "        'UNOE-BANK POS', "\
          "        'EPro', "\
          "        'Bankia', "\
          "        'CAJA RURAL DE GUISSONA POS', "\
          "        'KUTXABANK POS', "\
          "        'BANCO CAMINOS POS', "\
          "        'CAIXA RURAL DE L ALCUDIA POS', "\
          "        'truevo', "\
          "        'TRIODOS BANK POS', "\
          "        'RedBaron', "\
          "        'AccentpayCC', "\
          "        'MonetaCreditCard', "\
          "        'CAJA RURAL D ALGEMESI POS', "\
          "        'Paypoint', "\
          "        'WinPayCreditCard', "\
          "        'NOVO BANCO POS', "\
          "        'BANKOA POS', "\
          "        'BANCO SABADELL POS', "\
          "        'EPG', "\
          "        'AlliedWallet_DirectSale', "\
          "        'Processing', "\
          "        'Realex', "\
          "        'CAJA RURAL DE BURGOS POS', "\
          "        'AIB', "\
          "        'IBERIACARDS POS', "\
          "        'CAJASIETE POS', "\
          "        'BANCO POPULAR POS', "\
          "        'BANCA PUEYO POS', "\
          "        'COMERCIA GLOBAL PAYMENTS POS', "\
          "        'CAJA RURAL DE ZAMORA POS', "\
          "        'CAJA RURAL SAN JOSE DE ALMASSORA POS', "\
          "        'WebMoney', "\
          "        'CreditCards', "\
          "        'BankiaPucPuce', "\
          "        'BANCO MEDIOLANUM POS', "\
          "        'CAJA RURAL DE GIJON POS', "\
          "        'CreditGuard', "\
          "        'worldpayg', "\
          "        'TSI', "\
          "        'PaymentTrust', "\
          "        'TARGOBANK POS', "\
          "        'CAJA RURAL DE NAVARRA POS', "\
          "        'AMEX', "\
          "        'BancoCooperativo', "\
          "        'CAJA RURAL DE SALAMANCA POS', "\
          "        'CAJASUR POS', "\
          "        'processing', "\
          "        'BancoPopular', "\
          "        'INGDirect', "\
          "        'UniversalPayRedsys', "\
          "        'BBVAPucPuce', "\
          "        'Bankia', "\
          "        'Sabadell', "\
          "        'WalPay', "\
          "        'CAJA RURAL CASTILLA LA MANCHA POS', "\
          "        'CAJA RURAL DE EXTREMADURA POS', "\
          "        'Caixageral', "\
          "        'CAJA RURAL S. ISIDRO DE VALL DE UXO POS', "\
          "        'PayVision', "\
          "        'CAJA RURAL DE JAEN POS', "\
          "        'OmniPay', "\
          "        'be2bill', "\
          "        'GLOBALCAJA POS', "\
          "        'ABANCA CORPORACION BANCARIA POS', "\
          "        'LABORAL KUTXA POS', "\
          "        'Moneta', "\
          "        'CAJA RURAL DE LUGO POS', "\
          "        'BANCOFAR POS', "\
          "        'SantanderPucPuce', "\
          "        'CAJA RURAL CENTRAL POS', "\
          "        'CAJAMAR POS', "\
          "        'Barclays', "\
          "        'CAJA RURAL DE ARAGON POS', "\
          "        'CAJA RURAL DE UTRERA POS', "\
          "        'SwiftVoucher', "\
          "        'Bancomer', "\
          "        'CPCGate', "\
          "        'Elavon' "\
          "     ) "\
          " GROUP BY "\
          "     t.status_id, "\
          "     t.currency, "\
          "     t.operation_id, "\
          "     ca.internal_token "\
          " ORDER BY "\
          "     t.status_id "

          data=(merchant_id,merchant_customer_id,)                
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
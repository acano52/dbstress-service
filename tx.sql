===========================
Transaction was initiated
===========================



020-04-29T08:40:43.313208Z     11186818 Query 


select decryptsql0_.id as id1_0_, decryptsql0_.crypto_mode as crypto_m2_0_, decryptsql0_.date_created as date_cre3_0_, decryptsql0_.decrypted_data as decrypte4_0_, decryptsql0_.mercha        nt_id as merchant5_0_, decryptsql0_.token as token6_0_, decryptsql0_.transaction_id as transact7_0_ from decrypted_details decryptsql0_ where decryptsql0_.merchant_id=10162 and decryptsql0_.token='a34293b2-18bf-49ce-b601-553434a35c82'



insert into decrypted_details (crypto_mode, date_created, decrypted_data, merchant_id, token, transaction_id) values ('AES_ECB', '2020-04-29 08:40:43.288', '{"country":"RU","lastName"        :"Khusnutdinov","city":"Moskva","customerHasDeposited":"0","statusURL":"https://secure-pay.fxclub.org/ext//ps_epg","description":"Transfer to 13225769, id 17950342","language":"ru","maskedCardNumber":"533208****8658","customerCount        ry":"RU","expDate":"1021","chPhone":"79998241182","merchantId":"10162","customerEmail":"demon2411@mail.ru","chPostCode":"117209","customerId":"532779","merchantTransactionId":"17950342","addressLine1":"ulitca Perekopskaia dom 6 kva        rtira 26","currency":"RUB","state":"RUS","chName":"DMITRII KHUSNUTDINOV","merchantPassword":"b36cb7cf-4e13-401d-902b-95ea970e8d2c","amount":"11400","productId":"101621","chState":"RUS","ipAddress":"94.25.172.140","cardNumberToken":        "6915774284658658","cardType":"MASTERCARD","cvnNumber":"****","successURL":"https://mobile-lbx-upp-etf.libertex.org:443/result/dp/succeeded?payment_id","telephone":"79998241182","errorURL":"https://mobile-lbx-upp-etf.libertex.org:4        43/result/dp/failed?payment_id","firstName":"Dmitrii","cancelURL":"https://mobile-lbx-upp-etf.libertex.org:443/result/dp/failed?payment_id","paymentSolution":"creditcards","dob":"24-11-1982","chCity":"Moskva","operationType":"debit        ","postCode":"117209","rememberMe":"0","merchantParams":"firstDeposit:false;merchant:BVI;gateway:MOBILE_LIBERTEX"}', 10162, 'a34293b2-18bf-49ce-b601-553434a35c82', null)

token - a34293b2-18bf-49ce-b601-553434a35c82




SELECT * FROM e_customer WHERE merchant_customer_id = '532779' AND merchant_id = 10162 AND active = '1' LIMIT 1

SELECT  c . *, count(*) as total_success_transactions, sum(case when operation_id = 2 then 1 else 0 end) as num_success_deposits, sum(case when operation_id = 3 then 1 else 0 end) as         num_success_withdraws, sum(case when operation_id = 2 then amount else 0 end) as sum_success_amount_deposit, sum(case when operation_id = 3 then amount else 0 end) as sum_success_amount_withdraws 
FROM t_transactions t join e_custom        er c 
ON t.customer_id = c.payfrex_customer_id 
WHERE t.status_id = 3 AND t.merchant_id = 10162 AND t.customer_id = CONCAT(10162, '532779') AND c.merchant_customer_id = '532779' AND c.merchant_id = 10162 AND c.active = 1


SELECT 1
========

 SELECT ts.description as status, t.currency as currency, top.operation as operationType, count(*) AS n_transactions, sum(t.amount) as sum_amount , ps.name AS payment_solution, ca.account as cav_account_id
                        FROM
                        t_transactions t
                        INNER JOIN
                                e_payment_solutions ps on (t.paysol_id = ps.id)
                        INNER JOIN
                                t_status ts on (ts.id = t.status_id)
                        INNER JOIN
                                t_operations top on (top.id = t.operation_id)
                        JOIN
                                cus_accounts ca ON (ca.customer_id = '532779' AND t.paysol_id = ca.paysol_id AND ca.merchant_id = '10162' AND t.account_details_id = ca.id)
                        WHERE
                                t.customer_id = CONCAT('10162','532779')
                                AND t.amount != 0
                        AND
                                ca.disable = 0
                          AND ps.name IN
                                 (
                                   'creditcards'
                            ,
                                   'INGDirect'
                            ,
                                   'BANCO COOPERATIVO POS'
                            ,
                                   'Bankinter'
                            ,
                                   'CAJA RURAL DE TERUEL POS'
                            ,
                                   'CashU'
                            ,
                                   'CAJA DE CREDITO COOPERATIVO POS'
                            ,
                                   'BANCO FINANTIA SOFINLOC POS'
                            ,
                                   'Lacaixa'
                            ,
                                   'connectum'
                            ,
                                   'CAJA RURAL PROVINCIAL DE GRANADA POS'
                            ,
                                   'NetBanxCreditCard'
                            ,
                                   'Ibercaja'
                            ,
                                   'CAJA RURAL PROVINCIAL DE SORIA POS'
 ,
                                   'BANCO DE CREDITO SOCIAL COOPERATIVO POS'
                            ,
                                   'CAJA RURAL DE CIUDAD REAL POS'
                            ,
                                   'CAJA RURAL DE ALMENDRALEJO POS'
                            ,
                                   'NetPay'
                            ,
                                   'Vantiv'
                            ,
                                   'Targobank'
                            ,
                                   'CATALUNYA CAIXA POS'
                            ,
                                   'UNO-E POS'
                            ,
                                   'BancoCooperativo'
                            ,
                                   'VOGOGO'
                            ,
                                   'Ecommpay'
                            ,
                                   'CAJA RURAL NUESTRA SENORA DEL ROSARIO POS'
                            ,
                                   'OKPay'
                            ,
                                   'Bankinter'
                            ,
                                   'BANCA MARCH POS'
                            ,
                                   'CAJA RURAL DEL SUR POS'
                            ,
                                   'CAJA RURAL DE BURGOS FP SEG CASTEL POS'
                            ,
                                   'ING DIRECT POS'
                            ,
                                   'SafeCharge'
                            ,
                                   'SecureTrading'
                            ,
                                   'PAYDOO-WIRECARD'
                            ,
                                   'BANCO ALCALA POS'
                            ,
                                   'OchapayDirect'
                            , 
'CashFlows'
                            ,
                                   'Decta'
                            ,
                                   'WireCard'
                            ,
                                   'AlliedWallet'
                            ,
                                   'CAIXA RURAL GALEGA POS'
                            ,
                                   'CAJA RURAL SANTA CRUZ DE TENERIFE POS'
                            ,
                                   'CAIXA POPULAR DE VALENCIA POS'
                            ,
                                   'Commercegate'
                            ,
                                   'CaixaPucPuce'
                            ,
                                   'DEUTSCHE BANK POS'
                            ,
                                   'OnlineDeposit'
                            ,
                                   'Ibercaja'
                            ,
                                   'CAJA RURAL PROVINCIAL DE ASTURIAS POS'
                            ,
                                   'UniversalPay'
                            ,
                                   'KutxaBank'
                            ,
                                   'BANCO CEISS POS'
                            ,
                                   'CAJA RURAL DE ALBACETE CR CUENCA POS'
                            ,
                                   'Cardpay'
                            ,
                                   'ChargebackHunter'
                            ,
                                   'CAJA ESPANA POS'
                            ,
                                   'IpayOptions'
                            ,
                                   'CAIXA RURAL LA VALL POS'
                            ,
                                   'CAIXA POPULAR POS'
                            ,
                                   'Bbva'
                            ,
                                   'Santander'
                            ,
                                   'BANKINTER POS'
                            ,
                                   'EMerchantPayCC'
                            ,
                                   'WorldPay'
                            ,
                                   'CAJA COOPERATIVA DE ARQUITECTOS POS'
                            ,
                                   'CAJARURAL DE CASAS POS'
                            ,
                                   'Unicaja'
                            ,
                                   'RedsysPucPuce'
                            ,
                                   'Clearhaus'
                            ,
                                   'Ecp'
                            ,       
                                   'CAJA COLEGIO INGENIEROS CATALUNYA POS'
                            ,
                                   'ElavonDcc'
                            ,
                                   'mercadopagocard'
                            ,
                                   'Bancageral'
                            ,
                                   'BARCLAYS BANK PLC POS'
                            ,
                                   'Paydoo'
                            ,
                                   'Alliance'
                            ,
                                   'UNOE-BANK POS'
                            ,
                                   'EPro'
                            ,
                                   'Bankia'
                            ,
                                   'CAJA RURAL DE GUISSONA POS'
                            ,
                                   'KUTXABANK POS'
                            ,
                                   'BANCO CAMINOS POS'
                            ,
                                   'CAIXA RURAL DE L ALCUDIA POS'
                            ,
                                   'truevo'
                            ,
                                   'TRIODOS BANK POS'
                            ,
                                   'RedBaron'
                            ,
                                   'AccentpayCC'
                            ,
                                   'MonetaCreditCard'
                            ,
                                   'CAJA RURAL D ALGEMESI POS'
                            ,
                                   'Paypoint'
                            ,
                                   'WinPayCreditCard'
                            ,
                                   'NOVO BANCO POS'
                            ,
                                   'BANKOA POS'
                            ,
                                   'BANCO SABADELL POS'
                            ,
                                   'EPG'
                            ,
                                   'AlliedWallet_DirectSale'
                            ,
                                   'Processing'
                            ,
                                   'Realex'
                            ,
                                   'CAJA RURAL DE BURGOS POS'
                            ,
                                   'AIB'
                            ,
                                   'IBERIACARDS POS'
                            ,
                                   'CAJASIETE POS'
                            ,
                                   'BANCO POPULAR POS'
                            ,
                                   'BANCA PUEYO POS'
                            ,
                                   'COMERCIA GLOBAL PAYMENTS POS'
                            ,
                                   'CAJA RURAL DE ZAMORA POS'
                            ,
                                   'CAJA RURAL SAN JOSE DE ALMASSORA POS'
                            ,
                                   'WebMoney'
                            ,
                                   'CreditCards'
                            ,
                                   'BankiaPucPuce'
                            ,
                                   'BANCO MEDIOLANUM POS'
                            ,
                                   'CAJA RURAL DE GIJON POS'
                            ,
                                   'CreditGuard'
                            ,
                                   'worldpayg'
                            ,
                                   'TSI'
                            ,
                                   'PaymentTrust'
                            ,
                                   'TARGOBANK POS'
                            ,
                                   'CAJA RURAL DE NAVARRA POS'
                            ,
                                   'AMEX'
                            ,
                                   'BancoCooperativo'
                            ,
                                   'CAJA RURAL DE SALAMANCA POS'
                            ,
                                   'CAJASUR POS'
                            ,
                                   'processing'
                            ,
                                   'BancoPopular'
                            ,
                                   'INGDirect'
                            ,
                                   'UniversalPayRedsys'
                            ,
                                   'BBVAPucPuce'
                            ,
                                   'Bankia'
                            ,
                                   'Sabadell'
                            ,
                                   'WalPay'
                            ,
                                   'CAJA RURAL CASTILLA LA MANCHA POS'
                            ,
                                   'CAJA RURAL DE EXTREMADURA POS'
                            ,
                                   'Caixageral'
                            ,
                                   'CAJA RURAL S. ISIDRO DE VALL DE UXO POS'
                            ,
                                   'PayVision'
                            ,
                                   'CAJA RURAL DE JAEN POS'
                            ,
                                   'OmniPay'
                            ,
                                   'be2bill'
                            ,
                                   'GLOBALCAJA POS'
                            ,
                                   'ABANCA CORPORACION BANCARIA POS'
                            ,
                                   'LABORAL KUTXA POS'
                            ,
                                   'Moneta'
                            ,
                                   'CAJA RURAL DE LUGO POS'
                            ,
                                   'BANCOFAR POS'
                            ,
                                   'SantanderPucPuce'
                            ,
                                   'CAJA RURAL CENTRAL POS'
                            ,
                                   'CAJAMAR POS'
                            ,
                                   'Barclays'
                            ,
                                   'CAJA RURAL DE ARAGON POS'
                            ,
                                   'CAJA RURAL DE UTRERA POS'
                            ,
                                   'SwiftVoucher'
                            ,
                                   'Bancomer'
                            ,
                                   'CPCGate'
                            ,
                                   'Elavon'
                            )

   GROUP BY
                                t.status_id , t.currency, t.operation_id, ca.account
                        ORDER by
                                t.status_id



SELECT 2
========
 SELECT ts.description as status, t.currency as currency, top.operation as operation_type, count(*) AS n_transactions, sum(t.amount) as sum_amount , ps.name AS payment_solution, ca.account_number as cav_account_number , holder as cav_holder, iban as cav_iban

 
 SELECT 3
 ========
                                
 SELECT ts.description       AS status,
                       t.currency           AS currency,
                       top.operation        AS operation_type,
                       Count(t.id)          AS n_transactions,
                       Sum(t.amount)        AS sum_amount,
                       ps.name              AS payment_solution,
                       ca.card_number_token AS cav_card_number_token,
                       card_holder_name     AS cav_card_holder_name,
                       internal_token       AS cav_internal_token,
                       exp_date             AS cav_expiration_date
                               
                                
INSERT t_transaction
=====================
into t_transactions (id,date_created,date_modified,paysol_id,amount,status_id, operation_id, merchant_id, invoice_id, currency, country, product_id, message, original_txn_id, merchant_txn_id, customer_id, e_customer_id, dim_date_created_id, dim_date_modified_id, dim_time_created_id, dim_time_modified_id, workflow_step_id, workflow_id, workflow_version, workflow_name, workflow_description, ip, type, description, dim_ip_country_id, dim_ip_city_id, status_url, kyc_status, kyc_message, dim_merchant_date_created_id, dim_merchant_date_modified_id, dim_merchant_time_created_id, dim_merchant_time_modified_id, account_details_id) VALUES (null,NOW(),'2020-04-29 08:40:43.498',900,11400,1, 2,10162,null, 'RUB', 'RU', 101621, 'Transaction was initiated', null, '17950342', '10162532779', 42071214, 20200429, 20200429, 1084043,1084043, null,null , null,null,null, '94.25.172.140', 'ECOM', 'Transfer to 13225769, id 17950342', null, null, 'https://secure-pay.fxclub.org/ext//ps_epg', null, null, 20200429, 20200429, 1094043,1094043,null)


Optional Parameters
===================
 SELECT merchant_id, display_name as display_name, opt_param_col_id
                FROM a_attribute
                WHERE merchant_id is not null
                AND merchant_id = 10162
                AND opt_param_col_id is not null

                
 INSERT INTO t_optional_params
                 (
                        `transaction_id`
                 ,
                        `merchant_id`
                 ,
                        `1`
                 ,
                        `11`
                 ,
                        `6`
                 )
                VALUES
                 (
                        '122370798'
                 ,
                        '10162'
                 ,
                        'false'
                 ,
                        'BVI'
                 ,
                        'MOBILE_LIBERTEX'
                 )

Optional_transactions_parameters
================================
INSERT INTO t_optional_transactions_params (transaction_id, value, key_value) VALUES (122370798, 'false', 'firstDeposit')
2020-04-29T08:40:43.585731Z     11186552 Query  select @@session.tx_read_only
2020-04-29T08:40:43.594998Z     11186552 Query  INSERT INTO t_optional_transactions_params (transaction_id, value, key_value) VALUES (122370798, 'BVI', 'merchant')
2020-04-29T08:40:43.605192Z     11186552 Query  select @@session.tx_read_only
2020-04-29T08:40:43.614253Z     11186552 Query  INSERT INTO t_optional_transactions_params (transaction_id, value, key_value) VALUES (122370798, 'MOBILE_LIBERTEX', 'gateway')


t_transaction_device
=====================
 select transactio0_.transaction_id as transact1_2_0_, transactio0_.device_type as device_t2_2_0_ from t_transaction_device transactio0_ where transactio0_.transaction_id=122370798
2020-04-29T08:40:43.637989Z     11188570 Query  SELECT USER()
2020-04-29T08:40:43.642942Z     11186552 Query  select @@session.tx_read_only
2020-04-29T08:40:43.651729Z     11186552 Query  insert into t_transaction_device (device_type, transaction_id) values ('DESKTOP', 122370798)



decrypted_details
=================
select decryptsql0_.id as id1_0_, decryptsql0_.crypto_mode as crypto_m2_0_, decryptsql0_.date_created as date_cre3_0_, decryptsql0_.decrypted_data as decrypte4_0_, decryptsql0_.merchant_id as merchant5_0_, decryptsql0_.token as token6_0_, decryptsql0_.transaction_id as transact7_0_ from decrypted_details decryptsql0_ where decryptsql0_.merchant_id=10162 and decryptsql0_.token='a34293b2-18bf-49ce-b601-553434a35c82'

update decrypted_details set crypto_mode='AES_ECB', date_created='2020-04-29 08:40:43', decrypted_data='{"country":"RU","lastName":"Khusnutdinov","city":"Moskva","customerHasDeposited        ":"0","statusURL":"https://secure-pay.fxclub.org/ext//ps_epg","description":"Transfer to 13225769, id 17950342","language":"ru","maskedCardNumber":"533208****8658","customerCountry":"RU","expDate":"1021","chPhone":"79998241182","me        rchantId":"10162","customerEmail":"demon2411@mail.ru","chPostCode":"117209","customerId":"532779","merchantTransactionId":"17950342","addressLine1":"ulitca Perekopskaia dom 6 kvartira 26","currency":"RUB","state":"RUS","chName":"DM        ITRII KHUSNUTDINOV","merchantPassword":"b36cb7cf-4e13-401d-902b-95ea970e8d2c","amount":"11400","productId":"101621","chState":"RUS","ipAddress":"94.25.172.140","cardNumberToken":"6915774284658658","cardType":"MASTERCARD","cvnNumber        ":"****","successURL":"https://mobile-lbx-upp-etf.libertex.org:443/result/dp/succeeded?payment_id","telephone":"79998241182","errorURL":"https://mobile-lbx-upp-etf.libertex.org:443/result/dp/failed?payment_id","firstName":"Dmitrii"        ,"cancelURL":"https://mobile-lbx-upp-etf.libertex.org:443/result/dp/failed?payment_id","paymentSolution":"creditcards","dob":"24-11-1982","chCity":"Moskva","operationType":"debit","postCode":"117209","rememberMe":"0","merchantParam        s":"firstDeposit:false;merchant:BVI;gateway:MOBILE_LIBERTEX"}', merchant_id=10162, token='a34293b2-18bf-49ce-b601-553434a35c82', transaction_id=122370798 where id=38836623


t_customer_request
==================
 INSERT INTO `t_customer_request`(`date_created`, `transaction_id`, `user_agent`, `timeout`, `rating`)VALUES ('2020-04-29 08:40:43.703', 122370798, 'Apache-HttpClient/4.5.8 (Java/11.0.4)', null, null)


t_card_transactions
===================
 INSERT INTO `t_cart_transactions`(`date_created`, `gift`, `transaction_id`, `cus_invoice_address_id`, `cus_delivery_method_id`)VALUES ('2020-04-29 08:40:43.703', 0, 122370798, null, null)


532779



===========================
Transaction was Pending
===========================


===========================
Transaction in Process
===========================



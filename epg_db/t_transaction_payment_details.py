import mysql.connector
from flask_mysqlpool import MySQLPool
from flask_caching import Cache
from flask import current_app as app
from epg_utils.cache import *
import random
import json


def insert_t_transaction_payment_details(txnid,option):

       appcache=Cache(app)
       dic_txn = appcache.get(str(txnid)) 

       

       s_json1 = {
                  "status":"AWAITING_PAYSOL",
                  "transactionId": dic_txn['id'],
                  "paymentTransactionId":dic_txn['id'],
                  "dateCreated":str(datetime.now()),
                  "dateModified":str(datetime.now()),
                  "details":{
                           "status":"success",
                           "request_id":"939edb9ef668aa283a7914bf83569684af336140-5fa2f2954dc1bf10e122b97248b67b875cb30a10-00045975",
                           "project_id":677,
                           "payment_id":dic_txn['id']
                            },
                  "method":"SETTLE",
                  "paysolMessage":"Transaction is processing",
                  "paysolErrorMessage":"Transaction is processing",
                  "paysolId": dic_txn['paysol_id']
                }
       s_json2 = {
                  "md":"",
                  "pareq":"",
                  "acsUrl":"",
                  "method":"3DS-PAY-ENROLLMENT",
                  "status":"processing",
                  "details":"{\"project_id\":677,\"payment\":{\"id\":\"122370798\",\"type\":\"purchase\",\"status\":\"processing\",\"date\":\"2020-04-29T08:40:45+0000\",\"method\":\"card\",\"sum\":{\"amount\":1140000,\"currency\":\"RUB\"},\"description\":\"\"},\"account\":{\"number\":\"533208******8658\",\"type\":\"mastercard\",\"card_holder\":\"DMITRII KHUSNUTDINOV\",\"expiry_month\":\"10\",\"expiry_year\":\"2021\"},\"customer\":{\"id\":\"532779\",\"phone\":\"79998241182\"},\"operations\":[{\"id\":45974000023031,\"type\":\"sale\",\"status\":\"processing\",\"date\":\"2020-04-29T08:40:45+0000\",\"created_date\":\"2020-04-29T08:40:45+0000\",\"request_id\":\"939edb9ef668aa283a7914bf83569684af336140-5fa2f2954dc1bf10e122b97248b67b875cb30a10-00045975\",\"sum_initial\":{\"amount\":1140000,\"currency\":\"RUB\"},\"sum_converted\":{\"amount\":1140000,\"currency\":\"RUB\"},\"code\":\"9999\",\"message\":\"Awaiting processing\",\"eci\":\"00\",\"provider\":{\"id\":12,\"payment_id\":\"\",\"endpoint_id\":12}}],\"signature\":\"3zZmW39Q548TxlMz+gqLpa6boHhQHdv+qAZAjB79FteL\\/pwvji4QFxD3pXJuEbPUGH2eYwP\\/0RLJl7vUllfOAg==\"}\n",
                  "paysolId":dic_txn['paysol_id'],
                  "dateCreated":str(datetime.now()),
                  "dateModified":str(datetime.now()),
                  "paysolMessage":"Awaiting processing",
                  "transactionId":dic_txn['id'],
                  "paymentTransactionId":dic_txn['id']
               }
       s_json3 = s_json2
       s_json4 = {
                  "md":"eyJwdXJjaGFzZV9vcGVyYXRpb25faWQiOjQ1OTc0MDAwMDIzMDMxLCJwcm9qZWN0X2lkIjo2NzcsInBheW1lbnRfaWQiOiIxMjIzNzA3OTgiLCJwbHVzX21kIjoiMjg3NDQzNzIxMDUwIn0=",
                  "pareq":"eJxVUl1vwjAM/CuIF6RJIx8tUJAbxFam8QBjjD1PVepBJ9pCmg7493NYO1ikSL5zcrHPgfEp27W+0ZRpkYcd0eWdFua6SNJ8E3be10/3QWesYL01iNEb6sqggjmWZbzBVpqEbV4vGQx83xtIwXu8rWA5WeFBQS2sSLcrgTWQFIzexrlVEOvDw2yhep4MvB6wGkKGZhapWntKW3iSA/ulIY8zVK93KyHoygWALqrcmrPq+x6wBkBldmpr7X7EmMEstUUW264uMgbMpYBdC1lWLipJ6pQmah5NjvU+v0SaL6K5N/+aHhfrSQjMnYAktqgkl5z7ctjiwcjnI78P7MJDnLkalBA+511OpdcE7N07k5usS96SQCYbmkHTS4MAT/siRzpBTv7FkGCpVYKfcbWzH9RaRiwV4Vhg16Yen53X2pJ9wyENaigHvnB+XyinnZJhUgh+EXcAmLvE6lGyeuoU/fsNP28ouVE=",
                  "acsUrl":"https://ds1.mirconnect.ru:443/sc/pareq",
                  "method":"3DS-PAY-ENROLLMENT",
                  "status":"awaiting 3ds result",
                  "details":"{\"project_id\":677,\"payment\":{\"id\":\"122370798\",\"type\":\"purchase\",\"status\":\"awaiting 3ds result\",\"date\":\"2020-04-29T08:40:47+0000\",\"method\":\"card\",\"sum\":{\"amount\":1140000,\"currency\":\"RUB\"},\"description\":\"\"},\"account\":{\"number\":\"533208******8658\",\"type\":\"mastercard\",\"card_holder\":\"DMITRII KHUSNUTDINOV\",\"expiry_month\":\"10\",\"expiry_year\":\"2021\"},\"customer\":{\"id\":\"532779\",\"phone\":\"79998241182\"},\"operations\":[{\"id\":45974000023031,\"type\":\"sale\",\"status\":\"awaiting 3ds result\",\"date\":\"2020-04-29T08:40:47+0000\",\"created_date\":\"2020-04-29T08:40:45+0000\",\"request_id\":\"939edb9ef668aa283a7914bf83569684af336140-5fa2f2954dc1bf10e122b97248b67b875cb30a10-00045975\",\"sum_initial\":{\"amount\":1140000,\"currency\":\"RUB\"},\"sum_converted\":{\"amount\":1140000,\"currency\":\"RUB\"},\"code\":\"19999\",\"message\":\"Awaiting processing\",\"eci\":\"00\",\"provider\":{\"id\":12,\"payment_id\":\"287443721050\",\"auth_code\":\"\",\"endpoint_id\":12}}],\"acs\":{\"pa_req\":\"eJxVUl1vwjAM\\/CuIF6RJIx8tUJAbxFam8QBjjD1PVepBJ9pCmg7493NYO1ikSL5zcrHPgfEp27W+0ZRpkYcd0eWdFua6SNJ8E3be10\\/3QWesYL01iNEb6sqggjmWZbzBVpqEbV4vGQx83xtIwXu8rWA5WeFBQS2sSLcrgTWQFIzexrlVEOvDw2yhep4MvB6wGkKGZhapWntKW3iSA\\/ulIY8zVK93KyHoygWALqrcmrPq+x6wBkBldmpr7X7EmMEstUUW264uMgbMpYBdC1lWLipJ6pQmah5NjvU+v0SaL6K5N\\/+aHhfrSQjMnYAktqgkl5z7ctjiwcjnI78P7MJDnLkalBA+511OpdcE7N07k5usS96SQCYbmkHTS4MAT\\/siRzpBTv7FkGCpVYKfcbWzH9RaRiwV4Vhg16Yen53X2pJ9wyENaigHvnB+XyinnZJhUgh+EXcAmLvE6lGyeuoU\\/fsNP28ouVE=\",\"acs_url\":\"https:\\/\\/ds1.mirconnect.ru:443\\/sc\\/pareq\",\"md\":\"eyJwdXJjaGFzZV9vcGVyYXRpb25faWQiOjQ1OTc0MDAwMDIzMDMxLCJwcm9qZWN0X2lkIjo2NzcsInBheW1lbnRfaWQiOiIxMjIzNzA3OTgiLCJwbHVzX21kIjoiMjg3NDQzNzIxMDUwIn0=\"},\"signature\":\"MuoYjA\\/59QRybXWd24XRU0+N3PTQeKMF6U6UfvCw8z+nY46z\\/kVriueVR7nmQL+4rehLyTsb+5TUm1P2tjfpIA==\"}\n",
                  "paysolId":dic_txn['paysol_id'],
                  "dateCreated":str(datetime.now()),
                  "dateModified":str(datetime.now()),
                  "paysolMessage":"Awaiting processing",
                  "transactionId":dic_txn['id'],
                  "paymentTransactionId":dic_txn['id']
                }

       if option == 1:
          s_json=s_json1
       if option == 2:
          s_json=s_json2
       if option == 3:
          s_json=s_json3
       if option == 4:
           s_json=s_json4             


       sql=   "INSERT into t_transaction_payment_details "\
              "(date_created, "\
              " txn_id, "\
              " paysol_id,"\
              " paysol_txn_id,"\
              " details)"\
              "VALUES (NOW(), %s, %s, %s, %s)"

       data=(dic_txn['id'],
             dic_txn['paysol_id'],
             dic_txn['id'],
             json.dumps(s_json)
            )

       db = MySQLPool(app)
       try:
          conn = db.connection.get_connection()
          cursor = conn.cursor()
          cursor.execute(sql, data)  
          conn.commit
       except mysql.connector.Error as err:
          app.logger.error(format(sql))
          app.logger.error(data)
          raise err 
       finally:
          cursor.close()
          conn.close()



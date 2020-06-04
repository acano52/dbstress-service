import mysql.connector
from flask_mysqlpool import MySQLPool
from flask import current_app as app

def create_db_metrics():
       
       try:
         db = MySQLPool(app)
         conn = db.connection.get_connection()
         cursor = conn.cursor()
         sql="CREATE DATABASE IF NOT EXISTS sysops"
         cursor.execute(sql)
         sql="CREATE TABLE IF NOT EXISTS sysops.db_metrics_txn_0 "\
             "("\
             "  id bigint(20) NOT NULL AUTO_INCREMENT,"\
             "  date_created datetime DEFAULT NULL,"\
             "  txn_id  bigint(20) NOT NULL,"\
             "  txn_elapsed bigint(20),"\
             "  PRIMARY KEY (id),"\
             "  KEY I_DATE_CREATED (date_created),"\
             "  KEY I_TXN          (txn_id)"\
             ")"
         cursor.execute(sql)
         sql="CREATE TABLE IF NOT EXISTS sysops.db_metrics_txn_1"\
             "("\
             "  id bigint(20) NOT NULL AUTO_INCREMENT,"\
             "  date_created datetime DEFAULT NULL,"\
             "  txn_id      bigint(20) NOT NULL,"\
             "  txn_step_id smallint   NOT NULL,"\
             "  txn_elapsed bigint(20),"\
             "  PRIMARY KEY (id),"\
             "  KEY I_DATE_CREATED (date_created),"\
             "  KEY I_TXN          (txn_id),"\
             "  KEY I_STEP         (txn_step_id)"\
             ")"
         cursor.execute(sql)
         
       except mysql.connector.Error as e:
         app.logger.error(format(e.errno))
         app.logger.error(format(e.sqlstate))
         app.logger.error(format(sql))
         app.logger.error(format(e.msg))
         raise e 
       finally:
         cursor.close()
         conn.close()

       
def db_metric_0(transaction_id,start,end,metrics_level):
        
       if metrics_level == 0:
          elapsed = end - start
          millisecs=int(elapsed.total_seconds() * 1000)
          app.logger.info("db_metric_0 : %s", millisecs)

          sql=    "INSERT INTO sysops.db_metrics_txn_0 ( "\
                  "     date_created,"\
                  "     txn_id,"\
                  "     txn_elapsed"\
                  ") VALUES (NOW(),%s,%s)"

          data=(transaction_id,
                millisecs,
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
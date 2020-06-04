# Raw metrics

CREATE DATABASE IF NOT EXISTS sysops;

CREATE TABLE IF NOT EXISTS sysops.db_metrics_txn_0
(
  id bigint(20) NOT NULL AUTO_INCREMENT,
  date_created datetime DEFAULT NULL,
  txn_id  bigint(20) NOT NULL,
  txn_elapsed smallint,
  status tinyint(1) DEFAULT '0',
  PRIMARY KEY (id),
  KEY I_DATE_CREATED (date_created),
  KEY I_TXN          (txn_id)
);


CREATE TABLE IF NOT EXISTS sysops.db_metrics_txn_1
(
  id bigint(20) NOT NULL AUTO_INCREMENT,
  date_created datetime DEFAULT NULL,
  txn_id      bigint(20) NOT NULL,
  txn_step_id smallint   NOT NULL,
  txn_elapsed smallint,
  PRIMARY KEY (id),
  KEY I_DATE_CREATED (date_created),
  KEY I_TXN          (txn_id),
  KEY I_STEP         (txn_step_id)
);


# Agregations

CREATE TABLE db_metrics_txn_h
(
  id           bigint(20) NOT NULL AUTO_INCREMENT,
  date_created datetime DEFAULT NOT NULL,
  date_ini     datetime DEFAULT NOT NULL,
  date_end     datetime DEFAULT NOT NULL, 
  txn_count    int              NOT NULL,
  avg_elapsed 
  max_elapsed
  min_elapsed
)

CREATE TABLE db_metrics_txn_d
(
  id           bigint(20) NOT NULL AUTO_INCREMENT,
  date_created datetime DEFAULT NOT NULL,
  date_ini     datetime DEFAULT NOT NULL,
  date_end     datetime DEFAULT NOT NULL, 
  txn_count    int              NOT NULL,
  avg_elapsed 
  max_elapsed
  min_elapsed
)

  txn_elapsed bigint(20),
  PRIMARY KEY (id)
  KEY I_DATE_CREATED (date_created),
  KEY I_TXN          (txn_id)
  KEY I_STEP         (txn_step_id)
)

CREATE TABLE db_metrics_txn_d
(
  id bigint(20) NOT NULL AUTO_INCREMENT,
  date_created datetime DEFAULT NULL,
  txn_id      bigint(20) NOT NULL,
  txn_step_id smallint   NOT NULL,
  txn_elapsed bigint(20),
  PRIMARY KEY (id)
  KEY I_DATE_CREATED (date_created),
  KEY I_TXN          (txn_id)
  KEY I_STEP         (txn_step_id)
)

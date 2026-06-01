
-- Table mr1
CREATE EXTERNAL TABLE mr1 (
    station STRING,
    load_factor FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
LOCATION 'hdfs://namenode:8020/data-lake/processed/load_metrics/';
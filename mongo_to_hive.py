from pyspark import SparkContext,SparkConf                                                                                         
from pyspark.sql import SQLContext, SparkSession, HiveContext                                                                      
from pyspark.sql.functions import col,explode                                                                                      
                                                                                                                                   
#conf = SparkConf().set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.12:2.4.2")                                
                                                                                                                                   
my_spark = SparkSession.builder.appName('test').config('spark.mongodb.input.uri','mongodb://127.0.0.1/bigdatadb.covid19').config('spark.mongodb.output.uri','mongodb://127.0.0.1/bigdatadb.covid19').config('spark.jars.packages','org.mongodb.spark:mongo-spark-connector_2.12:2.4.2').config('spark.sql.warehouse.dir', '/root/spark-warehouse').enableHiveSupport().getOrCreate()                          
                                                                                                                                   
sqlContext = SQLContext(my_spark.sparkContext)                                                                                     
df = sqlContext.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://localhost/bigdatadb.covid19").load()       
df.printSchema()                                                                                                                   
my_spark.sql("create database if not exists bigdatadb")                                                                            
df.write.mode("overwrite").saveAsTable("bigdatadb.covid19")  
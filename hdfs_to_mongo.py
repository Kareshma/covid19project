from pyspark.sql import SparkSession


my_spark = SparkSession.builder.appName('MongoDBIntegration').config('spark.mongodb.input.uri','mongodb://sandbox-hdp.hortonworks.com/bigdatadb.covid19').config('spark.mongodb.output.uri','mongodb://sandbox-hdp.hortonworks.com/bigdatadb.covid19').config('spark.jars.packages','org.mongodb.spark:mongo-spark-connector_2.12:2.4.2').getOrCreate()


df = my_spark.read.option("multiline", "true").json("hdfs://sandbox-hdp.hortonworks.com:8020/user/root/covid19.json")              
df.count()                                                                                        
df.printSchema()                                                                                                                   
print(df.count())                                                                                                                  
df.write.format("com.mongodb.spark.sql.DefaultSource").mode("append").option("database","bigdatadb").option("collection", "covid19").save()
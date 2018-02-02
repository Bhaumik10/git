// Databricks notebook source
// scala
// Replace with your values
val AccessKey = "AKIAJK56G3FJSKECGJ2Q"
// Encode the Secret Key as that can contain "/"
val SecretKey = "KyKCtfWfawUqtp5i6SBraU40oDeGqeeDbryV0P0P".replace("/", "%2F")
val AwsBucketName = "youtilityanalytics"
val MountName = "youtilityanalytics"

dbutils.fs.mount(s"s3a://$AccessKey:$SecretKey@$AwsBucketName", s"/mnt/$MountName")
display(dbutils.fs.ls(s"/mnt/$MountName"))

// COMMAND ----------

val utility = sqlContext.read.format("csv").option("delimiter", "\t").load("/mnt/youtilityanalytics/qa/raw-tsv/2017/08/*/*/")

// COMMAND ----------

utility.take(1)

// COMMAND ----------

// MAGIC %sql drop table if exists utility

// COMMAND ----------

utility.createOrReplaceTempView("utility")

// COMMAND ----------

// MAGIC %sql cache table utility

// COMMAND ----------

// MAGIC %sql select * from utility limit 10

// COMMAND ----------

// MAGIC %sql select count(distinct _c4) from utility

// COMMAND ----------

// MAGIC %sql select count(*) from utility

// COMMAND ----------


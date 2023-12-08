from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("BigDataProcessing") \
    .getOrCreate()

# Chemin vers le dossier contenant les fichiers CSV
csv_directory = "C:/Users/briac/Documents/M2/Application of Big Data/StockEtablissement_info"

# Lire tous les fichiers CSV du dossier
df = spark.read.csv(csv_directory, header=True, sep=",", encoding="utf-8", quote='"', escape='"')

# Conversion du type de données de la colonne 'siren' en 'bigint'
df = df.withColumn("siren", col("siren").cast("bigint"))
df = df.withColumn("nic", col("nic").cast("int"))
df = df.withColumn("etablissementSiege", col("etablissementSiege") == "True")
df = df.withColumn("nombrePeriodesEtablissement", col("nombrePeriodesEtablissement").cast("int"))

# Configuration de la connexion JDBC
url = "jdbc:postgresql://localhost:5432/StockEtablissement"
properties = {
    "user": "postgres",
    "password": "@/fpayIMm8",
    "driver": "org.postgresql.Driver"
}

# Écrire le DataFrame dans PostgreSQL
df.write.jdbc(url=url, table="etablissement_info", mode="append", properties=properties)

# Fermer la session Spark
spark.stop()
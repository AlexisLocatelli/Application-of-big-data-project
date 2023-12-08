from pyspark.sql import SparkSession

spark = spark = SparkSession.builder \
                .appName("BigDataProcessing") \
                .config("spark.hadoop.home.dir", "C:\BigDataLocalSetup\Hadoop") \
                .getOrCreate()

input_file = "C:/Users/briac/Documents/M2/Application of Big Data/StockEtablissement_utf8.csv"

cols_to_keep = ["siren","nic","siret","statutDiffusionEtablissement","dateCreationEtablissement","trancheEffectifsEtablissement",
            "anneeEffectifsEtablissement","activitePrincipaleRegistreMetiersEtablissement","dateDernierTraitementEtablissement",
            "etablissementSiege","nombrePeriodesEtablissement"]

df = spark.read.csv(input_file, header=True, sep=",", encoding="utf-8", quote='"', escape='"')

df_selected = df.select(cols_to_keep)

output_file = "C:/Users/briac/Documents/M2/Application of Big Data/StockEtablissement_info.csv"

# Écrire les données dans un nouveau fichier CSV
df_selected.write.csv(output_file, mode="overwrite", header=True)

# Fermer la session Spark
spark.stop()
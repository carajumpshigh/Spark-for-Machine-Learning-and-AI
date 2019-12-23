"""
Features: distributed, processing, big data
Components: MLlib, Spark SQL, Spark Streaming, GraphX
Use cases: Real-time monitoring, text analysis, ecommerce pattern analysis, healthcare and genomic analysis

Steps: Preprocessing(collect, reformat, transform data), model building(apply algorithms to training data), validation(assess quality)
      -Preprocessing: extract, transform and load data to staging area;
                      review data for missing data and invalid values;
                      normalize and scale numeric data;
                      standardize categorical values;
      -Model building: select algorithms;
                       executing algorithms to fit data to models;
                       tuning hyperparameters
      -Validating models: apply models to additional test sets;
                          measuring quality of models(accuracy, precision, sensitivity)
Install: download package(spark,java,python)-> decompress and rename-> cd spark （ls/dir->） cd bin-> （ls/dir->） .\pyspark

"""


# Dataframe
emp_df = spark.read.csv("C:\Users\212720797\Desktop\Exercise Files\Ch01\01_04.txt",header=True)
emp_df
emp_df.schema
emp_df.printSchema()    # names and types of data
emp_df.columns    # list of columns' names
emp_df.take(5)    # first 5 rows
emp_df.count()    # number of rows
sample_df = emp_df.sample(False,0.1)      # no replacement of raw data, pick 10% of raw data
sample_df.count()
emp_mgrs_df = emp_df.filter("salary >= 100000")
emp_mgrs_df.count()
emp_mgrs_df.select("salary").show()       # top 20 salaries


# type:numeric(normalize, standardize, partitioning(continuous->buckets));
#      text(tokenizing(str->a set of tokens/words), TF-IDF(single str->vetor of texts and their frequency))

# Normalizing

from pyspark.ml.feature import MinMaxScaler
from pyspark.ml.linalg import Vectors

features_df = spark.createDataFrame([(1,Vector.dense([10.0,10000.0,1.0]),),
              (1,Vector.dense([10.0,10000.0,1.0]),),
              (1,Vector.dense([10.0,10000.0,1.0]),),
              (1,Vector.dense([10.0,10000.0,1.0]),)],["id","features"])
features_df.take(1)

#==========================================================================================================

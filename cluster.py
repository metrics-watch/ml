
import tensorflow as tf
from numpy import array
from load import training_data, error_data

tf.logging.set_verbosity(tf.logging.ERROR)

def fit(numclusters, input_fn):
  kmeans = tf.contrib.learn.KMeansClustering(
      num_clusters=numclusters, relative_tolerance=0.0001)
  return kmeans.fit(input_fn=input_fn)

def input_fn(matrix):
  return tf.constant(matrix, tf.float32), None

def input_fn_training():
  return input_fn(training_data[:5])

def input_fn_error():
  return input_fn(error_data[:1])



''' Train our model '''
print("## Training")
kmeans = fit(2, input_fn_training)

''' Display Clusters '''
print("## Clusters")
clusters = kmeans.clusters()
print(clusters)

''' Calculate miss from some error values '''
print("## Score")
score = kmeans.score(input_fn=input_fn_error)
print(score)
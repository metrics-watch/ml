
import tensorflow as tf
from load import training_data, error_data

tf.logging.set_verbosity(tf.logging.ERROR)

def fit(numclusters, input_fn):
  kmeans = tf.contrib.learn.KMeansClustering(
      num_clusters=numclusters, relative_tolerance=0.0001)
  kmeans.fit(input_fn=input_fn)
  return kmeans

def input_fn(matrix):
  return tf.constant(matrix, tf.float32), None

def input_fn_training():
  return input_fn(training_data)

def input_fn_error():
  return input_fn(error_data)



''' Train our model '''
print("## Training")
kmeans = fit(4, input_fn_training)

''' Display Clusters '''
print("## Clusters")
clusters = kmeans.clusters()
print(clusters)

''' Calculate miss from some error values '''
print("## Score")
score = kmeans.score(input_fn=input_fn_error)
print(score)
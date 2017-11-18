from sklearn.cluster import KMeans
from load import training_data, error_data, reverted_data
from decimal import Decimal



for i in range(1, 50):
  kmeans = KMeans(n_clusters=i, random_state=0).fit(training_data)
  training_score = '%.2E' % Decimal(-1*kmeans.score(training_data)/len(training_data))
  error_score = '%.2E' % Decimal(-1*kmeans.score(error_data)/len(error_data))
  reverted_score = '%.2E' % Decimal(-1*kmeans.score(reverted_data)/len(reverted_data))
  print(str(i) + " # " + training_score + " # " + error_score + " # " + reverted_score);

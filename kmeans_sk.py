from sklearn.cluster import KMeans
from load import training_data, error_data, reverted_data
from decimal import Decimal


kmeans = KMeans(n_clusters=9, random_state=0).fit(training_data)

print("Score Training")
print('%.2E' % Decimal(-1*kmeans.score(training_data)/len(training_data)))

print("Score Error")
print('%.2E' % Decimal(-1*kmeans.score(error_data)/len(error_data)))


print("Score Reverted")
print('%.2E' % Decimal(-1*kmeans.score(reverted_data)/len(reverted_data)))

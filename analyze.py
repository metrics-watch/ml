from hierarchical import calculate_cluster_distribution
from load import path_to_array
from persistance import load_model
import sys

if len(sys.argv) <= 1:
  print("ERROR: You need to specify a path to the data")
  exit(1)


model = load_model()
trained_distribution = calculate_cluster_distribution(model.labels_)

data = path_to_array(sys.argv[1])

labels = model.fit_predict(data)
current_distribution = calculate_cluster_distribution(labels)

print(trained_distribution)
print(current_distribution)

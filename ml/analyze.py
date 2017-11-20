from hierarchical import calculate_cluster_distribution
from load import path_to_array
from persistance import load_model
import sys
import locale

if len(sys.argv) <= 1:
  print("ERROR: You need to specify a path to the data")
  exit(1)

locale.setlocale(locale.LC_ALL, '')

filenames = sys.argv[1:]

model = load_model()
trained_distribution = calculate_cluster_distribution(model.labels_)

cluster_count = model.get_params()["n_clusters"]

for filename in filenames:
  #print('# ' +  filename);
  data = path_to_array(filename)

  if len(data) < cluster_count:
    print(" N/A")
    continue

  labels = model.fit_predict(data)
  current_distribution = calculate_cluster_distribution(labels)
  diff = abs(trained_distribution - current_distribution).sum()
  print(locale.format("%.4f", diff))
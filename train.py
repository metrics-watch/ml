from hierarchical import model
from load import path_to_array
from persistance import save_model
import sys

if len(sys.argv) <= 1:
  print("ERROR: You need to specify a path to the data")
  exit(1)

training_data = path_to_array(sys.argv[1])
model.fit(training_data)

save_model(model)
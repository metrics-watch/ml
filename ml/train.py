from hierarchical import model
from load import path_to_array
from persistance import save_model
import sys

if len(sys.argv) <= 1:
  print("ERROR: You need to specify a path to the data")
  exit(1)


print("# Loading Data from Files")
print(sys.argv[1:])
nested_data = list(map(lambda filename: path_to_array(filename), sys.argv[1:]) )

training_data = [item for sublist in nested_data for item in sublist]

print("# Training on " + str(len(training_data)) + " Events")

model.fit(training_data)

print("# Training finished")

save_model(model)

print("# Model saved")
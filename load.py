import json
import tensorflow as tf
import numpy as np

trainingpath = "./data/sample_pre_grid.json"
errorpath = "./data/sample_post_grid.json"

def read_data(path):
  events = []
  with open(path, 'r') as f:
    for line in iter(f.readline, ''):
      events.append(json.loads(line))
  return events

def eventToVector(event):
  return [event["status"], event["minuteofday"], event["dayofweek"], event["responsetime"]]

def pathToArray(path):
  return np.array(list(map(eventToVector, read_data(path))))

training_data = pathToArray(trainingpath)
error_data = pathToArray(errorpath)



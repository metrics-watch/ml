import json
import tensorflow as tf
import numpy as np

def read_data(path):
  events = []
  with open(path, 'r') as f:
    for line in iter(f.readline, ''):
      events.append(json.loads(line))
  return events

def event_to_vector(event):
  return [event["status"], event["responsetime"], event["minuteofday"], event["dayofweek"], event["method"], event["url"]]

def path_to_array(path):
  return np.array(list(map(event_to_vector, read_data(path))))



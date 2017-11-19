from sklearn.externals import joblib
path = "./data/current_model.pkl";

def save_model(model):
  joblib.dump(model, path) 

def load_model():
  return joblib.load(path) 
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import AgglomerativeClustering
import numpy as np


def route_distances(routes):
  equal = np.array(
    list(
      map(
        lambda route: np.core.defchararray.equal(
          routes,
          route
        ), routes
      )
    )
  ).__invert__().astype(int) * 10000
  return equal

def distance_by_route(X):
  numerical_vector = np.array(list(map(lambda event: event[:2], X)))
  route_vector = np.array(list(map(lambda event: event[4] + " " + event[5], X)))

  geometric_distance = euclidean_distances(numerical_vector)
  route_distance = route_distances(route_vector)

  absolute_distance = np.add(geometric_distance, route_distance)


  return absolute_distance

def calculate_cluster_distribution(labels):
  _, counts = np.unique(labels, return_counts=True)
  counts = np.array(counts) 
  total = counts.sum()
  relative = counts / total
  return relative

#model = AgglomerativeClustering(n_clusters=150)
model = AgglomerativeClustering(n_clusters=50,affinity=distance_by_route,linkage="complete")
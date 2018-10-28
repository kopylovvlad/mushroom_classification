from typing import List, Dict, Tuple
import clusters
import csv
import csv_helper as csv_h
import os
import argparse
import pickle
import sys
sys.setrecursionlimit(9_500)

parser = argparse.ArgumentParser()
parser.add_argument("-l", '--limit', help='Csv row limit', type=int)
arguments = parser.parse_args()

csv_row_limit: int = arguments.limit or 100  # 8120
print('csv_limit is: %d' % csv_row_limit)
dirname: str = os.path.dirname(os.path.abspath(__file__))
csvfile = open(dirname + '/mushrooms.csv', newline='')
filereader = csv.reader(csvfile, delimiter=',', quotechar='\"')

item_names, props, data = csv_h.csv_to_vector(filereader)

data = data[:csv_row_limit]
item_names = item_names[:csv_row_limit]
print('We have %d train items' % len(data))

f = open(dirname + '/tmp_data/mushrooms_data_vector1.pickle', 'wb')
pickle.dump((item_names, props, data), f)
f.close()

clust = clusters.hcluster(data, distance=clusters.tanimoto_coeff)

f = open(dirname + '/tmp_data/mushrooms_data_tuple1.pickle', 'wb')
pickle.dump((clust, item_names), f)
f.close()

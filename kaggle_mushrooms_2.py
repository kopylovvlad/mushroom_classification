from typing import List, Dict
import clusters
import os
import pickle
import sys
sys.setrecursionlimit(9_500)

dirname: str = os.path.dirname(os.path.abspath(__file__))

f = open(dirname + '/tmp_data/mushrooms_data_tuple1.pickle', 'rb')
clust, blognames = pickle.load(f)
f.close()

report: str = clusters.clust_to_string(clust, blognames)
file_object = open(dirname + '/tmp_data/mushrooms_report1.txt', 'w')
file_object.write(report)
file_object.close()

print('You can open file "' + dirname + '/tmp_data/mushrooms_report1.txt'+'"')

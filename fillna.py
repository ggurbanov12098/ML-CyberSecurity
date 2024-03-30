#!/usr/bin/env python

import os
import re
import string
import pandas as pd
import sys
from functools import reduce
# import socket
# import struct
import ipaddress

# filename = sys.argv[1]
filename = "master_dataset.csv"
# csv_file_path = os.path.join("./", filename)
file1 = pd.read_csv(filename)
file1.head(10)
file1.isnull().sum
# print(file1.isnull().sum)

# step-1 to replace all null
update_file = file1.fillna(" ")
update_file.isnull().sum()
# print (update_file.isnull().sum()) 
update_file.to_csv('fillna_'+filename, index = False)

# step-2 to remove all rows with null value
update_file = file1.fillna(0)



update_file.to_csv('fillna_'+filename, index = False)
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
filename = "ipdos.csv"
# csv_file_path = os.path.join("./", filename)
file1 = pd.read_csv(filename)
file1.head(10)
file1.isnull().sum
# print(file1.isnull().sum)

# step-1 to replace all null
update_file = file1.fillna(" ")
update_file.isnull().sum()
# print (update_file.isnull().sum()) 
update_file.to_csv('cleaned_'+filename, index = False)

# step-2 to remove all rows with null value
update_file = file1.fillna(0)
# print (update_file.isnull().sum())
# step-3 to convert tcp.flag, ip.dst, ip.src to integer
update_file['tcp.flags'] = update_file['tcp.flags'].apply(lambda x: int(str(x), 16))
# update_file['ip.dst'] = update_file['ip.dst'].apply(lambda x: int(ipaddress.IPv4Address(x))) #str(x).replace(',', '')
# update_file['ip.src'] = update_file['ip.src'].apply(lambda x: int(ipaddress.IPv4Address(x)))

# update_file['ip.dst'] = update_file['ip.dst'].apply(lambda x: int(ipaddress.IPv4Address(x.split(",")[0].strip())))
# update_file['ip.src'] = update_file['ip.src'].apply(lambda x: int(ipaddress.IPv4Address(x.split(",")[0].strip())))

update_file['ip.dst'] = update_file['ip.dst'].apply(lambda x: int(ipaddress.IPv4Address(x.split(",")[0].strip())) if isinstance(x, str) else x)
update_file['ip.src'] = update_file['ip.src'].apply(lambda x: int(ipaddress.IPv4Address(x.split(",")[0].strip())) if isinstance(x, str) else x)


update_file['ip.len'] = update_file['ip.len'].apply(lambda x: int(x.split(",")[0].strip() if isinstance(x, str) else x))
update_file['ip.ttl'] = update_file['ip.ttl'].apply(lambda x: int(x.split(",")[0].strip() if isinstance(x, str) else x))





# print(update_file['udp.port'])
# update_file['udp.port'] = update_file['udp.port'].apply(lambda x: int(x isinstance str: str(x, 36)))    
update_file['udp.port'] = update_file['udp.port'].apply(lambda x: int(str(x).replace(',', '')))

# Convert 'Not set' to 0 and 'Set' to 1 in 'ip.flags.df' and 'ip.flags.mf'
update_file['ip.flags.df'] = update_file['ip.flags.df'].apply(lambda x: 0 if x == 'Not set' else 1)
update_file['ip.flags.mf'] = update_file['ip.flags.mf'].apply(lambda x: 0 if x == 'Not set' else 1)

# Convert 'TCP' to 6 and 'UDP' to 17 in 'ip.proto' column
# update_file['ip.proto'] = update_file['ip.proto'].apply(lambda x: smthn for ICMP,UDP) #ipdos=66777

# update_file['ip.proto'] = update_file['ip.proto'].apply(lambda x: 6 if x == 'TCP' else (17 if x == 'UDP' else x))
update_file['ip.proto'] = update_file['ip.proto'].apply(lambda x: 6 if x == 'TCP' else (17 if x == 'UDP' else 999))

# update_file['ip.proto'] = update_file['ip.proto'].apply(lambda x: 6 if 'TCP' in x.split(',') else (17 if 'UDP' in x.split(',') else x))
# update_file['ip.proto'] = update_file['ip.proto'].apply(lambda x: 6 if 'TCP' in x.split(',') else (17 if 'UDP' in x.split(',') else (999 if x != '' else x)))




# update_file['ip.fragment'] = update_file['ip.fragment'].apply(lambda x: )
update_file['ip.fragment'] = update_file['ip.fragment'].apply(lambda x: int(x.replace(',', '')) if isinstance(x, str) else x)
update_file['ip.fragments'] = update_file['ip.fragments'].apply(lambda x: 999 if isinstance(x, str) else x)




# Function to replace non-ASCII characters with a specific number
def replace_special_character(text, replacement_number):
    if isinstance(text, str):
        return text.replace('�', str(replacement_number))
    else:
        return text

# Replace special characters in columns containing unexpected strings
update_file['tcp.segments'] = update_file['tcp.segments'].apply(lambda x: replace_special_character(x, 9999))
# update_file['http.request'] = update_file['http.request'].apply(lambda x: replace_special_character(x, 9999))

# Convert columns to numeric after replacing special characters
update_file['tcp.segments'] = pd.to_numeric(update_file['tcp.segments'], errors='coerce')
# update_file['http.request'] = pd.to_numeric(update_file['http.request'], errors='coerce')


# Convert True/False to int
update_file['http.request'] = update_file['http.request'].astype(int)

update_file = update_file.fillna(0)
update_file.to_csv('cleaned_'+filename, index = False)
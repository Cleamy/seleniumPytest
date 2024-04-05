import csv
import json

import yaml

def read_file(filepath):
    rel = []
    with open(filepath,mode='r',encoding='utf-8') as f:
        datas = yaml.load(stream=f,Loader=yaml.FullLoader)
        for data in datas:
            rel.append(data)
    return rel

def read_json(filepath):
    rel = []
    with open(filepath,mode='r',encoding='utf-8') as f:
        dict_data = json.load(f)
        for data in dict_data:
            rel.append(data)
    return rel

def read_csv(filepath):
    rel = []
    with open(filepath,mode='r',encoding='utf-8')as f:
        datas = csv.reader(f)
        for data in datas:
            rel.append(data)
    return rel

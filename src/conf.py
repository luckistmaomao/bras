#coding:utf-8

import yaml

with open('bras.yaml') as conf_file:
    conf_dic = yaml.load(conf_file, Loader=yaml.BaseLoader)

user = conf_dic['user'][0]
USERNAME = user['username']
PASSWORD = user['password']


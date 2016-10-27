# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:49:18 2015

@author: Jorge
"""

#TODO
#The flow is working, but the results are only shown on screen.
#need to save to db or text and inject to solr

import os
import tika
from tika import parser

#configurations
source = './originals/'
destination = './text/'
tika_server = 'http://localhost:9998/tika'

#cleaning filename, remove spaces
def rem_space(filename):
    return '_'.join(filename.split())

#obtain list of files to process
file_list = os.listdir(source)

#text extraction function
def textExtract(filename):
    parsed = parser.from_file(source+filename, tika_server)
    metadata = (parsed["metadata"])
    # author = (parsed["metadata"]["Author"])
    # title = (parsed["metadata"]["title"])
    # contentType = (parsed["metadata"]["Content-Type"])
    content = (parsed["content"])
    return parsed

def iterdir():
    for i in range(len(file_list)):
        try:
            newDoc = textExtract(file_list[i])
            #print (newDoc["metadata"])  #works to call just metadata
            #print (newDoc["content"])  #works to call just content in pretty print
            print (newDoc)              # to call everythin on the parsed doc in json format
            # textExtract(file_list[i])
            # print ('done ' + file_list[i])
        except:
            print ("Error " + file_list[i])
    print(' ......All done ...')


#run-it       
iterdir()
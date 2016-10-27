# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:49:18 2015

@author: Jorge
"""

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
    return metadata

def iterdir():
    for i in range(len(file_list)):
        try:
            newDoc = textExtract(file_list[i])
            print (newDoc)
            # textExtract(file_list[i])
            # print ('done ' + file_list[i])
        except:
            print ("Error " + file_list[i])
    print(' ......All done ...')


#run-it       
iterdir()
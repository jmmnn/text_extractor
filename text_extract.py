# -*- coding: utf-8 -*-
"""
Converts rich files to json using Apache Tika. Instructions:
1) Modify the configurations to suit your folder structure
2) Run $ python text_extract.py
"""

import os
import tika
from tika import parser

###### configurations
tika_server = 'http://localhost:9998/tika'
original_files = './original_files/'
json_files = './json_files/'
######

#text extraction function
def textExtract(filename):
    parsed = parser.from_file(filename, tika_server)
    metadata = (parsed["metadata"])
    content = (parsed["content"])
    # author = (parsed["metadata"]["Author"])
    # title = (parsed["metadata"]["title"])
    # contentType = (parsed["metadata"]["Content-Type"])
    return parsed

# Write to file function
def writteToFile(filename, extension, content):
    '''example: writteToFile('helloWorld' , '.txt' , 'Hello World')
    '''
    with open(filename + extension, 'w') as f:
        f.write(content)

#Directory iteration function
def iterdir(source , destination, function):
    '''
    This function takes a "source" directory a "destination" directory and
    a "function" which will be applied to all the files in the source directory.
    example: iterdir(source , destination, textExtract)
    '''
    file_list = os.listdir(source) #obtain list of files to process
    for i in range(len(file_list)):
        try:
            newDoc = function(source+file_list[i]) #this function is executed on each file
            #Change the extension for the output file e.g. .json, .txt, .csv
            writteToFile(destination + file_list[i], '.json', str(newDoc))
            print ('success processing file : ' + file_list[i])
        except:
            print ("Error " + file_list[i])
    print(' ......All done ...')

#tests:
#writteToFile('hola.txt', 'welcome!')
#print textExtract('tika_tutorial.pdf')["metadata"]

#run-it       
iterdir(original_files , json_files, textExtract) #this will initiate the iteration

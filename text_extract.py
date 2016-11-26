# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:49:18 2015

@author: Jorge
"""

#TODO

import os
import tika
from tika import parser

#configurations
tika_server = 'http://localhost:9998/tika'
original_files = './original_files/'
json_files = './json_files/'
renamed_files = './renamed_files'


#cleaning filename, remove spaces
def rem_space(filename):
    return '_'.join(filename.split())

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
iterdir(original_files , json_files, textExtract) #this will extract text from files
#iterdir(original_files , renamed_files, rem_space) #this will extract text from files

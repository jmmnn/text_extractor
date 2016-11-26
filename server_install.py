#!/usr/bin/env python

'''
Setting up your new Ubuntu server
'''
import subprocess
import sys
import os

#List commands to execute.

#Server setup
UPDATE ="sudo apt-get update"
GIT = "sudo apt-get install git"
PIP = "sudo apt-get install python-pip"
JAVA = "sudo apt-get install default-jre"
CLONE_REPO = "git clone https://github.com/jmmnn/text_extractor.git"

#######  Python stuff
TIKA = "sudo pip install -U tika"

#FIRST list of commands in sequence ## Uncomment these for 1st install
cmds = [
    UPDATE,
    GIT,
    PIP,
    JAVA,
    TIKA,
    CLONE_REPO
    ]

dir = os.getcwd()


###### Iterates over the FIRST list of commands
count=0
for cmd in cmds:
    count+=1
    print ("____Running Command Number : ",count , " $" , cmd)
    subprocess.call(cmd, shell=True)
    print ("____Finished Running Command: $" , cmd)
# text_extractor

This script takes rich files from a folder e.g. word, pdf, etc. and extracts the text from them using Apache Tika.

The resulting text is saved as .json files for each original file.

Instructions
-------------

1 - Obtain a new Ubuntu server [e.g. c9.io (free), VirtualBox, AWS, Godaddy cloud, etc.]  
2 - Copy the installer script to the server:  
`$ wget https://raw.githubusercontent.com/jmmnn/text_extractor/master/server_install.py`
3 - Run the istaller, click yes when necessary:  
`$ python server_install.py`  
At this point you have what you need.


If you want to test it:  
4 - Change directory to text_extractor:  
`$ cd text_extractor`  
5 - Then run:  
`$ python text_extract.py`  


To run, just place your files in the "original_files" folder and run the command above again.

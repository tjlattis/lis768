#! /usr/local/bin/python3
# tesser.py | a script which feeds all files in a given directory to tesseract
# depends: Pillow, PyTesser3
# Useage: ./pytesser.py [target directory] [output name]
import os, sys
from datetime import datetime
from PIL import Image
from pytesser3 import *

help_string = "tesser.py -- ocr a directory of jpgs with tesseract!\nUseage: ./tesser.py [target directory] [output name]"

# check for invalid or help options
if len(sys.argv) > 3:
    print("invalid options")
    print(help_string)
    quit()

if sys.argv[1] == "-h" or sys.argv[1] == "help":
    print(help_string)
    quit()

# some variables
page_itr = 1
start_time = datetime.now()
target_dir = './'   #default
out_file_name = "ocr_out.txt" #default

# lint for specified target dir and output name, then assign
if len(sys.argv) >= 2:
    if sys.argv[1].endswith('/'):
        target_dir = sys.argv[1] 
    else:
        target_dir = sys.argv[1] + '/'

if len(sys.argv) == 3:
    out_file_name = sys.argv[2]

# create output file
out_file = open(out_file_name, 'w')

# loop over target dir
for filename in sorted(os.listdir(target_dir)):
    
    # skip other file types
    if filename.endswith(".jpg"): 

        image_file = target_dir + filename
        file_time = datetime.now()
        
        # these lines from Manejando datos
        im = Image.open(image_file)
        text = image_to_string(im)
        text = image_file_to_string(image_file)
        text = image_file_to_string(image_file, graceful_errors=True)
        text = text.strip()

        # state enum and source file then concat ocr text to output file
        out_file.write("\n\n== page %s -- source file: %s ==\n\n" %(page_itr, filename))
        out_file.write(text)
        page_itr += 1

        # report elapsed time
        print("ocr complete on %s -- time elapsed: %s " %(filename, (datetime.now() - file_time)))
        continue
    
    else:
        continue

# close the output file
out_file.close()
print("ocr job finished! %s files ingested" %(page_itr))
print("total time elapsed: %s" %(datetime.now() - start_time)) 


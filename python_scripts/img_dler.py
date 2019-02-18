#!/usr/bin/env python

# Script Name: img_dler.py 
# Creation Date: 01/13/2019 
# Description: Script downloads image from supplied image url and randomly assigned a name 
# Author: Mr. Machine
# Tags: utility, image, python,  

# Library Imports
import random
import requests
import time

get = str(input("Enter URL of image to download: "))

def download_img(url):
    print("Downloading image...")
    time.sleep(1)
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    r = requests.get(url, stream=True)
    # save image file as a binary
    with open(full_name, 'wb') as f:
        f.write(r.content)
    return "Download complete. Saved image as: " + full_name

print(download_img(get))

#!/usr/bin/evn python

###########################################################################
# Script Name: md2pdf.py
# Create Date: 11/18/2018
# Description: python script to convert markdown files to pdf files using user inputs of filenames
# Author: Mr. Machine
# Tags: python, md, pdf, productivity
########################################################################### 

# Library imports
import markdown
import pdfkit

input_filename = 'todolist.md'
output_filename ='todolist.pdf'

with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

pdfkit.from_string(html_text, output_filename)

#!/usr/bin/env python

###########################################################################
# Script Name: webscraper.py
# Create Date: 12/05/2018
# Description: The purpose of this file is to enter a website url and perform a
# simple scrape of the webpage's content and parse through the text objects using
# regular expressions.
# Author: Mr. Machine
# Tags: python, utility, web, url 
# Resources: https://towardsdatascience.com/web-scraping-regular-expressions-and-data-visualization-doing-it-all-in-python-37a1aade7924
########################################################################### 

# Library imports
import requests
import re
from bs4 import BeautifulSoup

# Define the desired URL to scrape
# url = http://www.cleveland.com/metro/index.ssf/2017/12/case_western_reserve_university_president_barbara_snyders_base_salary_and_bonus_pay_tops_among_private_colleges_in_ohio.html # Example web URL for scraping demo
web_url = input("Enter the complete URL to scrape: ")

print("You entered " + web_url)
confirm = input("Is this entry correct? (Y/n)")

if confirm == Y or y:
	pass
else:
	break


# Make the GET request to the defined URL of website
# r = requests.get(url) # Example GET request for demo
r = requests.get(web_url)

# Extract the content
c = r.content

# Create soup object
soup = BeautifulSoup(c)

# Find the desired element on the webpage
# main_content = soup.find('div', attrs = {'class': 'entry-content'}) #Example entries for main content html tag
main_content = soup.find()

# Extract the relevant content as text
# content = main_content.find('ul').text # Example html 'ul' tag to search unordered lists within main content
content = main_content.find().text

# Create a pattern to match names
name_pattern = re.compile(r'^([A-Z]{1}.+?)(?:,)', flags = re.M)

# Find all occurrences of the pattern
names = name_pattern.findall(content)

# FMake school pattern nd extract schools
school_pattern = re.compile(r'(?:,|,\s)([A-Z]{1}.*?)(?:\s\(|:|,)')
schools = school_pattern.findall(content)

# Pattern to match the salaries
salary_pattern = re.compile(r'\$.+')
salaries = salary_pattern.findall(content)

# Convert salaries to numbers in a list comprehension
[int(''.join(s[1:].split(','))) for s in salaries]

















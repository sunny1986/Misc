########################################################################################
# Description: 
# This program checks for profanity in a given file
# 
# Steps:
# 1. Define a function that reads a file using Python's standard library open function
# 2. Define another function that checks for profanity by passing contents of the read 
#    file as a query to a website that provides results after checking profanity on the 
#    query passed
#
#
#
#
########################################################################################
import urllib

#1
def read_text():
    # open the file to check for profanity
    text = open("---- FILE LOCATION HERE ----")
    # read the contents of the files
    contents_of_file = text.read() 
    # close the file
    text.close()
    # return the contents read from the file to the calling function
    return contents_of_file

#2
def check_profanity():
    # get contents of the file
    QUERY = read_text()
    # open the website and pass the contents as a query to the website
    results = urllib.urlopen("http://www.wdylike.appspot.com/?q="+QUERY)
    # read the results obtained from the website
    output = results.read()    
    # print profanity check results
    if output == "true":
        print "Profanity check failed!"
    elif output == "false":
        print "Profanity check passed"
    else:
        print "Invalid data to check for profanity"

check_profanity()

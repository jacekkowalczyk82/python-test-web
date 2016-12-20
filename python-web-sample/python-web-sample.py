#!/usr/bin/env python

'''
Created on Apr 10, 2013

@author: kowalczy
'''
import web

import urllib
import httplib
import exceptions
import os
import datetime


#import properties_status_emails
#import properties_webservices

KEEP_DATA_FILE_PATH = '/home/jacek/data-to-keep.conf'


# apt-get install python-setuptools
# sudo easy_install web.py

urls = (
    '/hello/(.*)', 'hello',
    '/data/(.*)', 'KeptData',
    '/success/(.*)/(.*)', 'Success',
    '/datakeep/(.*)', 'KeepData',
    '/.*' , 'index'
)

usage = "Example usage : \n" + "http://server:port/data/ \n"

default_user = 'jacek'
default_pass = 'hasL0'

HOUR_SECONDS = 3600
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

        

class index:
    def GET(self):
       return "\n" + generateHelp()

class hello:
    def GET(self, name):
       
       if name == '':
          
           return "Hello unknown"
       else:
           return "Hello " + name

def readFile(path):
    content = []
    try:
        configFile = open(path, 'r')
        for line in configFile:
            content.append(line)
    except exceptions.IOError, ioe:
        content.append("Failed to read config file. Please contact Administrator. IOError" + str(ioe))
        return content

    #content = configFile.read();
    return content

def writeToFile(path,contentToAppend):
    print ('writing to file ',path)
    try:
        with open(path, "a") as configFile:
            configFile.write("\n")
            configFile.write(contentToAppend)
            configFile.write("\n")
    except exceptions.IOError, ioe:
        return "Failed to write config file. Please contact Administrator. IOError" + str(ioe);

    return readFile(path)



class KeepData (object):
    # example
    # curl -S -X POST http://computer-syrena:1234/reportunstability/category/FAIL%20description%20timed%20out%20-
        
    def POST(self, data ):
        post_data=web.input(name=[])
        print ('post data',post_data)
        record_id = post_data['record_id']
        print (record_id)
        content = writeToFile (KEEP_DATA_FILE_PATH,record_id)
        return generateListPage();
        
    
 
        
class KeptData(object):
    data =''
    
    def __init__(self):
        
        self.data = "";

    def GET(self, param):
        content = readFile(KEEP_DATA_FILE_PATH)
        return render_html(content);
    
        
def parseDate(stringTime):
    
    dt= datetime.datetime.strptime(stringTime, DATE_FORMAT)
    #print "parsed date:"
    #print dt;
    return dt;
 
   
def render_html(content):
    today = datetime.datetime.now()
    action_url =  'http://localhost:1237/datakeep/'   
    html_code = """<html>\n
<head>\n
<title>Keep data</title>\n

</head>\n
<body  bgcolor=\"#ffffff\">\n
<h1>Keep data</h1>\n
<p>List of record to keep</p>\n
<p>\n"""

    for line in content:
        html_code =html_code +line +"<br/>" 
    
    html_code =html_code +"""</p>\n
<form name=\"update_record\" action=\""""+action_url+"""\" method=\"POST\"> \n
<input type=\"text\" name=\"record_id\" value=\"put here record_id\"/> \n
<input type=\"submit\" value=\"Submit\"/></form> \n
<p>"""+str(today.strftime(DATE_FORMAT))+"""</p>\n
</body></html>"""
    
    return html_code;  
   
def generateListPage():
    action_url =  'http://localhost:1237/data/'   
    html_code = """<html>\n
<head>\n 
<title>Keep data</title>\n 
</head>\n 
<body  bgcolor=\"#ffffff\">\n 
<h1>\n 
Keep datas\n 
</h1>\n 
<p><a href=\""""+action_url+"""\">Go back to the list of records</a></p>

</body></html>"""

    return html_code;

def generateHelp():
    html_code = """<html>\n
<head>\n 
<title>Keep data</title>\n 
</head>\n 
<body  bgcolor=\"#ffffff\">\n 
<h1>\n 
Keep data\n 
</h1>\n 
<p>Examples of usage:</p>
<ul>
<li>http://server:port/hello/ </li>\n
<li>http://server:port/ </li>\n
<li>http://server:port/data/ </li>\n
<li>http://server:port/datakeep/ </li>\n
</ul>
</body></html>"""

    return html_code;

   
if __name__ == "__main__":
      app = web.application(urls, globals())
      app.run()



    

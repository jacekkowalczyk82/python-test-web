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

KEEP_CLOUDSTACKS_FILE_PATH = '/coredb/httpshare/pipeline-artifacts/do-not-delete-these-aws-stacks.conf'


# apt-get install python-setuptools
# sudo easy_install web.py

urls = (
    '/hello/(.*)', 'hello',
    '/cloudstacks/(.*)', 'KeppedCloudstacks',
    '/success/(.*)/(.*)', 'Success',
    '/cloudstackskeep/(.*)', 'KeepThisCloudstack',
    '/.*' , 'index'
)

usage = "Example usage : \n" + "http://server:port/cloudstacks/ \n"

default_user = 'coredb'
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
        content.append("Failed to read config file. Please contact Coredb Support Team. IOError" + str(ioe))
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
        return "Failed to write config file. Please contact Coredb Support Team. IOError" + str(ioe);

    return readFile(path)



class KeepThisCloudstack (object):
    # example
    # curl -S -X POST http://pl1lxd-014501:1234/reportunstability/Coredb-test-branch-with-FAT-category/FAT%20tests%20timed%20out%20-
        
    def POST(self, data ):
        post_data=web.input(name=[])
        print ('post data',post_data)
        stack_id = post_data['stack_id']
        print (stack_id)
        content = writeToFile (KEEP_CLOUDSTACKS_FILE_PATH,stack_id)
        return generateListPage();
        
    
 
        
class KeppedCloudstacks(object):
    cloudstacks =''
    
    def __init__(self):
        
        self.cloudstacks = "";

    def GET(self, param):
        content = readFile(KEEP_CLOUDSTACKS_FILE_PATH)
        return render_html(content);
    
        
def parseDate(stringTime):
    
    dt= datetime.datetime.strptime(stringTime, DATE_FORMAT)
    #print "parsed date:"
    #print dt;
    return dt;
 
   
def render_html(content):
    today = datetime.datetime.now()
    action_url =  'http://localhost:1237/cloudstackskeep/'   
    html_code = """<html>\n
<head>\n
<title>Keep These Amazon Cloudstacks</title>\n

</head>\n
<body  bgcolor=\"#ffffff\">\n
<h1>Keep These Amazon Cloudstacks</h1>\n
<p>List of cloudstacks that will not be deleted automaticaly:</p>\n
<p>\n"""

    for line in content:
        html_code =html_code +line +"<br/>" 
    
    html_code =html_code +"""</p>\n
<form name=\"update_record\" action=\""""+action_url+"""\" method=\"POST\"> \n
<input type=\"text\" name=\"stack_id\" value=\"put here stack id\"/> \n
<input type=\"submit\" value=\"Submit\"/></form> \n
<p>"""+str(today.strftime(DATE_FORMAT))+"""</p>\n
</body></html>"""
    
    return html_code;  
   
def generateListPage():
    action_url =  'http://localhost:1237/cloudstacks/'   
    html_code = """<html>\n
<head>\n 
<title>Keep These Amazon Cloudstacks</title>\n 
</head>\n 
<body  bgcolor=\"#ffffff\">\n 
<h1>\n 
Keep These Amazon Cloudstacks\n 
</h1>\n 
<p><a href=\""""+action_url+"""\">Go back to the list of cloud stacks</a></p>

</body></html>"""

    return html_code;

def generateHelp():
    html_code = """<html>\n
<head>\n 
<title>Keep These Amazon Cloudstacks</title>\n 
</head>\n 
<body  bgcolor=\"#ffffff\">\n 
<h1>\n 
Keep These Amazon Cloudstacks\n 
</h1>\n 
<p>Examples of usage:</p>
<ul>
<li>http://server:port/hello/ </li>\n
<li>http://server:port/ </li>\n
<li>http://server:port/cloudstacks/ </li>\n
<li>http://server:port/cloudstacks/keep/ </li>\n
</ul>
</body></html>"""

    return html_code;

   
if __name__ == "__main__":
      app = web.application(urls, globals())
      app.run()



    

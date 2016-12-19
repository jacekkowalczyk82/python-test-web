#!/usr/bin/env python
import os
import sys

url = 'https://jira.tomtomgroup.com';


resource = Resource(url + 'rest/api/2/search?jql=assignee=kowalczy%20AND%20%28project=ATF%20OR%20project=NAVAPP%29&fields=id,key,self,summary', pool_instance=None, filters=[auth])
response = resource.get(headers = {'Content-Type' : 'application/json'})
print (response)
    if response.status_int == 200:
        # Not all resources will return 200 on success. There are other success status codes. Like 204. We've read
        # the documentation though and know what to expect here.
        issue = json.loads(response.body_string())
		
        return issue
		
		
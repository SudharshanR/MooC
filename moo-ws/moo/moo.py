"""
6, Apr 2013

Example bottle (python) RESTful web service.

This example provides a basic setup of a RESTful service

Notes
1. example should perform better content negotiation. A solution is
   to use minerender (https://github.com/martinblech/mimerender)
"""

import time
import sys
import socket
import json
import bottle

#Sud starts
from bottle import route, run
from bottle import get, post, request
import json
from json import loads
#Sud ends

# bottle framework
from bottle import request, response, route, run, template, abort

#pymongo drivers
from pymongo import Connection

# moo
from classroom import Room
connection = Connection('localhost', 27017)
db = connection.mydatabase


# virtual classroom implementation
room = None

def setup(base,conf_fn):
   print '\n**** service initialization ****\n'
   global room 
   room = Room(base,conf_fn)

#
# setup the configuration for our service
@route('/')
def root():
   print "--> root"
   return 'welcome'
#
#
@route('/moo/ping/', method='PUT')
def put_document():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if not entity.has_key('_id'):
        abort(400, 'No _id specified')
    try:
        db['documents'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))

@route('/documents', method='PUT')
def put_document():
    connection = Connection('localhost', 27017)
    db = connection.mydatabase
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if not entity.has_key('_id'):
        abort(400, 'No _id specified')
    try:
        db['documents'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))
     
@route('/documents/:id', method='GET')
def get_document(id):
    entity = db['documents'].find_one({'_id':id})
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity

#
# Development only: echo the configuration of the virtual classroom.
#
# Testing using curl:
# curl -i -H "Accept: application/json" http://localhost:8080/moo/conf
#
# WARN: This method should be disabled or password protected - dev only!
#
@route('/moo/conf', method='GET')
def conf():
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   return room.dump_conf(fmt)

#
# example of a RESTful method. This example is very basic, it does not 
# support much in the way of content negotiation.
#
@route('/moo/echo/:msg')
def echo(msg):
   fmt = __format(request)
   response.content_type = __response_format(fmt)
   if fmt == Room.html:
      return '<h1>%s</h1>' % msg
   elif fmt == Room.json:
      rsp = {}
      rsp["msg"] = msg
      return json.dumps(all)
   else:
      return msg


#
# example of a RESTful query
#
@route('/moo/data/:name', method='GET')
def find(name):
   print '---> moo.find:',name
   return room.find(name)

#
# example adding data using forms
#
@route('/moo/data', method='POST')
def add():
   print '---> moo.add'

   # example list form values
   for k,v in request.forms.allitems():
      print "form:",k,"=",v

   name = request.forms.get('name')
   value = request.forms.get('value')
   return room.add(name,value)

#Sud starts	
@route('/Ownedupdate', method=['GET','POST'])
def updateOwned():
	data = request.body.readline()
	#print(email);
	print("in new moo of update OWNED ::::::::::::::")
	
	print(type(data));
	
	j = json.loads(data)
	ownedCourse = j['ownedCourse']
	email= j['useremail']
	print(email);
	#Sud starts
	#user = j['email']
	#pwd = j['password']
	return(room.updateOwned(email,ownedCourse))
	

@route('/updateQuiz/:email', method=['GET','POST'])
def updateQuiz(email):
	ownedQuiz = request.body.readline()
	print(email);
	print("in new moo of update ENrolled ::::::::::::::")
	
	#print(type(dataReceived));
	
	#j = json.loads(dataReceived)
	#ownedQuiz = j['ownedQuiz']
	

	#Sud starts
	#user = j['email']
	#pwd = j['password']
	return(room.updateQuiz(email,ownedQuiz))

	
@route('/checkLogin', method=['GET','POST'])
def checkLogin():
	dataReceived = request.body.readlines()
	
	print(type(dataReceived));
	
	j = json.loads(dataReceived[0])
	res = j['firstName']
	
	
	str_content = res.decode('utf-8')
	return(res);

@route('/user', method=['GET','POST'])
def createUser():
	dataReceived = request.body.readline()
	print("in new moo of create user::::::::::::::")
	print(type(dataReceived));
	
	userJson = json.loads(dataReceived)

	#Sud starts
	#user = j['email']
	#pwd = j['password']
	return(room.userAdd(userJson))
	#Sud ends
	#res = j['email']
	#str_content = res.decode('utf-8')
	
	# Store the user details in the db
	# If successufll return boolean true
	'''res={"result":"success"}
	data=json.dumps(res)
	
	return(res);'''
@route('/updateUser/:email', method=['GET','POST'])

def updateUser(email):
	dataReceived = request.body.readline()
	print("in new moo of User Update ::::::::::::::")
	print(type(dataReceived));
	
	userJson = json.loads(dataReceived)

	#Sud starts
	#user = j['email']
	#pwd = j['password']
	return(room.updateUser(userJson,email))
	#Sud ends
	#res = j['email']
	#str_content = res.decode('utf-8')
	
	# Store the user details in the db
	# If successufll return boolean true
	'''res={"result":"success"}
	data=json.dumps(res)
	
	return(res);'''

@route('/user/:email', method=['GET','POST'])
def getUser(email):
	#dataReceived = request.get(email)
	print("in new get moo of getUser ::::::::::::::")
	print("---> %s" % email);
	
	#userJson = json.loads(dataReceived)

	#Sud starts
	#user = j['email']
	#pwd = j['password']
	return(room.getUser(email))
	#Sud ends
	#res = j['email']
	#str_content = res.decode('utf-8')
	
	# Store the user details in the db
	# If successufll return boolean true
	'''res={"result":"success"}
	data=json.dumps(res)
	
	'''
	return(email);

@route('/course', method=['GET','POST'])
def createCourse():
	dataReceived = request.body.readline()
	courseJson = json.loads(dataReceived)
	return(room.courseAdd(courseJson))


@route('/course/list', method=['GET'])
def courselist():
	print("Called moo.listallCourses 1 ::::");
	a=room.courselist()
	res={"result":a}
	data=json.dumps(res)
	
	return(res);

@route('/course/:cid', method=['GET'])
def getCourse(cid):	
	return(room.getCourse(cid))

@route('/course/update/:cid', method=['GET','POST'])
def updateCourse(cid):
	print("In update course moooooo:::::::::::::::");
	dataReceived = request.body.readline()	
	courseJson = json.loads(dataReceived)
	
	return(room.updateCourse(courseJson,cid))


@route('/category/list', method=['GET'])
def listCategory():
	print("in new moo ::::::::::::::")
	a=room.listCategory()
	res={"result":a}
	data=json.dumps(res)
	
	return(res);


@route('/user/auth', method=['GET'])
def checkLogin():
	dataReceived = request.body.readlines()
	
	print(type(dataReceived));
	
	j = json.loads(dataReceived[0])

	return(room.checkLogin(j))	
	
@route('/category', method=['POST'])
def createCatagory():
	dataReceived = request.body.readline()
	print("in new moo ::::::::::::::")
	print(type(dataReceived));
	
	userJson = json.loads(dataReceived)

	return(room.createCatagory(userJson))

@route('/category/:cid', method=['GET'])
def getCategory(cid):
	print("in new get moo ::::::::::::::")
	print("---> %s" % cid);
	
	return(room.getCategory(cid))
	'''res={"result":"success"}
	data=json.dumps(res)
	
	'''



@route('/course/listenrolled/:email', method=['GET'])
def enrolledCourselist(email):
	a=room.enrolledCourselist(email)
	res={"result":a}
	data=json.dumps(res)
	
	return(res);

@route('/course/listowned/:email', method=['GET'])
def ownedCourselist(email):
	a=room.ownedCourselist(email)
	res={"result":a}
	data=json.dumps(res)
	
	return(res);	

@route('/coursedelete/:cid', method=['GET','POST'])
def deleteCourse(cid):
	dataReceived = request.body.readline()	
	courseJson = json.loads(dataReceived)
	return(room.deleteCourse(courseJson,cid))	

@route('/deleteOwnedCourse/:cid', method=['GET','POST'])
def deleteOwnedCourse(cid):
	dataReceived = request.body.readline()	
	courseJson = json.loads(dataReceived)
	return(room.deleteOwnedCourse(courseJson,cid))	

@route('/deleteEnrolledCourse/:cid', method=['GET','POST'])
def deleteEnrolledCourse(cid):
	dataReceived = request.body.readline()	
	courseJson = json.loads(dataReceived)
	return(room.deleteEnrolledCourse(courseJson,cid))

@route('/course/enroll', method=['GET','POST'])
def updateEnrolled():

	enrolledCourseData = json.loads(request.body.readline())
	return(room.updateEnrolled(enrolledCourseData));

@route('/course/drop', method=['GET','POST'])
def dropEnrolled():

	dropCourseData = json.loads(request.body.readline())
	return(room.dropEnrolled(dropCourseData));	
@route('/announcement/:cid', method=['GET'])
def getann(cid):
        return(room.getann(cid))

@route('/announcementcollection', method=['GET','POST'])
def createannouncementcollection():
       dataReceived = request.body.readline()
       print("in new moo ::::::::::::::")
       print(type(dataReceived));
       
       userJson = json.loads(dataReceived)

       #Sud starts
       #user = j['email']
       #pwd = j['password']
       return(room.announcementcollectionAdd(userJson))

@route('/announcement/list', method=['GET'])
def createannouncementlist():
       print("in new moo ::::::::::::::")

       print "inside mooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
       a=room.createannouncementlist()
       res={"result":a}
       data=json.dumps(res)
       
       return(res);

@route('/discussioncollection', method=['GET','POST'])
def creatediscussioncollection():
	dataReceived = request.body.readline()
	print("in new moo ::::::::::::::")
	print(type(dataReceived));
	
	userJson = json.loads(dataReceived)

	#Sud starts
	#user = j['email']
	#pwd = j['password']
	return(room.discussioncollectionAdd(userJson))
	#Sud ends
	#res = j['email']
	#str_content = res.decode('utf-8')
	
	# Store the user details in the db
	# If successufll return boolean true
	'''res={"result":"success"}
	data=json.dumps(res)
	
	return(res);'''

@route('/discussion/:cid', method=['GET'])
def getdis(cid):	
	return(room.getdis(cid))

@route('/discussion/list', method=['GET'])
def creatediscussionlist():
	print("in new moo ::::::::::::::")

	print "inside mooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
	a=room.creatediscussionlist()
	res={"result":a}
	data=json.dumps(res)
	
	return(res);

#Sud ends

#
# Determine the format to return data (does not support images)
#
# TODO method for Accept-Charset, Accept-Language, Accept-Encoding, 
# Accept-Datetime, etc should also exist
#
def __format(request):
   #for key in sorted(request.headers.iterkeys()):
   #   print "%s=%s" % (key, request.headers[key])

   types = request.headers.get("Accept",'')
   subtypes = types.split(",")
   for st in subtypes:
      sst = st.split(';')
      if sst[0] == "text/html":
         return Room.html
      elif sst[0] == "text/plain":
         return Room.text
      elif sst[0] == "application/json":
         return Room.json
      elif sst[0] == "*/*":
         return Room.json

      # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc

   # default
   return Room.html

#
# The content type on the reply
#
def __response_format(reqfmt):
      if reqfmt == Room.html:
         return "text/html"
      elif reqfmt == Room.text:
         return "text/plain"
      elif reqfmt == Room.json:
         return "application/json"
      else:
         return "*/*"
         
      # TODO
      # xml: application/xhtml+xml, application/xml
      # image types: image/jpeg, etc

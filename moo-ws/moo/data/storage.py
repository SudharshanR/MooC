"""
Storage interface
"""

import time
from bottle import route, run, request, abort
from pymongo import Connection
from bson.objectid import ObjectId
import sys, traceback
 
connection = Connection('localhost', 27017)
db = connection.mydatabase
 
class Storage(object):
 
   def __init__(self):
      # initialize our storage, data is a placeholder
      self.data = {}

      # for demo
      self.data['created'] = time.ctime()

   def insert(self,name,value):
      print "---> insert:",name,value
      try:
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	entity ={"_id": "doc1", "name": "Test Document 1"}
	db['documents'].save(entity)
        return "added"
      except:
         return "error: data not added"

   #Sud start
   def createUser(self,userJson):
      # print "---> insert:",name,value
      try:
	print("IN myinsert :::::::::::::::::::%s" % (userJson))
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	#entity ={"_id": user, "pwd":pwd}
	user = userJson['email']
	pwd = userJson['password']
	print("Typing in create user------------>");	
	print(user);
	cursor=db.userDetails.find_one({'email':user})
	#print(cursor);
	#res = cursor.next() if cursor.hasNext() else None
	#print(res);
	if cursor is None:
		print("Inside else part");
		db["userDetails"].save(userJson)
	 	return "SUCCESS"
	else:
		return "ERROR"
      except:
         
	 
	 return "no data exists"
   #Sud end

   def updateUser(self,userJson,email):
      # print "---> insert:",name,value
      try:
	print("IN myinsert :::::::::::::::::::%s" % (userJson))
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	#entity ={"_id": user, "pwd":pwd}
	firstName = userJson['firstName']
	lastName = userJson['lastName']
	email = userJson['email']
	status = userJson['status']
	own=userJson['own']
	enrolled=userJson['enrolled']
	quizzes=userJson['quizzes']
	print("Typing in update user of storage------------>");	
	print(userJson);
	print(email);
	#db.userDetails.update({"email":"mm"},{$set:{firstName:"rajan",lastName:"shannnnnnnnnnn"}});
	resOfUpdate=db.userDetails.update(
                    { "email": email },
                    { '$set':{"firstName": firstName,"lastName":lastName,"own":own,"enrolled":enrolled,"status":status}});
	#print(cursor);
	#res = cursor.next() if cursor.hasNext() else None
	#print(res);ma
	
	return str(resOfUpdate)
      except:
         
	 
	 return "no data exists"

   def updateEnrolled(self,email,enrolledCourse):
      # print "---> insert:",name,value
      try:
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	
	resOfUpdate=db.userDetails.update(
                    { "email": email },
                    { '$set':{"enrolled":enrolledCourse}});	
	return str(resOfUpdate)
      except:     
	 
	 return "no data exists"

   def updateOwned(self,email,ownedCourse):
      # print "---> insert:",name,value
      try:
	print("IN myinsert :::::::::::::::::::%s%s" % (email,ownedCourse))
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	
	print("Typing in update own of storage------------>");	
	print(ownedCourse);
	print(email);
	
	resOfUpdate=db.userDetails.update(
                    { "email": email },
                    { '$push':{"own":ownedCourse}});
	
	
	return str(resOfUpdate)
      except:
         
	 
	 return "no data exists"

   def updateQuiz(self,email,ownedQuiz):
      # print "---> insert:",name,value
      try:
	print("IN myinsert :::::::::::::::::::%s%s" % (email,ownedQuiz))
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	
	print("Typing in update quiz of storage------------>");	
	print(ownedQuiz);
	print(email);
	
	resOfUpdate=db.userDetails.update(
                    { "email": email },
                    { '$set':{"quizzes":ownedQuiz}});
	
	
	return str(resOfUpdate)
      except:
         
	 
	 return "no data exists"




   def getUser(self,email):
      # print "---> insert:",name,value
      
      try:
	print("IN storage of get user :::::::::::::::::::%s" % (email))
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	#entity ={"_id": user, "pwd":pwd}
	#user = userJson['email']
	#pwd = userJson['password']
	print("Typing in get user------------>");	
	print(email);
	document=db.userDetails.find_one({'email':email},{ 'email': 1, 'firstName':      		1 ,'lastName':1 ,'_id':0 ,'status':1 ,'own':1,'quizzes':1,'enrolled':1 } )
	#print(cursor);
	#res = cursor.next() if cursor.hasNext() else None
	#print(res);
	if document is None:
		return "ERROR"
	 	
	else:
		
		return document
      except:
         
	 
	 return "no data exists"
   def checkLogin(self,userJson):
      # print "---> insert:",name,value
      try:
	print("IN myinsert :::::::::::::::::::%s" % (userJson))
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	user = userJson['email']
	pwd = userJson['password']
	print("Typing in create user------------>");	
	print(user);
	cursor=db.userDetails.find({'email':user,'password':pwd}).count()
	print(db.userDetails.find({'email':user,'password':pwd}))
	if cursor > 0:
		print("Inside else part");
		return "SUCCESS"
	else:
		return "ERROR"
      except:
         
	       return "no data exists"

   def createCourse(self,courseJson):
      try:
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	title = courseJson['title']
	year = courseJson['year']
	email = courseJson['email']
	cursor= db.course.find({"year":year,"title":title}).count()

	if cursor == 0:
	 	cid = db["course"].save(courseJson)
		#db.userDetails.update({"email":email},{'$set':{"own":"MOOCNAME_"+str(cid)}})
		return str(cid)
	else:
		return "ERROR"    	
      except:
	return "No data found"

   def courselist(self):
      try:
	print("Called store.listallCourses 1 ::::");
	connection = Connection('localhost', 27017)
	db = connection.mydatabase
	cid=db["course"].find()
	if cid.count() > 0:
		print("Called lstore.istallCourses 2 ::::");
		a=list()
		for c in cid:
			cid=str(c['_id'])
			name=(c['title'])
			a.append({cid:name})
			
		return a
	else:
		return '0'
      except:
    	  traceback.print_exc(file=sys.stdout)
	  return "No data"

   def getCourse(self,cid):
      try:
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	document=db.course.find_one({'_id':ObjectId(cid)},{ '_id': 0 }) 
	print document    		
	if document is None:
		return "ERROR"
	 	
	else:
		return document
      except:
         	return "no data exists"

   def updateCourse(self,data,cid):
      try:
	print("entered storage of updaate course :::::::::::::::");  
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	#data=json.loads(content)
	title=data['title']
	description=data['Description']
	category=data['category']
	dept=data['dept']	
	term=data['term']
	year=data['year']
	updatedCourse=db.course.update(
                    { "_id":ObjectId(cid) },
                    { '$set':{"title": title,"description":description,"category":category,"dept":dept, "term":term, "year":year}});
	
	return str(updatedCourse)
      except: 
    	 traceback.print_exc(file=sys.stdout)
	 
	 return "no data exists"

   def listCategory(self):
      try:
	connection = Connection('localhost', 27017)
	db = connection.mydatabase
	cid=db["catagorycollectionDetails"].find()
	
	if cid.count() > 0:
		a=list()
		for c in cid:
			cid=str(c['_id'])
			name=(c['name'])
			a.append({cid:name})
			
		return a
	else:
		return '0'
      except:
	  return "No data"

   def getCategory(self,cid):
      # print "---> insert:",name,value
      try:
	print("IN storage of get user :::::::::::::::::::%s" % (cid))
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	print("Typing in get user------------>");	
	print(cid);
	#objcid="'"+cid+"'"
	document=db.catagorycollectionDetails.find_one({'_id':ObjectId(cid)},{ '_id': 0, 'name': 1 ,'description':1 ,'createDate':1 ,'status':1 }) 
	print document    		
	if document is None:
		return "ERROR"
	 	
	else:
		return document
      except:
         	return "no data exists"

   def createCatagory(self,userJson):
      try:
	print("IN myinsert :::::::::::::::::::%s" % (userJson))
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	cid=db["catagorycollectionDetails"].save(userJson)
	return "MOOC_NAME"+str(cid)
      except:
	return "No data"

   def remove(self,name):
      print "---> remove:",name

   def names(self):
      print "---> names:"
      for k in self.data.iterkeys():
        print 'key:',k

   def find(self,name):
      print "---> storage.find:",name
      if name in self.data:
         rtn = self.data[name]
         print "---> storage.find: got value",rtn
         return rtn
      else:
         return None
   def createannouncementlist(self):
     try:
       connection = Connection('localhost', 27017)
       db = connection.mydatabase
       cid=db["announcementcollectionDetails"].find()
       print "inside storageeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
   
       if cid.count() > 0:
               a=list()
               for c in cid:
                       cid=str(c['_id'])
                       title=(c['title'])
                       description=(c['description'])
                       
                       a.append({cid:title})
                       
               return a
       else:
               return '0'
     except:
         return "No data"

   def getann(self,cid):
     try:
       connection = Connection('localhost', 27017)
       db = connection.mydatabase
       document=db.announcementcollectionDetails.find_one({'_id':ObjectId(cid)},{ '_id': 0 })
       print document                    
       if document is None:
               return "ERROR"
               
       else:
               return document
     except:
                return "no data exists"
 

   def createannouncementcollection(self,userJson):
     # print "-> insert:",name,value
     try:
       print("IN myinsert :::::::::::::::::::%s" % (userJson))
       connection = Connection('localhost', 27017)
       db = connection.mydatabase
       db["announcementcollectionDetails"].save(userJson)
       return "success"
     except:
       return "No data"

   def creatediscussioncollection(self,userJson):
      # print "---> insert:",name,value
      try:
	print("IN myinsert :::::::::::::::::::%s" % (userJson))
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	db["discussioncollectionDetails"].save(userJson)
	return "success"
      except:
	return "No data"

   def enrolledCourselist(self,email):
      try:
	connection = Connection('localhost', 27017)
	db = connection.mydatabase
	cid=db["userDetails"].find({"email":email, "enrolled":{'$ne':"[]"}},{"enrolled":1})
	if cid.count() > 0:
		courseList = cid[0]['enrolled']
		a=list()
		for c in courseList:
			cname = c[c.index(":")+1:]
			details=db["course"].find({"_id":ObjectId(cname)},{"_id":1,"title":1})
			courseID = (details[0]['_id'])
			name = (details[0]['title'])
			a.append({str(courseID):str(name)})
			
		return a
	else:
		return '0'
      except:
    	  traceback.print_exc(file=sys.stdout)
	  return "No data"

   def updateEnrolled(self,enrolledCourseData):
      try:
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	
	cid = enrolledCourseData['cid']
	email = enrolledCourseData['email']
	resOfUpdate=db.userDetails.update(
                    { "email": email },
                    { '$push':{"enrolled":cid}});	
	return 'SUCCESS'
      except:
	 return "no data exists"

   def dropEnrolled(self,droppedCourseData):
      try:
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	
	droppedCourseId = droppedCourseData['cid']
	email = droppedCourseData['email']

	enrolledCourses=db["userDetails"].find({"email":email},{"enrolled":1})[0]
	a = list()
	for c in enrolledCourses['enrolled']:
		print("Enrollled Courses ::"+c+" :::: To drop ::::::"+droppedCourseId)
		if c != droppedCourseId:
			a.append(c)

	resOfUpdate=db.userDetails.update(
                    { "email": email },
                    { '$set':{"enrolled":a}});	
	return 'SUCCESS'
      except:
    	 traceback.print_exc(file=sys.stdout)
	 return "no data exists"


   def ownedCourselist(self,email):
      try:
	connection = Connection('localhost', 27017)
	db = connection.mydatabase
	cid=db["userDetails"].find({"email":email, "own":{'$ne':"[]"}},{"own":1})
	if cid.count() > 0:
		courseList = cid[0]['own']
		print("Course list size :::%d" % len(courseList));
		a=list()
		for c in courseList:
			cname = c[c.index(":")+1:]
			details=db["course"].find({"_id":ObjectId(cname)},{"_id":1,"title":1})
			courseID = (details[0]['_id'])
			name = (details[0]['title'])
			a.append({str(courseID):str(name)})
			
		return a
	else:
		return '0'
      except:
    	  traceback.print_exc(file=sys.stdout)
	  return "No data"

   def deleteCourse(self,courseJson,cid):
      try:
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	email = courseJson['email']
	db.course.remove(
                    { "_id":ObjectId(cid) });
	return "SUCCESS"
      except: 
	 traceback.print_exc(file=sys.stdout)
	 return "no data exists"

   def deleteOwnedCourse(self,courseJson,cid):
      try:
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	email = courseJson['email']
	ownedCourses=db["userDetails"].find({"email":email},{"own":1})[0]
	a = list()
	for c in ownedCourses['own']:
		if c[c.index(":")+1:] != cid:
			print("Skipping :::"+c);
			a.append(c)

	resOfUpdate=db.userDetails.update(
                    { "email": email },
                    { '$set':{"own":a}});
	return "SUCCESS"
      except: 
	 traceback.print_exc(file=sys.stdout)
	 return "no data exists"

   def deleteEnrolledCourse(self,courseJson,cid):
      try:
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	ownedCourses=db["userDetails"].find({"enrolled":cid})
	for c in ownedCourses:
		a = list()
		email = c['email']
		for courses in c['enrolled']:
			if courses != cid:
				a.append(courses)
			db.userDetails.update(
				    { "email": email },
				    { '$set':{"enrolled":a}});
	return "SUCCESS"
      except: 
	 traceback.print_exc(file=sys.stdout)
	 return "no data exists"


   def getdis(self,cid):
      try:
        connection = Connection('localhost', 27017)
	db = connection.mydatabase
	document=db.discussioncollectionDetails.find_one({'_id':ObjectId(cid)},{ '_id': 0 }) 
	print document    		
	if document is None:
		return "ERROR"
	 	
	else:
		return document
      except:
         	return "no data exists"

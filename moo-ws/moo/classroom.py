"""
6, Apr 2013

Example domain logic for the RESTful web service example.

This class provides basic configuration, storage, and logging.
"""

import sys
import os
import socket
import StringIO
import json

# moo 
from data.storage import Storage

#
# Room (virtual classroom -> Domain) functionality - note this is separated 
# from the RESTful implementation (bottle)
#
# TODO: only return objects/data and let moo.py handle formatting through 
# templates
#
class Room(object):
   # very limited content negotiation support - our format choices 
   # for output. This also shows _a way_ of representing enums in python
   json, xml, html, text = range(1,5)
   
   #
   # setup the configuration for our service
   #
   def __init__(self,base,conf_fn):
      self.host = socket.gethostname()
      self.base = base
      self.conf = {}
      
      # should emit a failure (file not found) message
      if os.path.exists(conf_fn):
         with open(conf_fn) as cf:
            for line in cf:
               name, var = line.partition("=")[::2]
               self.conf[name.strip()] = var.strip()
      else:
         raise Exception("configuration file not found.")

      # create storage
      self.__store = Storage()
   

   #
   # example: find data
   #
   def find(self,name):
      print '---> classroom.find:',name
      return self.__store.find(name)

   #
   # example: add data
   #
   def add(self,name,value):
      try:
         self.__store.insert(name,value)
         self.__store.names();
         return 'success'
      except:
         return 'failed'
   def checkLogin(self,data):
      try:
	 print("Inclassromm :::::::::::::");
         
         self.__store.names();
	 return(self.__store.checkLogin(data))
        
      except:
         return 'failed'

   #Sud start
   def userAdd(self,userJson):
      try:
	 print("Inclassromm :::::::::::::");
         
         self.__store.names();
	 return(self.__store.createUser(userJson))
        
      except:
         return 'failed'
   def updateUser(self,userJson,email):
      try:
	 print("Inclassromm of update user:::::::::::::");
         
         self.__store.names();
	 return(self.__store.updateUser(userJson,email))
        
      except:
         return 'failed'


   def updateEnrolled(self,enrolledCourseData):
      try:         
	 return(self.__store.updateEnrolled(enrolledCourseData))
        
      except:
         return 'failed'

   def ownedCourselist(self,email):
      try:
	 return(self.__store.ownedCourselist(email))
         
      except:
         return 'failed'


   def deleteCourse(self,courseJson,cid):
      try:      
	 return(self.__store.deleteCourse(courseJson,cid))
        
      except:
         return 'failed'


   def deleteOwnedCourse(self,courseJson,cid):
      try:      
	 return(self.__store.deleteOwnedCourse(courseJson,cid))
        
      except:
         return 'failed'


   def deleteEnrolledCourse(self,courseJson,cid):
      try:      
	 return(self.__store.deleteEnrolledCourse(courseJson,cid))
        
      except:
         return 'failed'

   def dropEnrolled(self,droppedCourseData):
      try:         
	 return(self.__store.dropEnrolled(droppedCourseData))
        
      except:
         return 'failed'

   def updateCourse(self,courseJson,cid):
      try:  
	 print("entered class room of updaate course :::::::::::::::");    
	 return(self.__store.updateCourse(courseJson,cid))
        
      except:
         return 'failed'
   def updateOwned(self,email,ownedCourse):
      try:
	 print("Inclassromm of update enrolled:::::::::::::");
         
         self.__store.names();
	 return(self.__store.updateOwned(email,ownedCourse))
        
      except:
         return 'failed'

   def updateQuiz(self,email,ownedQuiz):
      try:
	 print("Inclassromm of update enrolled:::::::::::::");
         
         self.__store.names();
	 return(self.__store.updateQuiz(email,ownedQuiz))
        
      except:
         return 'failed'

   def announcementcollectionAdd(self,userJson):
     try:
        print("Inclassromm :::::::::::::");
       
        self.__store.names();
        return(self.__store.createannouncementcollection(userJson))
       
     except:
        return 'failed'

   def discussioncollectionAdd(self,userJson):
      try:
	 print("Inclassromm :::::::::::::");
         
         self.__store.names();
	 return(self.__store.creatediscussioncollection(userJson))
         
      except:
         return 'failed'

  

   def getdis(self,cid):
      try:         
	 return(self.__store.getdis(cid))
        
      except:
         return 'failed'

   def creatediscussionlist(self):
      try:
	 print("Inclassromm :::::::::::::");
         
       	 print "inside classroommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
         self.__store.names();
	 return(self.__store.creatediscussionlist())
         
      except:
         return 'failed'

   def createannouncementlist(self):
     try:
        self.__store.names();
        return(self.__store.createannouncementlist())
       
     except:
        return 'failed'
 
   def getann(self,cid):
     try:        
        return(self.__store.getann(cid))
       
     except:
        return 'failed'
 
 
   def getUser(self,email):
      try:
	 print("Inclassromm :::::::::::::");
         
         self.__store.names();
	 return(self.__store.getUser(email))
        
      except:
         return 'failed'

   def courseAdd(self,courseJson):
      try:
	 return(self.__store.createCourse(courseJson))        
      except:
         return 'failed'

   def courselist(self):
      try:
	 print("Inclassromm :::::::::::::");
         
         self.__store.names();
	 return(self.__store.courselist())
         
      except:
         return 'failed'

   def getCourse(self,cid):
      try:         
	 return(self.__store.getCourse(cid))
        
      except:
         return 'failed'

   def listCategory(self):
      try:
	 print("Inclassromm :::::::::::::");
         
         self.__store.names();
	 return(self.__store.listCategory())
         
      except:
         return 'failed'

   def getCategory(self,cid):
      try:
	 print("Inclassromm :::::::::::::");
         
         self.__store.names();
	 return(self.__store.getCategory(cid))
        
      except:
         return 'failed'
   
   def createCatagory(self,userJson):
      try:
	 print("Inclassromm :::::::::::::");
         
         self.__store.names();
	 return(self.__store.createCatagory(userJson))
         
      except:
         return 'failed'

   def enrolledCourselist(self,email):
      try:
	 return(self.__store.enrolledCourselist(email))
         
      except:
         return 'failed'

#Sud ends

      # TODO success|failure

   #
   # dump the configuration in the requested format. Note placing format logic
   # in the functional code is not really a good idea. However, it is here to
   # provide an example.
   #
   #
   def dump_conf(self,format):
      if format == Room.json:
         return self.__conf_as_json()
      elif format == Room.html:
         return self.__conf_as_html()
      elif format == Room.xml:
         return self.__conf_as_xml()
      elif format == Room.text:
         return self.__conf_as_text()
      else:
         return self.__conf_as_text()

   #
   # output as xml is supported through other packages. If
   # you want to add xml support look at gnosis or lxml.
   #
   def __conf_as_json(self):
      return "xml is hard"

   #
   #
   #
   def __conf_as_json(self):
      try:
         all = {}
         all["base.dir"] = self.base
         all["conf"] = self.conf
         return json.dumps(all)
      except:
         return "error: unable to return configuration"

   #
   #
   #
   def __conf_as_text(self):
      try:
        sb = StringIO.StringIO()
        sb.write("Room Configuration\n")
        sb.write("base directory = ")
        sb.write(self.base)
        sb.write("\n\n")
        sb.write("configuration:\n")
        
        for key in sorted(self.conf.iterkeys()):
           print >>sb, "%s=%s" % (key, self.conf[key])
        
        str = sb.getvalue()
        return str
      finally:
        sb.close()

#
      return "text"

   #
   #
   #
   def __conf_as_html(self):
      try:
        sb = StringIO.StringIO()
        sb.write("<html><body>")
        sb.write("<h1>")
        sb.write("Room Configuration")
        sb.write("</h1>")
        sb.write("<h2>Base Directory</h2>\n")
        sb.write(self.base)
        sb.write("\n\n")
        sb.write("<h2>Configuration</h2>\n")
        
        sb.write("<pre>")
        for key in sorted(self.conf.iterkeys()):
           print >>sb, "%s=%s" % (key, self.conf[key])
        sb.write("</pre>")
     
        sb.write("</body></html>")

        str = sb.getvalue()
        return str
      finally:
        sb.close()

#
# test and demonstrate the setup
#
if __name__ == "__main__":
  if len(sys.argv) > 2:
     base = sys.argv[1]
     conf_fn = sys.argv[2]
     svc = Room(base,conf_fn)
     svc.dump_conf()
  else:
     print "usage:", sys.argv[0],"[base_dir] [conf file]"

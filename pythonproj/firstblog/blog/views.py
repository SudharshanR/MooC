# Create your views here.
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import RequestContext     
import httplib2
import urllib2
import hashlib
import os, sys, re
import datetime
from urllib import urlencode
from blog.models import posts
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from blog.models import MOOC
from blog.models import MOOCS


latest_mooc_list = None
default_mooc = None
user_dict = {}
global moocUrl
global moocName
def moocsToHome(request):

       global moocUrl,moocName
       email=request.POST['email']
	
       print("Entereddddddddddddddd moocsaction::::::");
       moocUrl=request.POST['primaryurl']
       moocName="Headstart"

       print moocUrl
       print moocName
       return render_to_response('home.html',{'email':email},context_instance=RequestContext(request))
def selectMoocs(request):
       listmoocs=MOOCS.objects.all()
       print("IN SELECT MOOCS");
       print(listmoocs.length)
       return render_to_response('moocs.html',{'groups':listmoocs,'email':email},context_instance=RequestContext(request))


def home(request):
        
	
	h = httplib2.Http(".cache")
	resp, content = h.request("http://localhost:8080/hello","GET")
	str_content = content.decode('utf-8')
	
	return render_to_response('index2.html',{'res':str_content})


def loginPage(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def homePage(request):
	email=request.POST['email']
	print("In home page----->")
	return render_to_response('home.html',{'email':email},context_instance=RequestContext(request))

def createUserPage(request):
	return render_to_response('SignUp.html',context_instance=RequestContext(request))

def createannouncementcollection(request):
	h = httplib2.Http()
	resp, content= h.request(
	moocUrl+"/course/list",
	"GET",
	headers={'Content-Type': 'application/json'}
	)
	print("CALLED :::::::::::::::::::::");
	
	#str_content = content.decode('utf-8')
	res=json.loads(content)
	a=list()
	a=res['result']
        return render_to_response('announcementcollection.html', {'res':a},context_instance=RequestContext(request))

def createCoursePage(request):
	email=request.POST['email']
	print("In create course page------->")
	print(email);
	h = httplib2.Http()
	resp, content= h.request(
	"http://localhost:8080/category/list",
	"GET",
	headers={'Content-Type': 'application/json'}
	)
	
	str_content = content.decode('utf-8')
	res=json.loads(str_content)['result']
	a=list()
	a=res

	return render_to_response('createcourse.html',{'res':a,'email':email},context_instance=RequestContext(request))

def createCategoryPage(request):
	email=request.POST['email']
	return render_to_response('createcategory.html',{'email':email},context_instance=RequestContext(request))

#@csrf_exempt
@csrf_exempt
def checkLogin(request):
	global latest_mooc_list, default_mooc, headers, user_dict
	email=request.POST['user']
	pwd=request.POST['pwd']
	status=1
	password=hashlib.sha1(pwd).hexdigest()
	print("SUD called :::::::");
	params = {'email':email,'password':password,'status':status}	
	print(params)	   				        
	data=json.dumps(params)
	h = httplib2.Http()
	resp, content= h.request(
	"http://localhost:8080/user/auth",
	"GET",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
	str_content = content.decode('utf-8')
	print("Content received-->"+str_content);
	#res=json.loads(str_content)['result']
	if(str_content=='SUCCESS'):
		print("Inside if but not entering inner if");
		if(str_content=='SUCCESS'):
			print("Entering if of check login");
			listmoocs=MOOCS.objects.all()
       			print("IN SELECT MOOCS");
       			#print(listmoocs.length)
                	#del user_dict[user.username]; # remove entry with key 'Name'
			# create empty entry in dictionary so that we can add user selections later
			
			#print(""+default_mooc.PrimaryUrl);
			#print(""+email);	       		
			#user_dict[email] = {"url": default_mooc.PrimaryUrl}
			
			
                	#ctx = get_context(request)		
			return render_to_response('moocs.html',{'email':email,'groups':listmoocs},context_instance=RequestContext(request))
	else:
			print("Entering else of check login");		
			return render_to_response('index.html',{'res':str_content},context_instance=RequestContext(request))

def createUser(request):
	
	firstName=request.POST['fname']
	lastName=request.POST['lname']
	email=request.POST['uname']
	p=request.POST['pwd1']
	password=hashlib.sha1(p).hexdigest()
 
	params = 	{'firstName':firstName,'lastName':lastName,'email':email,'password':password,'own':[],
	'quizzes':[],'enrolled':[],'status':[]}   	
	data=json.dumps(params)
  	print("---------------->IN create user :::::::::::::")
	print(data)
	#url=user_dict[email][url]+"/user"
	#print(moocrl);
	h = httplib2.Http()
	resp, content= h.request(
	"http://localhost:8080/user",
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
	#j = json.loads(content)
	str_content = content.decode('utf-8')
	if(str_content=='SUCCESS'):
		return render_to_response('index.html', {'email':email},context_instance=RequestContext(request))
	else:
		return render_to_response('index2.html',  {'res':str_content})
		
'''
def createUser(request):
	
	firstName=request.POST['fname']
	lastName=request.POST['lname']
	email=request.POST['uname']
	p=request.POST['pwd1']
	password=hashlib.sha1(p).hexdigest()
 
	params = 	{'firstName':firstName,'lastName':lastName,'email':email,'password':password,'own':[],
	'quizzes':[],'enrolled':[],'status':[]}   	
	data=json.dumps(params)
  	print("---------------->")
	print(data)
	
	h = httplib2.Http()
	resp, content= h.request(
	"http://localhost:8080/user",
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
	#j = json.loads(content)
	str_content = content.decode('utf-8')
	if(str_content=='SUCCESS'):
		return render_to_response('home.html', {'email':email},context_instance=RequestContext(request))
	else:
		return render_to_response('index2.html',  {'res':str_content})
'''


def createCourse(request):
	#global latest_mooc_list, default_mooc, headers, user_dict
	email=request.POST['email']
	title=request.POST['title']
	category=request.POST['category']
	section=request.POST['section']
	dept=request.POST['dept']
	term=request.POST['term']
	year=request.POST['year']
	iname=request.POST['iname']
	iemail=request.POST['iemail']
	description=request.POST['description']
	version=request.POST['version']
 	print("in create course----------->");
	print(email)
	params = {'email':email,'title':title,'category':category,'section':section,'dept':dept,'term':term,'year':year,'instructor':[{'name':iname,'email':iemail}],'days':[],'hours':[],'Description':description,'attachment':"No Attachment for this course",'version':version}
   	
	data=json.dumps(params)
	print("In create course :::::::::::::::::::;%s" % email);	
	#print(user_dict[email]);
	#url=user_dict[email]["url"]+"/course"
	#print(url);
	url=moocUrl+"/course"
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
	str_content = content.decode('utf-8')
	print("Result of creating course---->"+str_content);
	courseUpdate=moocName+":"+str_content
	params1={'ownedCourse':courseUpdate,'useremail':email}
	data1=json.dumps(params1)
	print("checkkkkkkkkkkkkkkkkkkk");
	print(email)
	url="http://localhost:8080/Ownedupdate"
	h3 = httplib2.Http()
	resp, content= h3.request(
	url,
	"POST",
	body=data1,
	headers={'Content-Type': 'application/json'}
	)
	str_content = content.decode('utf-8')
	print("Result of updating course---->"+str_content);
	return render_to_response('home.html',{'email':email}, context_instance=RequestContext(request))

def updateEnrolled(request):
	cid = request.POST['id']
	email = request.POST['email']

	params = {'cid':moocName+":"+cid,'email':email}
   	data=json.dumps(params)

	url="http://localhost:8080/course/enroll"
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
	str_content = content.decode('utf-8')
	return render_to_response('home.html',{'id':str_content,'email':email},context_instance=RequestContext(request))



	

def listallCourses(request):
	email=request.POST['email']
	h = httplib2.Http()

	url=moocUrl+"/course/list"
	resp, content= h.request(
	url,
	"GET",
	body="",
	headers={'Content-Type': 'text/html'}
	)
	str_content = content.decode('utf-8')
	res=json.loads(str_content)['result']	
	a=list()
	a=res
	return render_to_response('courselist.html',{'res':a,'email':email},context_instance=RequestContext(request))

@csrf_exempt
def getcourse(request):
	email=request.POST['email']
	cid=request.POST['cid']
	url=moocUrl+"/course/%s" % cid
	print(url)
	#url="http://localhost:8080/course/%s" % cid
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"GET",
	headers={'Content-Type': 'application/json'}
	)
	str_content = content.decode('utf-8')
	data=json.loads(content)
	
	title=data['title']
	description=data['Description']
	category=data['category']
	dept=data['dept']

	url=moocUrl+"/category/%s" % category
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"GET",
	headers={'Content-Type': 'application/json'}
	)
	data=json.loads(content)
	category=data['name']
	
	return render_to_response('displaycourse.html',{'email':email,'id':cid,'title':title,'description':description ,'category':category ,'dept':dept },context_instance=RequestContext(request))

def listCategories(request):
	email=request.POST['email']
	url=moocUrl+"/category/list" 
	#"http://localhost:8080/category/list"
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"GET",
	headers={'Content-Type': 'application/json'}
	)
	
	str_content = content.decode('utf-8')
	res=json.loads(str_content)['result']
	categoryList=list()
	categoryList=res

	return render_to_response('listCategory.html',{'res':categoryList,'email':email},context_instance=RequestContext(request))

@csrf_exempt
def updateCoursePage(request):
	email=request.POST['email']
	cid=request.POST['id']
	url=moocUrl+"/course/%s" % cid
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"GET",
	headers={'Content-Type': 'application/json'}
	)
	data=json.loads(content)
	title=data['title']
	description=data['Description']
	category=data['category']
	dept=data['dept']	
	term=data['term']
	year=data['year']
	days=data['days']
	hours=data['hours']
	section=data['section']
	version=data['version']
	url=moocUrl+"/category/list" 
	h2 = httplib2.Http()
	resp2, content2= h2.request(
	url,
	"GET",
	headers={'Content-Type': 'application/json'}
	)
	
	str_content = content2.decode('utf-8')
	res=json.loads(str_content)['result']
	a=list()
	a=res

	return render_to_response('updatecourse.html',{'res':a,'email':email,'id':cid,'title':title,'description':description ,'category':category ,'dept':dept , 'term':term,'year':year,'section':section, 'days':days, 'hours':hours, 'version':version },context_instance=RequestContext(request))


def updateCourse(request):
	email=request.POST['email']
	title=request.POST['title']
	dept=request.POST['dept']
	section=request.POST['section']
	category=request.POST['category']
	description=request.POST['Description']
	cid=request.POST['id']	
	term=request.POST['term']
	year=request.POST['year']

 	url=moocUrl+"/courseupdate/%s" % cid
	params = {'email':email,'title':title,'category':category,'section':section,'dept':dept,'term':term,'year':year,'Description':description}
	data=json.dumps(params)
	url="http://localhost:8080/course/update/%s" % cid

	h = httplib2.Http()
	resp, content= h.request(
	url,
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
	str_content = content.decode('utf-8')
	return render_to_response('home.html',{'email':email}, context_instance=RequestContext(request))


@csrf_exempt
def getCategory(request):
	email=request.POST['email']
	print('came here')
	cid=request.POST['cid']
	url=moocUrl+"/category/%s" % cid
	#url="http://localhost:8080/category/%s" % cid
	print(url)
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"GET",
	headers={'Content-Type': 'application/json'}
	)
	#str_content = content.decode('utf-8')
	data=json.loads(content)
	name=data['name']
	description=data['description']
	createDate=data['createDate']
	status=data['status']
	print(name)
	print(description)
	return render_to_response('displayCategory.html',{'name':name,'description':description ,'createDate':createDate ,'status':status,'email':email },context_instance=RequestContext(request))

def createCategory(request):
	print(" In view of create categoryyy ---------------> ");
	email=request.POST['email']
	name=request.POST['name']
	description=request.POST['desc']
	createDate=request.POST['date']
	status=request.POST['status']
		
	params = {'name':name,'description':description,'createDate':createDate,'status':status}

	data=json.dumps(params)
  	print("---------------->")
	print(data)
	url=moocUrl+"/category"
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
	str_content = content.decode('utf-8')
	return render_to_response('home.html',{'res':str_content,'email':email},context_instance=RequestContext(request))

def deleteCourse(request):
	email=request.POST['email']
	cid=request.POST['id']
 
	params = {'email':email}
	data=json.dumps(params)   
	url=moocUrl+"/coursedelete/%s" % cid

	h = httplib2.Http()
	resp, content= h.request(
	url,
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
   
	url="http://localhost:8080/deleteOwnedCourse/%s" % cid

	h2 = httplib2.Http()
	resp2, content2= h2.request(
	url,
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
   
	url="http://localhost:8080/deleteEnrolledCourse/%s" % moocName+":"+cid

	h3 = httplib2.Http()
	resp3, content3= h3.request(
	url,
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)

	str_content = content.decode('utf-8')
	return render_to_response('home.html',{'email':email}, context_instance=RequestContext(request))

def announcementcollection(request):
       
       #announceId=request.POST['aid']
       courseId=request.POST['cid']
       title=request.POST['title']
       email=request.POST['email']
       
       description=request.POST['desc']
       postDate=request.POST['date']
       status=request.POST['status']
               
       
       params = {'email':email,'courseId':courseId,'title':title,'description':description,'postDate':postDate,'status':status}
       data=json.dumps(params)
       print("-------------->")
       print(data)
       
       h = httplib2.Http()
       resp, content= h.request(
       "http://localhost:8080/announcementcollection",
       "POST",
       body=data,
       headers={'Content-Type': 'application/json'}
       )
       #j = json.loads(content)
       str_content = content.decode('utf-8')
       return render_to_response('home.html',{'email':email,'res':str_content},context_instance=RequestContext(request))

def creatediscussioncollection(request):
      	email=request.POST['email']
	return render_to_response('discussioncollection.html',{'email':email},context_instance=RequestContext(request))
	
def discussioncollection(request):
	
	title=request.POST['title']
	email=request.POST['email']
	
	created_by=request.POST['created_by']
	created_at=request.POST['created_at']
	updated_at=request.POST['updated_at']
		
	
	params = {'title':title,'created_by':created_by,'created_at':created_at,'updated_at':updated_at}
	data=json.dumps(params)
  	print("---------------->")
	print(data)
	
	h = httplib2.Http()
	resp, content= h.request(
	"http://localhost:8080/discussioncollection",
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
	#j = json.loads(content)
	str_content = content.decode('utf-8')
	return render_to_response('home.html',{'res':str_content,'email':email},context_instance=RequestContext(request))

@csrf_exempt
def getdiscussion(request):
	print('came here')
	cid=request.POST['cid']
	email=request.POST['email']
	url="http://localhost:8080/discussion/%s" % cid
	print(url)
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"GET",
	headers={'Content-Type': 'application/json'}
	)
	#str_content = content.decode('utf-8')
	data=json.loads(content)
	title=data['title']
	created_by=data['created_by:']
	created_at=data['created_at']
	updated_at=data['updated_at']
	print(title)
	print(created_by)
	return render_to_response('displaydiscussion.html',{'email':email,'title':title,'created_by':created_by ,'created_at':created_at ,'updated_at':updated_at },context_instance=RequestContext(request))


def listalldiscussion(request):
	email = request.POST['email']
	print("INSIDE list all VIEWS ::::::::::::::::::"+email);
	h = httplib2.Http()
	resp, content= h.request(
	"http://localhost:8080/discussion/list",
	"GET",
	headers={'Content-Type': 'application/json'}
	)
	
	str_content = content.decode('utf-8')
	res=json.loads(str_content)['result']
	a=list()
	a=res
	return render_to_response('discussionlist.html',{'res':a,'email':email},context_instance=RequestContext(request))


def listallannouncement(request):
       print("INSIDE VIEWS ::::::::::::::::::");
       email = request.POST['email']
       h = httplib2.Http()
       resp, content= h.request(
       "http://localhost:8080/announcement/list",
       "GET",
       headers={'Content-Type': 'application/json'}
       )
       
#       str_content = content.decode('utf-8')
       res=json.loads(content)
       a=list()
       a=res['result']
       return render_to_response('announcementlist.html',{'res':a,"email":email},context_instance=RequestContext(request))

@csrf_exempt
def getannouncement(request):
       print('came here')
       cid=request.POST['cid']
       email=request.POST['email']
       url="http://localhost:8080/announcement/%s" % cid
       print(url)
       h = httplib2.Http()
       resp, content= h.request(
       url,
       "GET",
       headers={'Content-Type': 'application/json'}
       )
       #str_content = content.decode('utf-8')
       data=json.loads(content)
       title=data['title']
       description=data['description']
       createDate=data['postDate']
       status=data['status']
       print(title)
       print(description)
       return render_to_response('displayannouncement.html',{'title':title,'description':description ,'createDate':createDate ,'status':status,'email':email },context_instance=RequestContext(request))
 


def dropEnrolled(request):
	cid = request.POST['cid']
	email = request.POST['email']

	params = {'cid':moocName+":"+cid,'email':email}
   	data=json.dumps(params)

	url="http://localhost:8080/course/drop"
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
	str_content = content.decode('utf-8')
	return render_to_response('home.html',{'id':str_content,'email':email},context_instance=RequestContext(request))

def updateOwned(request):
	ownedCourse='mooc'+'000000001'
	#email=request.POST['email']
	email='t@t.com'
	print("PRinting in view of update Enrolled user---------------->")
	print(ownedCourse)
	url="http://localhost:8080/updateOwned/%s" % email
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"POST",
	body=ownedCourse,
	headers={'Content-Type': 'application/json'}
	)
	str_content = content.decode('utf-8')
	return render_to_response('index2.html',  {'res':str_content})

def updateQuiz(request):
	ownedQuiz='mooc'+'000000001'
	#email=request.POST['email']
	email='t@t.com'
	print("PRinting in view of update Enrolled user---------------->")
	print(ownedQuiz)
	url="http://localhost:8080/updateQuiz/%s" % email
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"POST",
	body=ownedQuiz,
	headers={'Content-Type': 'application/json'}
	)
	str_content = content.decode('utf-8')
	return render_to_response('index2.html',  {'res':str_content})


def updateUser(request):
	
	firstName=request.POST['fname']
	lastName=request.POST['lname']
	email=request.POST['email']
	own=request.POST['own']
	quizzes=request.POST['quizzes']
	enrolled=request.POST['enrolled']
	status=request.POST['status']
	
	#password=hashlib.sha1(p).hexdigest()
 
	params = {'firstName':firstName,'lastName':lastName,'email':email,'quizzes':quizzes,'enrolled':enrolled,
	'own':own,'status':status}   	
	data=json.dumps(params)
  	print("PRinting in view of update user---------------->")
	print(data)
	url="http://localhost:8080/updateUser/%s" % email
	h = httplib2.Http()
	resp, content= h.request(
	url,
	"POST",
	body=data,
	headers={'Content-Type': 'application/json'}
	)
	#j = json.loads(content)
	str_content = content.decode('utf-8')
	#if(str_content=='SUCCESS'):
	return render_to_response('home.html', {'email':email},context_instance=RequestContext(request))
	#else:
		#return render_to_response('index2.html',  {'res':str_content})
def getUser(request):
	email=request.POST['email']
	print(email);
	print("In view of getUser--------->")
	
	h = httplib2.Http()
	url="http://localhost:8080/user/%s" % email
	print(url)
	resp, data1= h.request(
	url,
	"GET",
	body="",
	headers={'Content-Type': 'application/json'}
	)
	print(data1);
	#str_content = content.decode('utf-8')
	data=json.loads(data1)
	print("---------------::::::::::::::::::::");	
	print(data);
	email=data['email']
	firstName=data['firstName']
	lastName=data['lastName']
	quizzes=data['quizzes']
	enrolled=data['enrolled']
	status=data['status']
	own=data['own']
	return render_to_response('displayUser.html',{'email':email,'firstName':firstName ,'lastName':lastName ,'status':status ,'own':own,'quizzes':quizzes,'enrolled':enrolled},
context_instance=RequestContext(request))	
	
def getUserForUpdate(request):	
	print("In view of getuserfor update--------->")
	email=request.POST['email']
	h = httplib2.Http()
	url="http://localhost:8080/user/%s" % email
	print(url)
	resp, data1= h.request(
	url,
	"GET",
	body="",
	headers={'Content-Type': 'application/json'}
	)
	print(data1);
	#str_content = content.decode('utf-8')
	data=json.loads(data1)
	print("---------------::::::::::::::::::::");	
	print(data);
	email=data['email']
	firstName=data['firstName']
	lastName=data['lastName']
	quizzes=data['quizzes']
	enrolled=data['enrolled']
	status=data['status']
	own=data['own']
	return render_to_response('updatePerson.html',{'email':email,'firstName':firstName ,'lastName':lastName ,'status':status ,'own':own,'quizzes':quizzes,'enrolled':enrolled},context_instance=RequestContext(request))


def listEnrolledCourses(request):
	email=request.POST['email']
	h = httplib2.Http()
	resp, content= h.request(
	"http://localhost:8080/course/listenrolled/%s" % email,
	"GET",
	body="",
	headers={'Content-Type': 'text/html'}
	)
	str_content = content.decode('utf-8')
	res=json.loads(str_content)['result']
	a=list()
	a=res
	return render_to_response('listenrolledcourses.html',{'res':a,'email':email},context_instance=RequestContext(request))

def listOwnedCourses(request):
	email=request.POST['email']
	h = httplib2.Http()
	resp, content= h.request(
	"http://localhost:8080/course/listowned/%s" % email,
	"GET",
	body="",
	headers={'Content-Type': 'text/html'}
	)
	str_content = content.decode('utf-8')
	res=json.loads(str_content)['result']
	a=list()
	a=res
	return render_to_response('listownedcourses.html',{'res':a,'email':email},context_instance=RequestContext(request))

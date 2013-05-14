from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
     url(r'^moocs$', 'blog.views.selectMoocs', name='selectMoocs'),
     url(r'^moocsToHome$', 'blog.views.moocsToHome', name='moocsToHome'),
     url(r'^$', 'blog.views.home', name='home'),
     url(r'^user/auth$', 'blog.views.loginPage', name='loginPage'),
     url(r'^user/signout$', 'blog.views.loginPage', name='signout'),
     #url(r'^user/:email', 'blog.views.getUser', name='getUser'),
     url(r'^user$', 'blog.views.createUserPage', name='createUserPage'),
      url(r'^home$', 'blog.views.homePage', name='homePage'),

     url(r'^checkLog$', 'blog.views.checkLogin', name='checkLogin'),
     url(r'^SignUp$', 'blog.views.createUser', name='createUser'),
     url(r'^updateEnrolled$', 'blog.views.updateEnrolled', name='updateEnrolled'),
     url(r'^dropEnrolled$', 'blog.views.dropEnrolled', name='dropEnrolled'),
     url(r'^getUser$', 'blog.views.getUser', name='getUser'),
 
     url(r'^updateUser$', 'blog.views.updateUser', name='updateUser'),
     url(r'^getUserForUpdate$', 'blog.views.getUserForUpdate', name='getUserForUpdate'),

    
     url(r'^updateOwned$', 'blog.views.updateOwned', name='updateOwned'),
     url(r'^updateQuiz$', 'blog.views.updateQuiz', name='updateQuiz'),

	
     url(r'^addcourse$', 'blog.views.createCoursePage', name='createCoursePage'),
     url(r'^course/add$', 'blog.views.createCourse', name='createCourse'),
     url(r'^course/list$', 'blog.views.listallCourses', name='listallCourses'),
     url(r'^course/enrolled$', 'blog.views.listEnrolledCourses', name='listEnrolledCourses'),
     url(r'^course/owned$', 'blog.views.listOwnedCourses', name='listOwnedCourses'),
     url(r'^deletecourse$', 'blog.views.deleteCourse', name='deleteCourse'),
     
     url(r'^updatecourse$', 'blog.views.updateCoursePage', name='updateCoursePage'),
     url(r'^course/update$', 'blog.views.updateCourse', name='updateCourse'),
     url(r'^getCourse$', 'blog.views.getcourse', name='getcourse'),
     url(r'^createCategoryPage$', 'blog.views.createCategoryPage', name='createCategoryPage'),
     url(r'^createCategory$', 'blog.views.createCategory', name='createCategory'),
     url(r'^getCategory$', 'blog.views.getCategory', name='getCategory'),
     url(r'^listCategories$', 'blog.views.listCategories', name='listCategories'),
	
     url(r'^announcementcollection$', 'blog.views.createannouncementcollection', name='createannouncementcollection'),
     url(r'^announcement$', 'blog.views.announcementcollection', name='announcementcollection'),

     url(r'^announcement/list$', 'blog.views.listallannouncement', name='listallannouncement'),
     url(r'^getannouncement$', 'blog.views.getannouncement', name='getannouncement'),


     url(r'^discussioncollection', 'blog.views.creatediscussioncollection', name='creatediscussioncollection'), 
     url(r'^discussion', 'blog.views.discussioncollection', name='discussioncollection'), 
 
     url(r'^discussion/list', 'blog.views.listalldiscussion', name='listalldiscussion'), 
     url(r'^getdiscussion', 'blog.views.getdiscussion', name='getdiscussion'), 
    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

from django.urls import path
from . import views

from .views import change_password

urlpatterns = [
    # path('signup/', views.signup, name = "signup"),
    path('addstudents/', views.addstudents, name = "addstudents"),
    path('addstaff/', views.addstaff, name = "addstaff"),
    # path('signin/', views.signin, name = "signin"),
    path('signinsims/', views.signinsims, name = "signinsims"),
	path('logout/', views.logout, name="logout"),
 
 
    path('news/', views.news, name = "news"),
    path('', views.dashboard, name = "dashboard"),
    
    path('patient/', views.patient, name = "patient"),
    path('viewpatient/<str:pk>/', views.viewpatient.as_view(), name = "viewpatient"),
    path('staff/', views.staff, name = "staff"),
    path('studentaccount/', views.studentaccount, name = "studentaccount"),
    path('payments/', views.payments, name = "payments"),
    path('profile/', views.profile, name = "profile"),
    path('myprofile/', views.myprofile, name = "myprofile"),
    path('base/', views.base, name = "base"),
    
    path('addPatient/', views.addPatient, name = "addPatient"),
    path('addstaffcontactinfo/', views.addstaffcontactinfo, name = "addstaffcontactinfo"),
    # path('studentaccount/', views.studentaccount, name = "studentaccount"),

    # url for viewing
    path("viewstudentaccount/<int:id>/",views.viewstudentaccount,name = "viewstudentaccount"),
    # path("viewpatient/<int:id>/",views.viewpatient,name = "viewpatient"),
    path("viewstaffinfo/<int:id>/",views.viewstaffinfo,name = "viewstaffinfo"),
    
    # url for updating the information
    path('updatepatient/<int:pk>/', views.updatepatient, name = "updatepatient"),
    path('updatestaffcontactinfo/<int:id>/', views.updatestaffcontactinfo, name = "updatestaffcontactinfo"),
    path('updatestudentaccount/<int:id>/', views.updatestudentaccount, name = "updatestudentaccount"),
    
    # url for deletting information
    path('deletepatient/<int:pk>/', views.deletepatient, name = "deletepatient"),
    path('deletestaffcontactinfo/<int:id>/', views.deletestaffcontactinfo, name = "deletestaffcontactinfo"),
    path('deletestudentaccount/<int:id>/', views.deletestudentaccount, name = "deletestudentaccount"),
    
    path('change-password/', change_password, name='change_password'),

]

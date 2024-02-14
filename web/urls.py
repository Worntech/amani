from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin, name = "admin"),
    path('signup/', views.signup, name = "signup"),
    path('signin/', views.signin, name = "signin"),
	path('logout/', views.logout, name="logout"),
 
    path("",views.home,name = "home"),
    path("aboutus/",views.aboutus,name = "aboutus"),
    path("base/",views.base,name = "base"),
    path("contactus/",views.contactus,name = "contactus"),
    path("contactpost/",views.contactpost,name = "contactpost"),
    path("contactlist/",views.contactlist,name = "contactlist"),
    path("viewcontact/<int:id>/",views.viewcontact,name = "viewcontact"),
    path('deletecontact/<int:id>/', views.deletecontact, name = "deletecontact"),
    path("dashboard/",views.dashboard,name = "dashboard"),
    path("services/",views.services,name = "services"),
    
    # url for success message
    path("signupsucces/",views.signupsucces,name = "signupsucces"),
    path("logedout/",views.logedout,name = "logedout"),
    
    
    path("invoices/",views.invoices,name = "invoices"),
    path("payments/",views.payments,name = "payments"),
    
    
    path("allstaff/",views.allstaff,name = "allstaff"),
    path("courses/",views.courses,name = "courses"),
]

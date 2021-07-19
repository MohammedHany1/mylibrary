from django.urls import path

from . import views
#from .views import borrowbook

urlpatterns = [
    path('signup/', views.index, name='index'),
    path('login/', views.signin, name='signin'),
    path('update/', views.update, name='update'),
    path('updatepassword/', views.updatepassword, name='updatepassword'),
    path('', views.home, name='home'),
    path('logout/', views.logoutt, name='logoutt'),
    path('student/', views.student, name='student'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('browse/', views.browse, name='browse'),
    path('addbook/', views.addbook, name='addbook'),
    path('<int:id>/', views.changebook, name='changebook'),
    path('borrowbook/', views.borrowbook, name='borrowbook'),
    path('rentbook/<int:id>', views.rentbook, name='rentbook'),
    path('extendbook/<int:id>', views.extendbook, name='extendbook'),
    path('returnbook/<int:id>', views.returnbook, name='returnbook'),
    path('aboutus/', views.aboutus, name='aboutus'),
]
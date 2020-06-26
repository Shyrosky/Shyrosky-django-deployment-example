from django.urls import path
from basic_app import views
#from basic_app.views import index, register

app_name = 'basic_app'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),  
    
]

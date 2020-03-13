from django.conf.urls import url
from collegeapp import views

app_name='collegeapp'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^signin/$',views.signin,name='signin')
]

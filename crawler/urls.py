from django.conf.urls import url
import views


urlpatterns = [ url(r'^crawler/$',views.crawler,name='crawler'),]

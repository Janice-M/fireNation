from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [


    url(r'^$', views.homepage, name='homepage'),
    url(r'^add/hood$', views.add_hood, name='add_hood'),
    url(r'^join_hood/(\d+)', views.join_hood, name='join_hood'),
    url(r'^leave_hood/(\d+)', views.leave_hood, name='leave_hood'),
    url(r'^add/biz$', views.add_biz, name='add_biz'),
    url(r'^add/post$', views.add_post, name='add_post'),
    url(r'^search_results/', views.search_results, name='search_results'),
    url(r'^user/(?P<username>\w+)', views.user_profile, name='user_profile'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT)

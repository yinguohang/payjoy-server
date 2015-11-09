from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PayJoy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^getShopGrade/(\d+)/$', 'website.views.getShopGrade', name="getShopGrade"),
    url(r'^setShopGrade/$', 'website.views.setShopGrade', name="setShopGrade"),
    url(r'^getItemGrade/(\d+)/$', 'website.views.getItemGrade', name="getItemGrade"),
    url(r'^setItemGrade/$', 'website.views.setItemGrade', name="setItemGrade"),
    url(r'^$', 'website.views.index', name="index"),
    url(r'^admin/', include(admin.site.urls)),
)

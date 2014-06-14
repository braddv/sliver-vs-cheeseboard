from django.conf.urls import patterns, include, url
from app.views.home import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='HomeView')
)

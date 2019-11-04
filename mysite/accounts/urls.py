from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('user_fill',views.user_fill,name='user_fill'),
    path(r'accounts/(?P<regdno>\d{10})/user_data',views.user_data,name='user_data'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('user_draft',views.user_draft,name='user_draft'),
    path(r'draft/(?P<regdno>\d{10})/approve',views.approve,name='approve'),
    path(r'draft/(?P<regdno>\d{10})/delete',views.delete,name='delete'),

]

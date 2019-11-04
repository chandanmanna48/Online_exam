from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('aptitude',views.aptitude,name='aptitude'),
    path('reasogning',views.reasogning,name='reasogning'),
    path('gk',views.gk,name='gk'),
    path('sample_practice_gk',views.sample_practice_gk,name='sample_practice_gk'),
    path('online_test_gk',views.online_test_gk,name='online_test_gk'),
    path('GeneralKnowledge_result',views.GeneralKnowledge_result,name='GeneralKnowledge_result'),
    path('sample_practice_aptitude',views.sample_practice_aptitude,name='sample_practice_aptitude'),
    path('online_test_aptitude',views.online_test_aptitude,name='online_test_aptitude'),
    path('aptitude_result',views.aptitude_result,name='aptitude_result'),
    path('sample_practice_reasogning',views.sample_practice_reasogning,name='sample_practice_reasogning'),
    path('online_test_reasogning',views.online_test_reasogning,name='online_test_reasogning'),
    path('reasogning_result',views.reasogning_result,name='reasogning_result'),
    
    
]
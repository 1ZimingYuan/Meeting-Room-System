from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', views.admin_view),
    path('person_home/', views.person_home,name='person_home'),
    path('lab_home/', views.lab_home,name='lab_home'),
    path('lab_log/', views.lab_log,name='lab_log'),
    path('lab_log_out/', views.lab_log_out,name='lab_log_out'),
    path('lab_enroll/', views.enroll,name='enroll'),
    path('school/', views.school_view,name='school'),
    path('school_add/', views.school_add_view,name='school_add'),
    path('school_update/<int:school_id>', views.school_update),
    path('school_delete/<int:school_id>', views.school_delete),
    path('research_direction/', views.research_direction_view,name='research_direction'),
    path('res_add/', views.res_add,name='res_add'),
    path('res_update/<int:res_id>', views.res_update),
    path('res_delete/<int:res_id>', views.res_delete),
    path('lab/', views.lab_view,name='lab'),
    path('lab_add/', views.lab_add_view,name='lab_add'),
    path('lab_update/<int:lab_id>', views.lab_update),
    path('lab_delete/<int:lab_id>', views.lab_delete),
    path('meeting_room/', views.meeting_room_view,name='meeting_room'),
    path('meeting_room_add/', views.meeting_room_add_view,name='meeting_room_add'),
    path('meeting_room_update/<int:m_id>', views.meeting_room_update),
    path('meeting_room_delete/<int:m_id>', views.meeting_room_delete),
    path('薛羽/', views.xueyu_view,name='xueyu'),
    path('xueyu_add/', views.xueyu_add_view,name='xueyu_add'),
    path('xueyu_update/<int:xueyu_id>', views.xueyu_update,),
    path('xueyu_delete/<int:xueyu_id>', views.xueyu_delete,),
    # path('account/<string:account_name>', views.account,),
    path('account', views.account,name='account'),
    path('user_admin/', views.user_admin,name='user_admin'),
    path('password_modification/', views.password_modification,name='password_modification'),


]

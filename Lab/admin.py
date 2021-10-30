from django.contrib import admin
from .models import xueyu, meeting_room, user_login, research_direction


# Register your models here.
class research_direction_manager(admin.ModelAdmin):
    list_display = ['id', 'study_dire', 'school_included', 'labs_included', 'is_active']
    list_display_links = ['id']
    list_editable = ['study_dire']
    list_filter = ['study_dire']
    search_fields = ['study_dire', 'school_included']


class xueyumanager(admin.ModelAdmin):  # 控制管理器后台界面对数据表的显示形式
    list_display = ['id', 'name', 'age', 'sex']  # 显示哪些字段
    list_display_links = ['name']  # 点击哪个字段可以进入其更改页面
    list_filter = ['sex']  # 显示包含哪些字段的过滤器
    search_fields = ['name', 'age']  # 显示可以对哪些字段进行搜索的搜索条
    '''添加可在列表页可编辑的字段，该字段必须在list_display中，
    且必须与list_display_links互斥！'''
    list_editable = ['age']  # 哪些字段可以进行编辑进而修改其后端数据


class meeting_room_manager(admin.ModelAdmin):
    list_display = ['building', 'room_number', ]
    list_display_links = ['room_number']
    search_fields = ['building', 'room_number', ]


class userlogin_manager(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'password', 'gender', 'email']
    list_display_links = ['id']
    list_filter = ['gender']
    search_fields = ['user_name']
    list_editable = ['password', 'gender', 'email']


admin.site.register(xueyu, xueyumanager)
admin.site.register(meeting_room, meeting_room_manager)
admin.site.register(user_login, userlogin_manager)
admin.site.register(research_direction, research_direction_manager)

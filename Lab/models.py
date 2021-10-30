from django.db import models


# Create your models here.
class school(models.Model):
    class Meta:
        db_table = 'school'

    school_name = models.CharField('学院名称', max_length=100, default='', unique=True)
    leader = models.CharField('院长', max_length=100, default='', unique=True)
    num_faculty = models.PositiveIntegerField('教职工数量', default=0)
    num_student = models.PositiveIntegerField('学生数量', default=0)
    is_active = models.BooleanField('is_active', default=True)


class research_direction(models.Model):
    class Meta:
        db_table = 'research_direction'
        verbose_name = '研究方向'
        verbose_name_plural = '研究方向'

    study_dire = models.CharField('研究方向', max_length=100, default='', unique=True, )
    school_included = models.CharField('所涉院系', max_length=1000, default='')
    labs_included = models.PositiveIntegerField('所涉实验组数量', default=0)
    num_researcher = models.PositiveIntegerField('研究人员数量', default=0)
    research_founds = models.DecimalField('总科研经费（万）', max_digits=10, decimal_places=2)
    is_active = models.BooleanField('is_active', default=True)


class labs(models.Model):
    class Meta:
        db_table = 'labs'

    leader = models.CharField('负责人（导师）', max_length=10, default='', unique=True)
    research_direction = models.CharField('研究方向', max_length=100, default='无')
    num_doctors = models.PositiveIntegerField('博士生数量', default=0)
    num_masters = models.PositiveIntegerField('硕士生数量', default=0)
    total_num = models.PositiveIntegerField('总人数', default=0)
    total_found = models.DecimalField('总研究经费（万）', max_digits=10, decimal_places=2)
    is_active = models.BooleanField('is_active', default=True)


class xueyu(models.Model):
    class Meta:
        db_table = 'xueyu'
        verbose_name = '薛羽组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}_{self.age}_{self.sex}'

    name = models.CharField(verbose_name='姓名', max_length=10, default='', unique=True)
    age = models.IntegerField(verbose_name='年龄', default=0)
    sex = models.CharField(verbose_name='性别', max_length=10, default='')
    graduate_institution = models.CharField(verbose_name='最高学位毕业院校', max_length=10, default='')
    positions = models.CharField(verbose_name='职位', max_length=10, default='无')
    title = models.CharField(verbose_name='职称', max_length=11, default='无')
    direction = models.CharField(verbose_name='研究方向', max_length=100, default='无')
    degree = models.CharField(verbose_name='正在研修的学位', max_length=10, default='无')
    is_active = models.BooleanField(verbose_name='is_active', default=True)


class meeting_room(models.Model):
    class Meta:
        db_table = 'meeting_room'
        verbose_name = '会议室'
        verbose_name_plural = verbose_name

    building = models.CharField(verbose_name='楼号', max_length=10, default='')
    room_number = models.CharField(verbose_name='会议室', max_length=10, default='')
    time_range_occupied = models.CharField(verbose_name='占用日期', max_length=100, default='')
    lab_occupying = models.CharField(verbose_name='占用人', default='无', max_length=12)
    phone_number = models.CharField(verbose_name='联系方式', default='无', max_length=45)
    function = models.CharField(verbose_name='用途', default='无', max_length=45)
    is_active = models.BooleanField(verbose_name='is_active', default=True)


class user_login(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name

    user_name = models.CharField(verbose_name='用户名', max_length=40, default='', unique=True)
    password = models.CharField(verbose_name='密码', max_length=50, default='')
    gender = models.CharField(verbose_name='性别', max_length=50, default='')
    email = models.EmailField(verbose_name='邮箱')
    faculty = models.CharField(verbose_name='院系', max_length=100, default='')
    clas = models.CharField(verbose_name='班级', max_length=10,default='')
    stu_job_number = models.CharField(verbose_name='学号/工号', max_length=40, default='') 
    major = models.CharField(verbose_name='专业',max_length=45,default='')
    direction = models.CharField(verbose_name='专业方向', max_length=45, default='')
    identity_class = models.CharField(verbose_name='身份证件类型', max_length=79, default='')
    identity = models.CharField(verbose_name='证件号码', max_length=100, default='')
    phone_number = models.CharField(verbose_name='手机号', max_length=78, default='')



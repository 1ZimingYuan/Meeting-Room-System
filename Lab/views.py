from typing import Mapping
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import school, research_direction, xueyu, meeting_room, labs, user_login
import hashlib
import time 


def person_home(request):
    if request.method == 'GET':
        alert = '<script> alert("该用户不存在或密码错误!")</script>'
        return render(request, 'Lab/lab_log.html', locals())
        
    return render(request, 'Lab/person_home.html')

def lab_home(request):
    return render(request, 'Lab/lab_home.html')

def school_view(request):
    sch = school.objects.all()
    user_name=request.session.get('user_name')
    if user_name:
        return render(request, 'Lab/school_view.html', locals())
    user_name=request.COOKIES.get('user_name')
    if user_name:
        request.session.set('user_name', user_name)
        return render(request, 'Lab/school_view.html', locals())
    
    alert='<script> alert("请先登陆!")</script>'
    return render(request, 'Lab/lab_log.html', locals())

def school_add_view(request):
    user_name=request.session.get('user_name')
    if request.method == 'GET':
        return render(request, 'Lab/school_add_view.html',locals())
    elif request.method == 'POST':
        if request.POST.get('button') == "提交":
            school.objects.create(school_name=request.POST['school_name'],
                                leader=request.POST['leader'],
                                num_student=request.POST['num_student'],
                                num_faculty=request.POST['num_faculty'])
            return HttpResponseRedirect('/Lab/school')
        elif request.POST.get('button') == "取消":
            return HttpResponseRedirect('/Lab/school')

def school_update(request, school_id):
    sch = school.objects.get(id=school_id)
    user_name=request.session.get('user_name')
    if request.method == 'GET':
        return render(request, 'Lab/school_update.html', locals())
    elif request.method == 'POST':
        if request.POST.get('submit') == "更新":
            sch = school.objects.get(id=school_id)
            sch.school_name = request.POST['school_name']
            sch.leader = request.POST['leader']
            sch.num_faculty = request.POST['num_faculty']
            sch.num_student = request.POST['num_student']
            sch.save()
            return HttpResponseRedirect('/Lab/school')
        elif request.POST.get('submit') == "取消":
            return HttpResponseRedirect('/Lab/school')

def school_delete(request, school_id):
    sch = school.objects.get(id=school_id)
    sch.is_active = False
    sch.save()
    return HttpResponseRedirect('/Lab/school')

def research_direction_view(request):
    red = research_direction.objects.all()
    user_name=request.session.get('user_name')
    if user_name:
        return render(request, 'Lab/research_direction_view.html', locals())
    user_name=request.COOKIES.get('user_name')
    if user_name:
        request.session.set('user_name', user_name)
        return render(request, 'Lab/research_direction_view.html', locals())
    
    alert='<script> alert("请先登陆!")</script>'
    return render(request, 'Lab/lab_log.html', locals())

def res_add(request):
    user_name=request.session.get('user_name')
    if request.method == 'GET':
        return render(request, 'Lab/res_add.html',locals())
    elif request.method == 'POST':
        if request.POST.get('submit') == "提交":
            research_direction.objects.create(
                study_dire=request.POST['study_dire'],
                school_included=request.POST['school_included'],
                labs_included=request.POST['labs_included'],
                num_researcher=request.POST['num_researcher'],
                research_founds=request.POST['research_founds'])
            return HttpResponseRedirect('/Lab/research_direction')
        elif request.POST.get('submit') == '取消':
            return HttpResponseRedirect('/Lab/research_direction')

def res_update(request, res_id):
    res = research_direction.objects.get(id=res_id)
    user_name=request.session.get('user_name')
    if request.method == 'GET':
        return render(request, 'Lab/res_update.html', locals())
    elif request.method == 'POST':
        submit = request.POST.get('submit')
        if submit == "提交":
            res.study_dire = request.POST['study_dire']
            res.school_included = request.POST['school_included']
            res.labs_included = request.POST['labs_included']
            res.num_researcher = request.POST['num_researcher']
            res.research_founds = request.POST['research_founds']
            res.save()
            return HttpResponseRedirect('/Lab/research_direction')
        elif submit == '取消':
            return HttpResponseRedirect('/Lab/research_direction')

def res_delete(request, res_id):
    res = research_direction.objects.get(id=res_id)
    res.is_active = False
    res.save()
    return HttpResponseRedirect('/Lab/research_direction')

def xueyu_view(request, ):
    xue = xueyu.objects.all()
    return render(request, 'Lab/xueyu_view.html', locals())

def xueyu_add_view(request):
    if request.method == 'GET':
        return render(request, 'Lab/xueyu_add_view.html')
    elif request.method == 'POST':
        xueyu.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            sex=request.POST['sex'],
            graduate_institution=request.POST['graduate_institution'],
            positions=request.POST['positions'],
            title=request.POST['title'],
            direction=request.POST['direction'],
            degree=request.POST['degree'])
        return HttpResponseRedirect('/Lab/xueyu')

def xueyu_update(request, xueyu_id):
    xy = xueyu.objects.get(id=xueyu_id)
    if request.method == 'GET':
        return render(request, 'Lab/xueyu_update.html', locals())
    elif request.method == 'POST':
        xy.name = request.POST['name']
        xy.age = request.POST['age']
        xy.sex = request.POST['sex']
        xy.graduate_institution = request.POST['graduate_institution']
        xy.positions = request.POST['positions']
        xy.title = request.POST['title']
        xy.direction = request.POST['direction']
        xy.degree = request.POST['degree']
        xy.save()
        return HttpResponseRedirect('/Lab/xueyu')

def xueyu_delete(request, xueyu_id):
    xy = xueyu.objects.get(id=xueyu_id)
    xy.is_active = False
    xy.save()
    return HttpResponseRedirect('/Lab/xueyu')

def meeting_room_view(request):
    met = meeting_room.objects.all()
    user_name=request.session.get('user_name')
    if user_name:
        return render(request, 'Lab/meeting_room.html', locals())
    user_name=request.COOKIES.get('user_name')
    if user_name:
        request.session.set('user_name', user_name)
        return render(request, 'Lab/meeting_room.html', locals())
    
    alert='<script> alert("请先登陆!")</script>'
    return render(request, 'Lab/lab_log.html', locals())

def meeting_room_add_view(request):
    user_name=request.session.get('user_name')
    if request.method == 'GET':
        mo_da={}
        tim=time.localtime(time.time())
        if tim[1] in [1,3,5,7,8,10,12]:
            if tim[2]+6<=31:
                mo_da[str(tim[1])]=[tim[2]+i for i in range(7)]
            else:
                mo_da[str(tim[1])]=[]
                mo_da[str(tim[1]+1)]=[]
                for i in range(7):
                    if tim[2]+i<=31:
                        mo_da[str(tim[1])].append(tim[2]+i)
                    else:
                        mo_da[str(tim[1]+1)].append((tim[2]+i)%31)
        else:
            if tim[2]+6<=30:
                mo_da[str(tim[1])]=[tim[2]+i for i in range(7)]
            else:
                mo_da[str(tim[1])]=[]
                mo_da[str(tim[1]+1)]=[]
                for i in range(7):
                    if tim[2]+i<=30:
                        mo_da[str(tim[1])].append(tim[2]+i)
                    else:
                        mo_da[str(tim[1]+1)].append((tim[2]+i)%30) 
        day=[]
        for i,j in mo_da.items():
            for  k in j:
                day.append(i+'月'+str(k)+'日')


        # if tim[1] in [1,3,5,7,8,10,12]:
        #     day=[(tim[2])%32,(tim[2]+1)%32,(tim[2]+2)%32,(tim[2]+3)%32,(tim[2]+4)%32,(tim[2]+5)%32,(tim[2]+6)%32]
        # else:
        #     day=[(tim[2])%31,(tim[2]+1)%31,(tim[2]+2)%31,(tim[2]+3)%31,(tim[2]+4)%31,(tim[2]+5)%31,(tim[2]+6)%31]
        
        return render(request, 'Lab/meeting_room_add_view.html',locals())
    elif request.method == 'POST':
        submit = request.POST.get('submit')
        if submit == "提交":
            meeting_room.objects.create(
                building=request.POST['building'],
                room_number=request.POST['room_number'],
                time_range_occupied=request.POST['time_range_occupied']+','+request.POST['start_time']+'-'+request.POST['end_time'],
                lab_occupying=request.POST['lab_occupying'],
                phone_number=request.POST['phone_number'],
                function=request.POST['function'])
            return HttpResponseRedirect('/Lab/meeting_room/')
        elif submit =="取消":
            return HttpResponseRedirect('/Lab/meeting_room/')

def meeting_room_update(request, m_id):
    user_name=request.session.get('user_name')
    m = meeting_room.objects.get(id=m_id)
    print(m.time_range_occupied)
    date=m.time_range_occupied.split(',')[0]
    start_time = m.time_range_occupied.split(',')[1].split('-')[0]
    end_time = m.time_range_occupied.split(',')[1].split('-')[1]
    if request.method == 'GET':
        return render(request, 'Lab/meeting_room_update.html', locals())
    elif request.method == 'POST':
        submit = request.POST.get('submit')
        if submit == "更新":
            m.building = request.POST['building']
            m.room_number = request.POST['room_number']
            m.time_range_occupied = request.POST['time_range_occupied']+','+request.POST['start_time']+'-'+request.POST['end_time']
            m.lab_occupying = request.POST['lab_occupying']
            m.function = request.POST['function']
            m.phone_number = request.POST['phone_number']
            m.save()
            return HttpResponseRedirect('/Lab/meeting_room')
        elif submit =="取消":
            return HttpResponseRedirect('/Lab/meeting_room')

def meeting_room_delete(request, m_id):
    m = meeting_room.objects.get(id=m_id)
    m.is_active = False
    m.save()
    return HttpResponseRedirect('/Lab/meeting_room')

def lab_view(request):
    lab = labs.objects.all()
    user_name=request.session.get('user_name')
    if user_name:
        return render(request, 'Lab/labs_view.html', locals())
    user_name=request.COOKIES.get('user_name')
    if user_name:
        request.session.set('user_name', user_name)
        return render(request, 'Lab/labs_view.html', locals())
    alert='<script> alert("请先登陆!")</script>'
    return render(request, 'Lab/lab_log.html', locals())

def lab_add_view(request):
    user_name=request.session.get('user_name')
    if request.method == 'GET':
        return render(request, 'Lab/lab_add.html',locals())
    elif request.method == 'POST':
        submit = request.POST.get('submit')
        if submit == "提交":
            labs.objects.create(
                leader=request.POST['leader'],
                research_direction=request.POST['research_direction'],
                num_masters=request.POST['num_masters'],
                num_doctors=request.POST['num_doctors'],
                total_num=request.POST['total_num'],
                total_found=request.POST['total_found'])
            return HttpResponseRedirect('/Lab/lab')
        elif submit == "取消":
             return HttpResponseRedirect('/Lab/lab')

def lab_update(request, lab_id):
    lab = labs.objects.get(id=lab_id)
    user_name=request.session.get('user_name')
    if request.method == 'GET':
        return render(request, 'Lab/lab_update.html', locals())
    elif request.method == 'POST':
        submit = request.POST.get('submit')
        if submit == "更新":
            lab.leader = request.POST['leader']
            lab.research_direction = request.POST['research_direction']
            lab.num_doctors = request.POST['num_doctors']
            lab.num_masters = request.POST['num_masters']
            lab.total_num = request.POST['total_num']
            lab.total_found = request.POST['total_found']
            lab.save()
            return HttpResponseRedirect('/Lab/lab')
        elif submit == '取消':
            return HttpResponseRedirect('/Lab/lab')

def lab_delete(request, lab_id):
    lab = labs.objects.get(id=lab_id)
    lab.is_active = False
    lab.save()
    return HttpResponseRedirect('/Lab/lab')

def lab_log(request):
    if request.method == 'GET':
        user_name=request.session.get('user_name')
        if user_name:
            # print('sesion',request.session.get('user_name'))
            # return render(request, 'Lab/already_logged.html')
            return render(request,'Lab/person_home.html', locals())
        user_name = request.COOKIES.get('user_name')    
        if user_name:
            # print('cookie',c_user_name)
            request.session['user_name'] = user_name
            # return render(request,'Lab/already_logged.html')
            return render(request,'Lab/person_home.html', locals())
        return render(request, 'Lab/lab_log.html')
    elif request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        if request.POST.get('action') == '登录':
            has = hashlib.md5()
            has.update(password.encode())
            password_ = has.hexdigest()
            if (user_name,) not in user_login.objects.values_list('user_name') or \
                    (password_,) not in user_login.objects.values_list('password'):
                alert = '<script> alert("该用户不存在或密码错误!")</script>'
                return render(request, 'Lab/lab_log.html', locals())
            request.session['user_name'] = user_name
            # res = HttpResponse('<div align="center"><h1>登录成功！</h1></div>')
            res = render(request,'Lab/person_home.html', locals())
            if 'remember' in dict(request.POST).keys():
                res.set_cookie('user_name', user_name, 3 * 24 * 60 * 60)
            return res
        elif request.POST['action'] == '注册':
            return HttpResponseRedirect('/Lab/lab_enroll')
        else:
            return HttpResponseRedirect('/Lab/lab_home')

def lab_log_out(request):
    # request.session.delete('user_name')
    if 'user_name' in request.session:
        del request.session['user_name']
    res=HttpResponseRedirect('/Lab/lab_log')
    if 'user_name' in request.COOKIES:
        res.delete_cookie('user_name')
    return res

def enroll(request):
    if request.method == 'GET':
        return render(request, 'Lab/enroll.html')
    elif request.method == 'POST':
        if request.POST.get('enroll'):
            if request.POST.get('user_name') == '' or request.POST.get(
                    'password') == '':
                alert = '<script>alert("用戶名和密码不能为空！")</script>'
                return render(request, 'Lab/enroll.html', locals())
            elif request.POST['password'] != request.POST['confirm']:
                alert = '<script>alert("确认密码错误!")</script>'
                return render(request, 'Lab/enroll.html', locals())
            elif (request.POST['user_name'],
                  ) in user_login.objects.values_list('user_name'):
                alert = '<script>alert("该用户已存在!")</script>'
                return render(request, 'Lab/enroll.html', locals())
            else:
                try:
                    has = hashlib.md5()
                    has.update(request.POST['password'].encode())
                    has = has.hexdigest()
                    user_login.objects.create(
                        user_name=request.POST['user_name'],
                        password=has,
                        gender=request.POST.get('gender', '男'),
                        email=request.POST['email'],
                        faculty=request.POST['faculty'],
                        clas=request.POST['clas'],
                        stu_job_number=request.POST['stu_job_number'],
                        major=request.POST['major'],
                        direction=request.POST['direction'],
                        identity_class=request.POST['identity_class'],
                        identity=request.POST['identity'],
                        phone_number=request.POST['phone_number'])
                    user_name=request.POST.get('user_name')
                    request.session['user_name'] = user_name
                    # res = HttpResponse('<div align="center"><h1>登录成功！</h1></div>')
                    alert = '<script>alert("注册成功!")</script>'
                    res = render(request,'Lab/person_home.html', locals())
                    res.set_cookie('user_name', user_name, 3 * 24 * 60 * 60)
                    return res
                    alert = '<script>alert("注册成功!")</script>'
                    return render(request, 'Lab/person_home.html', locals())
                except Exception as e:
                    print('4455',e)
                    alert = '<script>alert("该用户已存在!")</script>'
                    return render(request, 'Lab/enroll.html', locals())

        elif request.POST.get('return'):
            return HttpResponseRedirect('/Lab/lab_home')
        elif request.POST.get('login'):
            return HttpResponseRedirect('/Lab/lab_log')
    
def account(request):
    if request.method == 'GET':
        account_name = request.session.get('user_name')
        account_info= user_login.objects.get(user_name=account_name)
        return render(request, 'Lab/account.html', locals())
    elif request.method == 'POST':
        account_name = request.session.get('user_name')
        # account_info= user_login.objects.get(user_name=account_name)
        enroll=request.POST.get('enroll')
        if enroll == '更改':
            # account_name = request.session.get('user_name')
            account_info= user_login.objects.get(user_name=account_name)
            return render(request, 'Lab/account_.html', locals())
        elif enroll == '提交':
           user = user_login.objects.get(user_name=request.session.get('user_name'))
           user.user_name = request.POST['user_name']
           user.gender = request.POST['gender']
           user.email = request.POST['email']
           user.faculty = request.POST['faculty']
           user.clas = request.POST['clas']
           user.stu_job_number = request.POST['stu_job_number']
           user.major = request.POST['major']
           user.direction = request.POST['direction']
           user.identity_class = request.POST['identity_class']
           user.identity = request.POST['identity']
           user.phone_number = request.POST['phone_number']
           user.save()
           account_info= user_login.objects.get(user_name=account_name)
           return render(request, 'Lab/account.html',locals())

        elif enroll == '取消':
            # user_name = request.POST['user_name']
            account_name = request.session.get('user_name')
            account_info= user_login.objects.get(user_name=account_name)
            # res = HttpResponse('<div align="center"><h1>登录成功！</h1></div>')
            res = render(request,'Lab/account.html', locals())
            if 'remember' in dict(request.POST).keys():
                res.set_cookie('user_name', account_name, 3 * 24 * 60 * 60)
            return res
        elif enroll == '返回':
            user_name = request.session.get('user_name')
            return render(request, 'Lab/person_home.html', locals())
        elif enroll == "修改密码":
            # user_name = request.session.get('user_name')
            # return render(request, "Lab/password_modification.html",locals())
            return HttpResponseRedirect("/Lab/password_modification")
            
def password_modification(request):
    user_name = request.session.get('user_name')
    if request.method == 'GET':
        return render(request, "Lab/password_modification.html",locals())
    if request.method == 'POST':
        submit = request.POST.get('submit')
        if submit == '取消':
            return HttpResponseRedirect('/Lab/account')
        elif submit == '提交':
            if request.POST.get('password') == "":
                alert='<script> alert("密码不能为空!")</script>'
                return render(request, "Lab/password_modification.html",locals())
            if request.POST.get('password') != request.POST.get('confirm'):
                alert='<script> alert("密码不一致!")</script>'
                return render(request, "Lab/password_modification.html",locals())
            else:
                user_name == request.session.get('user_name')
                user = user_login.objects.get(user_name=user_name)
                has = hashlib.md5()
                has.update(request.POST.get('password').encode())
                has = has.hexdigest()
                if has == user.password:
                    alert='<script> alert("新密码不能与原密码一致!")</script>'
                    return render(request, "Lab/password_modification.html",locals())
                user.password = has
                user.save()
                return HttpResponseRedirect('/Lab/account')

def user_admin(request):
    pass


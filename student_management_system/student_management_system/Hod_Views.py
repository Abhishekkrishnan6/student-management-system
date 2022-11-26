from django.shortcuts import  render, redirect
from django.contrib.auth.decorators import  login_required

from student_management.models import  Course,Session_Year,CustomUser,Student,Staff,Subject
from django.contrib import messages
@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()

    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female =Student.objects.filter(gender = 'Female').count()
    print(student_gender_female,student_gender_male)

    context = {
        'student_count':student_count,
        'staff_count':staff_count,
        'course_count':course_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,


    }
    #return render(request,'Hod/home.html')

    return render(request,'Hod1/home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'email is already taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=email).exists():
            messages.warning(request,'username is already taken')
            return redirect('add_student')
        else:
            user=CustomUser(
                first_name = first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type = 3

            )
            user.set_password( password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
            )
            student.save()
            messages.success(request,user.first_name + "  " + user.last_name + " Are Successfully added")
            return redirect('add_student')




    context = {
        'course':course,
        'session_year':session_year,
    }

    return render(request , 'Hod1/add_student.html',context)


def VIEW_STUDENT(request):
    student = Student.objects.all()
    #print(student)
    context = {
        'student':student,
    }
    return render(request,'Hod1/view_student.html',context)


def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    context = {
        'student':student,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'Hod1/edit_student.html',context)


def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
       # print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        #print(profile_pic)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        #update user after editing
        user = CustomUser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course
        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year



        student.save()
        messages.success(request,'Record are succesfully updated')

        return  redirect('view_student')



    return render(request,'Hod1/edit_student.html')


def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id= admin)
    student.delete()
    messages.success(request,'Record are successfully deleted')
    return redirect('view_student')


def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        #print(course_name)

        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request,'Course Are succesfully created')
        return redirect('add_course')
    return render(request,'Hod1/add_course.html')


def VIEW_COURSE(request):
    course = Course.objects.all()
    #print(course)
    context={
        'course':course
    }
    return render(request,'Hod1/view_course.html',context)


def EDIT_COURSE(request,id):
    course = Course.objects.get(id = id)
    context = {
        'course':course,
    }
    return render(request,'Hod1/edit_course.html',context)


def UPDATE_COURSE(request ):
    if request.method == "POST":
        name = request.POST.get('name')
        # course_name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')
        # print(course_name,course_id)
        course = Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request,'Course are successfully added')
        return redirect('view_course')


    return render(request,'Hod1/edit_course.html')


def DELETE_COURSE(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request,'Courseare successfully delete')
    return redirect('view_course')


def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is Already Taken')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is Already Taken')
            return redirect('add_staff')
       # print(profile_pic,first_name,last_name,password,email,username,address,gender)

        else:
            user = CustomUser(first_name = first_name , last_name = last_name,email=email,username = username ,profile_pic=profile_pic,user_type=2)
            user.set_password(password)
            user.save()

            staff = Staff(
                   admin = user,
                address = address,
                gender = gender
            )
            staff.save()

            messages.success(request,'Staff are successfully added')
            return redirect('add_staff')


    return render(request,'Hod1/add_staff.html')


def VIEW_STAFF(request):
    staff = Staff.objects.all()
    print(staff)
    context = {
        'staff':staff,
    }
    return render(request , 'Hod1/view_staff.html',context)


def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id = id)
    context = {
        'staff': staff,
    }
    return render(request,'Hod1/edit_staff.html',context)


def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('stff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id = staff_id)
        user.username=username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        print(first_name,last_name)
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic



        user.save()
        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request,'Staff is succesfully Update')
        return redirect('view_staff')




    return render(request,'Hod1/edit_staff.html')


def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')



        course = Course.objects.get(id = course_id)
        staff  = Staff.objects.get(id = staff_id)
        subject = Subject(


            name = subject_name,
            course = course ,
            staff = staff




        )
        subject.save()
        messages.success(request,'Subjects are successfully added')
        return redirect('add_subject')





    context = {
        'course':course,
        'staff':staff,
    }
    return render(request,'Hod1/add_subject.html',context)
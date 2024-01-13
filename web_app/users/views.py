from collections import OrderedDict
from .models import Member
from .models import Courses_detail   # UsCoursesDetail
import charset_normalizer
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from  reportlab.lib.units import inch 
from reportlab.lib.pagesizes import letter


def all_details_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    # Create text object
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 15)

    # Designate the models
    members = Member.objects.all()
    
    courses_detail = Courses_detail.objects.all() 

    # Create a blank list
    lines = []

    # Loops
    for member in members:
        lines.append(member.id)
        lines.append(member.name)
        lines.append(member.surname)
        lines.append(member.address)
        lines.append(member.age)
        lines.append(member.phone_number)
        lines.append(member.date_of_birth)
        lines.append(member.school_name)
        lines.append(member.parents_occupation)
        lines.append(member.courses)
        lines.append(member.fees)
        lines.append(member.created_at)
        lines.append(member.updated_at)
        lines.append(member.date)
        lines.append(member.timestamp)
        lines.append(" ")

    for Courses_detail in Courses_detail:
        lines.append(Courses_detail.course_list)
        lines.append(Courses_detail.course_fee)
        lines.append(Courses_detail.course_time)
        lines.append(Courses_detail.course_time2)
        lines.append(Courses_detail.instructor)
        lines.append(" ")


    # Loop
    for line in lines:
        textobj.textLine(line)

    # Finish up
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='all_details.pdf')


# Below all the functions are defined for homepage, registartionpage, & all models functions 
def homepage(request):
    return render(request, 'homepage.html')


def Entry(request):
    latest_Entry = Entry.objects.latest('id')
    Entry_number = latest_Entry.Entry_number + 1 if latest_Entry else 1

    if request.method == 'POST':
        selected_courses = request.POST.get('course')
        if len(selected_courses) >= 4:
            return HttpResponse("You can select a maximum of 4 courses.")
        # Process form data and create a new entry
        # Assign entry_number to the entry being created

        return HttpResponse('registration successful!')
    return render(request, 'create_Entry.html', {'Entry_number': Entry_number})


def registration(request):
    courses = Courses_detail.objects.all()
    id =None

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        address = request.POST.get('address')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        school_name = request.POST.get('school_name')
        parents_occupation = request.POST.get('parents_occupation')
        
        
        #course_list name write name as model name
        # courses = request.POST.get('courses')
        fees = request.POST.get('fees')
        time = request.POST.get('time')
        time2 = request.POST.get('time2')
        date = request.POST.get('date')
        

        obj = Member(
            name=name,
            surname=surname,
            address=address,
            age=age,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            school_name=school_name,
            parents_occupation=parents_occupation,
            id = id,
            # subject=subject,
            fees=fees,
            date=date,
            
        )
        obj.save()


    # context = {'page': page}
    messages.success(request, "your registration was successfully",{'id':id})
    
    context = {'courses': courses}
    return render(request, 'registration.html', {'courses': courses})


    
    course_list = []
    course_fee =  []
    course_time =  []
    course_time2= []
    
    return render(request, 'registration.html')
    return render(request, 'registration.html',{'course_list': course_list, 'course_fee': course_fee, 'course_time': course_time , 'course_time2':course_time2})



# this function is for 2nd model  courses_deatails.
# dict course render to regist.
def courses_list(request):
    courses = Courses_detail.objects.all()
    return render(request, 'registration.html', {'courses': courses})


def courses_detail(request, course_id):
    course = Courses_detail.objects.get(id=course_id)
    fees = fees.objects.filter(course=course)
    times = times.objects.filter(course=course)
    return render(request, 'registration.html', {'courses': course})

# def  UsCoursesDetail(request):
#     id = request.POST.get('id')
#     course = request.POST.get('course')
#     member =  request.POST.get('course')
    
#     if request.method == 'POST':
#         id = request.POST.get('id')
#         course = request.POST.get('course')
#         member = request.POST.get('member')
        
#         obj = UsCoursesDetail(
#             id= id,
#             course = course,
#             member = member,
#         )   
        
#         obj.save()
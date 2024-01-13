from django.shortcuts import render


def courses_deatails(request):
    if request.method == 'POST':
        course_list = request.POST.get('course_list')
        course_fee = request.POST.get('course_fee')
        course_time  = request.POST.get('course_time')
        course_time2  = request.POST.get('course_time2')
        instructor = request.POST.get('instructor')


        co = courses_deatails(
            course_list =course_list,
            course_fee  = course_fee,
            course_time = course_time,
            course_time2 = course_time2,
            instructor = instructor,
           )
        co.save()

    return render(request, 'registration.html', {'course_list': course_list, 'course_fee': course_fee, 'course_time': course_time , 'course_time2':course_time2 , 'instructor': instructor})
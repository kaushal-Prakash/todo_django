from django.shortcuts import render
from .models import Student, Course


# 🏠 Home
def home(request):
    return render(request, 'home.html')


# 👨‍🎓 Student List
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


# 📚 Course List
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


# 📝 Register (Enroll Student)
def register(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == "POST":
        student_id = request.POST.get('student')
        course_id = request.POST.get('course')

        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)

        student.courses.add(course)

        return render(request, 'success.html', {
            'message': f"{student.name} enrolled in {course.coursename}"
        })

    return render(request, 'register.html', {
        'students': students,
        'courses': courses
    })


# 📊 Enrolled List (Students per Course)
def enrolled_list(request):
    courses = Course.objects.all()
    students = None
    selected_course = None

    if request.method == "POST":
        course_id = request.POST.get('course')
        selected_course = Course.objects.get(id=course_id)
        students = selected_course.students.all()

    return render(request, 'enrolled_list.html', {
        'courses': courses,
        'students': students,
        'selected_course': selected_course
    })
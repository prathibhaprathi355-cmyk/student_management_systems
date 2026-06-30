from django.shortcuts import render , redirect
from .models import Student
from django.http import HttpResponse

# Create your views here.
def displayDetails(request):
    students = Student.objects.all()

    context = {
        'students' : students
    }

    return render(request , 'student-details.html' , context)
def one_student_details(request ,id ):
    # print(id)
    student = Student.objects.get(id=id)

    context ={
        'student':student
    }

    return render(request , 'one-student-details.html',  context)


def create_student(request):
    if request.method =='POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        marks = request.POST.get('marks')
        course = request.POST.get('course')
        admsnType = request.POST.get('admsnType')

        Student.objects.create(name=name , roll = roll , marks=marks , course = course , admsnType=admsnType)

        return redirect('home')
        
    return render(request , 'create-student.html')

def update_student_view(request , id ):
    try:
        student = Student.objects.get(id=id)
        
    except Student.DoesNotExist:
        return HttpResponse("Student id not found")
    if request.method =='POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        marks = request.POST.get('marks')
        course = request.POST.get('course')
        admsnType = request.POST.get('admsnType')

        student.name=name 
        student.marks=marks 
        student.course = course 
        student.admsnType=admsnType
        student.save()

        return redirect('home')
    context={
        'student' : student
    }
    return render(request ,'update.html' , context)
def delete_student(request,id):
    try:
        student =Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse('Student id not found')
    
    if request.POST:
        student.delete()
        return redirect('home')
    context={
        'student' : student
    }
    return render(request , 'delete-student.html' , context)

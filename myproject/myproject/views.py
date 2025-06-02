from django.shortcuts import render,redirect
from myapp.models import *

def homePage(request):
    return render(request,"home.html")


def student_list(request):
    students = StudentModel.objects.all()
    return render(request, 'student.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        student = StudentModel(
            StudentName=request.POST.get('StudentName'),
            StudentId=request.POST.get('StudentId'),
            Department=request.POST.get('Department'),
            Mobile=request.POST.get('Mobile'),
            Date_of_Birth=request.POST.get('Date_of_Birth'),
            Age=request.POST.get('Age'),
            Address=request.POST.get('Address'),

        )

        student.save()
        return redirect('student')
    return render(request, 'addstudent.html')
def student_edit(request,id):
    student=StudentModel.objects.get(id=id)
    if request.method == 'POST':
        student = StudentModel(
                id=id,
                StudentName=request.POST.get('StudentName'),
                StudentId=request.POST.get('StudentId'),
                Department=request.POST.get('Department'),
                Mobile=request.POST.get('Mobile'),
                Date_of_Birth=request.POST.get('Date_of_Birth'),
                Age=request.POST.get('Age'),
                Address=request.POST.get('Address'),

            )

        student.save()
        return redirect('student')  
    return render(request, 'editsutdent.html',{'student' : student })


def student_delete(req,id):
    student=StudentModel.objects.get(id=id).delete()
    return redirect('student')

def student_view(req,id):
    student=StudentModel.objects.get(id=id)
    return render(req,'viewstudent.html',{'student' : student })      

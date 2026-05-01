from django.shortcuts import render,get_object_or_404
from .forms import StudentForm
from . models import Student

# Create your views here.


def home_modelForm(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'student_success.html')   

    return render(request,'home.html',{'form':form})


def student_list(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})


def student_detail(request,id):
    student=get_object_or_404(Student,id=id)
    return render(request,'student_detail.html')
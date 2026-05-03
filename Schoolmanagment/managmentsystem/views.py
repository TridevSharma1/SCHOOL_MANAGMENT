from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# 📌 READ (List)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


# 📌 CREATE
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get('name'),
            student_class=request.POST.get('student_class'),
            city=request.POST.get('city'),
            age=request.POST.get('age'),
            address=request.POST.get('address'),
            roll_no=request.POST.get('roll_no'),
            image=request.FILES.get('image')
        )
        return redirect('student_list')

    return render(request, 'add_student.html')


# 📌 UPDATE
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.student_class = request.POST.get('student_class')
        student.city = request.POST.get('city')
        student.age = request.POST.get('age')
        student.address = request.POST.get('address')
        student.roll_no = request.POST.get('roll_no')

        if request.FILES.get('image'):
            student.image = request.FILES.get('image')

        student.save()
        return redirect('student_list')

    return render(request, 'update_student.html', {'student': student})


# 📌 DELETE
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')
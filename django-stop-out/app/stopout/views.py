from django.shortcuts import render, get_object_or_404

from .models import School, Student


def index(request):
    school_list = School.objects.order_by('name')
    context = {
        'school_list': school_list,
    }
    return render(request, 'stopout/index.html', context)


# 학교별로 학생 리스트 보여줌
def school_view(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    student_list = school.student_set.all()
    context = {
        'school': school,
        'student_list': student_list,

    }
    return render(request, 'stopout/school_view.html', context)

# 전체 학생 목록 보여주기
def student_list(request):
    all_student_list = Student.objects.all()
    context = {
        'all_student_list': all_student_list,
    }
    return render(request, 'stopout/student.html', context)

#학생 한명 목록 보여주
def student_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    friends = student.friends.all()
    context = {
        'student': student,
        'friends': friends,
        'school': student.school.name,
    }
    return render(request, 'stopout/student_view.html', context)




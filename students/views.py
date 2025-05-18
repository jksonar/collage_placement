from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from placements.models import Company, JobApplication
from accounts.models import StudentProfile
from .models import OffCampusApplication

@login_required
def dashboard(request):
    student = request.user.studentprofile
    applications = JobApplication.objects.filter(student=student)
    ongoing_companies = Company.objects.filter(application_deadline__gte=timezone.now())
    
    context = {
        'student': student,
        'applications_count': applications.count(),
        'ongoing_companies': ongoing_companies,
        'placement_status': student.placement_status
    }
    return render(request, 'students/dashboard.html', context)

@login_required
def company_list(request):
    student = request.user.studentprofile
    companies = Company.objects.all()
    
    # Filter companies based on placement status and category
    if student.placement_status == 'placed_twice':
        companies = []
    elif student.placement_status == 'placed':
        # If placed, can only apply to higher categories
        current_company = JobApplication.objects.filter(student=student, status='accepted').first()
        if current_company and current_company.company.category == 'dream':
            companies = []
        elif current_company and current_company.company.category == 'core':
            companies = companies.filter(category='dream')
        elif current_company and current_company.company.category == 'mass':
            companies = companies.filter(category__in=['core', 'dream'])
    
    context = {
        'companies': companies,
        'student': student
    }
    return render(request, 'students/company_list.html', context)

@login_required
def apply_company(request, pk):
    student = request.user.studentprofile
    company = get_object_or_404(Company, pk=pk)
    
    # Check eligibility
    if student.placement_status == 'placed_twice':
        messages.error(request, 'You cannot apply as you are already placed in two companies.')
        return redirect('students:company_list')
    
    # Check if already applied
    if JobApplication.objects.filter(student=student, company=company).exists():
        messages.error(request, 'You have already applied to this company.')
        return redirect('students:company_list')
    
    # Create application
    JobApplication.objects.create(
        student=student,
        company=company,
        status='pending'
    )
    messages.success(request, f'Successfully applied to {company.name}')
    return redirect('students:application_list')

@login_required
def application_list(request):
    applications = JobApplication.objects.filter(student=request.user.studentprofile)
    return render(request, 'students/application_list.html', {'applications': applications})

@login_required
def off_campus_list(request):
    applications = OffCampusApplication.objects.filter(student=request.user.studentprofile)
    return render(request, 'students/off_campus_list.html', {'applications': applications})

@login_required
def add_off_campus(request):
    if request.method == 'POST':
        # Add off-campus application logic
        company_name = request.POST.get('company_name')
        role = request.POST.get('role')
        status = request.POST.get('status')
        
        OffCampusApplication.objects.create(
            student=request.user.studentprofile,
            company_name=company_name,
            role=role,
            status=status
        )
        messages.success(request, 'Off-campus application added successfully!')
        return redirect('students:off_campus_list')
    return render(request, 'students/add_off_campus.html')

@login_required
def policy_page(request):
    return render(request, 'students/policy.html')

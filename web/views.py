from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


from web.models import *

from job.models import *

from product.models import *

from main.functions import generate_form_errors


from users.models import JobCreator

from django.shortcuts import redirect

from .forms import *

from django.core.paginator import Paginator



def index(request):
    job_list = JobPosting.objects.all()
    skills = Skill.objects.all()

    employment_type = request.GET.get('employment_type')
    is_remote = request.GET.get('is_remote')
    skills_required = request.GET.getlist('skills_required')

    if employment_type:
        job_list = job_list.filter(employment_type=employment_type)
    
    if is_remote:
        job_list = job_list.filter(is_remote=True)

    if skills_required:
        job_list = job_list.filter(skills_required__in=skills_required).distinct()


    context= {
        'job_list': job_list,
        'skills': skills
    }
    return render(request, 'web/index.html', context=context)


def jamal(request):
    return render(request, 'web/jamal.html')




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password

        )

        user.save()


        job_creator = JobCreator.objects.create(
            user=user,
        )

        job_creator.save()

        return HttpResponseRedirect(reverse('web:login'))
    else:
        return render(request, 'web/register.html')



def login(request):
    error_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            
            error_message = 'Invalid name or pass.'
    
    return render(request, 'web/login.html', {'error_message': error_message})

    

def logout(request):
    auth_logout(request)

    return HttpResponseRedirect(reverse('web:login'))





# @login_required(login_url='/login')
# def item_done(request, id):
#     item = Task.objects.get(id=id, is_complete=False)
#     item.is_complete = True
#     item.save()
    
#     return HttpResponseRedirect(reverse('web:index'))


# @login_required(login_url='/login')
# def delete_item(request, id):
#     item = Task.objects.get(id=id)
#     item.delete()
#     return HttpResponseRedirect(reverse('web:index'))



@login_required(login_url='/login')
def create_job_posting(request):
    user = request.user
    # Get the job creator associated with the current user
    job_creator = get_object_or_404(JobCreator, user=user)

    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job_posting = form.save(commit=False)  # Don't save to the database yet
            job_posting.job_creator = job_creator  # Assign the job_creator to the posting
            job_posting.save()  # Now save the job posting with the job creator
            return redirect('web:your_job_list')  # Redirect after successful form submission
    else:
        form = JobPostingForm()

    context = {
        'form': form
    }
    
    return render(request, 'form/job_posting_form.html', context=context)



@login_required(login_url='/login')
def job_posting_list(request):
    job_list = JobPosting.objects.all()
    skills = Skill.objects.all()

    employment_type = request.GET.get('employment_type')
    is_remote = request.GET.get('is_remote')
    skills_required = request.GET.getlist('skills_required')

    if employment_type:
        job_list = job_list.filter(employment_type=employment_type)
    
    if is_remote:
        job_list = job_list.filter(is_remote=True)

    if skills_required:
        job_list = job_list.filter(skills_required__in=skills_required).distinct()


    context= {
        'job_list': job_list,
        'skills': skills
    }

    return render(request, 'form/job_posting_list.html', context=context)





# View to show the details of a single company
@login_required(login_url='/login')
def job_detail(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    context = {
        'job': job,
    }
    return render(request, 'form/job_detail.html', context)




@login_required(login_url='/login')
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)  # Handles file uploads like the logo
        if form.is_valid():
            form.save()
            return redirect('web:company_list')  # Redirect to a company listing or another appropriate page
    else:
        form = CompanyForm()
    
    return render(request, 'form/company_form.html', {'form': form})






# View to list all companies
@login_required(login_url='/login')
def company_list(request):
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }
    return render(request, 'form/company_list.html', context)


# View to show the details of a single company
@login_required(login_url='/login')
def company_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    context = {
        'company': company,
    }
    return render(request, 'form/company_detail.html', context)





@login_required(login_url='/login')
def add_or_edit_company(request, company_id=None):
    if company_id:
        company = get_object_or_404(Company, id=company_id)
        form_action = "Edit Company"
    else:
        company = None
        form_action = "Add Company"
        
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')  # Adjust the redirect target as necessary
    else:
        form = CompanyForm(instance=company)

    return render(request, 'company/company_form.html', {
        'form': form,
        'form_action': form_action
    })





def apply_for_job(request, job_id):
    job = JobPosting.objects.get(id=job_id)

    if request.method == 'POST':
        form = WorkerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            worker_profile = form.save(commit=False)
            worker_profile.applied_job = job  # Link the worker to the job posting
            worker_profile.save()
            return redirect('web:job_success_page')  # Redirect to a success page after form submission
        else:
            message = generate_form_errors(form)
            form = WorkerProfileForm()
            context ={
                "error": True,
                "message": message,
                "form": form,
            }
            return render(request, 'form/job_apply.html', context=context)


    else:
        form = WorkerProfileForm()

    return render(request, 'form/job_apply.html', {'form': form, 'job': job})




def job_success_page(request):

    return render(request, 'form/job_success_page.html')



def your_job_list(request):
    user = request.user
    # If there's only one JobCreator per user, use `.get()`
    job_creator = get_object_or_404(JobCreator, user=user)
    
    # Filter job postings based on the specific job_creator
    jobs = JobPosting.objects.filter(job_creator=job_creator)

    context = {
        'job_creator': job_creator,
        'jobs': jobs,
    }
    
    return render(request, 'form/your_job_list.html', context=context)


def worker_profile_list(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    worker_profiles = WorkerProfile.objects.filter(applied_job=job)
    
    context = {
        'job': job,
        'worker_profiles': worker_profiles,
    }
    
    return render(request, 'form/worker_profile_list.html', context)




def worker_profile_detail(request, profile_id):
    worker_profile = get_object_or_404(WorkerProfile, id=profile_id)
    
    context = {
        'worker_profile': worker_profile,
    }
    
    return render(request, 'form/worker_profile_detail.html', context=context)





def applied_job_list(request):
    user = request.user
    # If there's only one JobCreator per user, use `.get()`
    job_creator = get_object_or_404(JobCreator, user=user)
    
    # Filter job postings based on the specific job_creator
    jobs = WorkerProfile.objects.filter(job_creator=job_creator)

    context = {
        'job_creator': job_creator,
        'jobs': jobs,
    }
    
    return render(request, 'form/your_applied_job_list.html', context=context)
























def product_filter(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    size_filter = request.GET.get('size', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    sort_option = request.GET.get('sort', '')

    products = Product.objects.all()
    
    if search_query:
        products = products.filter(name__icontains=search_query)

    if category_id:
        products = products.filter(category_id=category_id)

    if size_filter:
        products = products.filter(size=size_filter)

    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)


    
    if sort_option == 'low_to_high':
        products = products.order_by('price')
    elif sort_option == 'high_to_low':
        products = products.order_by('-price')
    elif sort_option == 'latest':
        products = products.order_by('-created_at')
    else:
        products = products.order_by('-id')



    categories = Category.objects.all()
    available_sizes = Product.objects.values_list('size', flat=True).distinct()

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'categories': categories,
        'available_sizes': available_sizes,
        'search_query': search_query,
        'selected_category': category_id,
        'selected_size': size_filter,
        'min_price': min_price,
        'max_price': max_price,
        'sort': sort_option,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj
    }

    return render(request, 'form/product_filter.html', context)


def filter(request):
    products = Product.objects.all()
    search_query = request.GET.get('search', '')

    if search_query:
        products = products.filter(name__icontains=search_query)

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'products': products,
        'products': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
        'search_query': search_query,
    }

    return render(request, 'form/filter.html', context=context)







def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'form/product_detail.html', {'product': product})
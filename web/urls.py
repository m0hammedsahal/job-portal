from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("jamal/", views.jamal, name="jamal"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    
    # path('delete/<int:id>/', views.delete_item, name='delete_item'),
    # path('done/<int:id>/', views.item_done, name='item_done'),
    path('job-posting/create/', views.create_job_posting, name='job_posting_create'),
    path('job-postings/', views.job_posting_list, name='job_posting_list'),
    path('job-detail/<int:job_id>/', views.job_detail, name='job_detail'),

    path('company/create/', views.create_company, name='create_company'),
    path('company-postings/', views.company_list, name='company_list'),

    path('companies/', views.company_list, name='company_list'), 
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),

    path('company/edit/<int:company_id>/', views.job_success_page, name='edit_company'),
    
    path('success', views.job_success_page, name='job_success_page'),

    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),

    path('your-job-list', views.your_job_list, name='your_job_list'),

    path('job/<int:job_id>/worker_profiles/', views.worker_profile_list, name='worker_profile_list'),

    path('worker_profile/<int:profile_id>/', views.worker_profile_detail, name='worker_profile_detail'),

    path('applied-job-list>/', views.applied_job_list, name='applied_job_list'),

    # pro
    path('product-filter', views.product_filter, name='product_filter'),
    path('filter', views.filter, name='filter'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    
]
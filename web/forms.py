
from django import forms
from .models import JobPosting, Skill, Company, WorkerProfile

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['title', 'company', 'location', 'salary', 'description', 'responsibilities', 'requirements', 'employment_type', 'is_remote', 'skills_required', 'apply_link']
        widgets = {
            "title": forms.TextInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2', "placeholder": "Title"}),
            "company": forms.Select(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2', "placeholder": "Company"}),
            "location": forms.TextInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2', "placeholder": "Location"}),
            "salary": forms.TextInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2', "placeholder": "Salary"}),
            "description": forms.Textarea(attrs={
                'class': 'w-full border-gray-300 border-[1px] rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'rows': 4, 
                'cols': 100  }),
            "responsibilities": forms.Textarea(attrs={
                'class': 'w-full border-gray-300 border-[1px] rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'rows': 4, 
                'cols': 100  }),
            "requirements": forms.Textarea(attrs={
                'class': 'w-full border-gray-300 border-[1px] rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2',
                'rows': 4, 
                'cols': 100  }),
            "apply_link": forms.TextInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2', "placeholder": "Apply Link"}),

            'is_remote': forms.CheckboxInput(attrs={"class": ""}),
            'skills_required': forms.CheckboxSelectMultiple,  # Displays skills as checkboxes
            'employment_type': forms.RadioSelect,  # Displays employment type as radio buttons
        }



class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website', 'email', 'phone_number', 'address', 'city', 'state', 'country', 'postal_code', 'description', 'logo', 'industry', 'founded_year', 'employee_count', 'revenue']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2', 'placeholder': 'Company Name'}),
            'website': forms.URLInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2', 'placeholder': 'Company Website'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2', 'placeholder': 'Company Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2', 'placeholder': 'Phone Number'}),
            'address': forms.Textarea(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2', 'rows': 3, 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2', 'placeholder': 'State'}),
            'country': forms.TextInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2', 'placeholder': 'Country'}),
            'postal_code': forms.TextInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2', 'placeholder': 'Postal Code'}),
            'description': forms.Textarea(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2', 'rows': 4, 'placeholder': 'Company Description'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'w-full border-[1px] border-gray-300 rounded-lg p-2'}),
            
            'industry': forms.TextInput(attrs={'class': 'w-full border-gray-300 border-[1px] rounded-lg shadow-sm p-2', 'placeholder': 'Industry'}),
            'founded_year': forms.NumberInput(attrs={'class': 'w-full border-gray-300 border-[1px] rounded-lg shadow-sm p-2', 'placeholder': 'Founded Year'}),
            'employee_count': forms.NumberInput(attrs={'class': 'w-full border-gray-300 border-[1px] rounded-lg shadow-sm p-2', 'placeholder': 'Employee Count'}),
            'revenue': forms.TextInput(attrs={'class': 'w-full border-gray-300 border-[1px] rounded-lg shadow-sm p-2', 'placeholder': 'Revenue'}),
        }





class WorkerProfileForm(forms.ModelForm):
    class Meta:
        model = WorkerProfile
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'address',
            'highest_education', 'institution_name', 'graduation_year',
            'current_job_title', 'company_name', 'experience_years',
            'skills', 'resume'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'placeholder': 'Phone'}),
            'address': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'rows': 3, 'placeholder': 'Address'}),
            'highest_education': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'placeholder': 'Highest Education'}),
            'institution_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'placeholder': 'Institution Name'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'placeholder': 'Graduation Year'}),
            'current_job_title': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'placeholder': 'Current Job Title'}),
            'company_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'placeholder': 'Company Name'}),
            'experience_years': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'placeholder': 'Years of Experience'}),
            'skills': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg', 'rows': 3, 'placeholder': 'Skills (comma-separated)'}),
            'resume': forms.FileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg'}),
        }

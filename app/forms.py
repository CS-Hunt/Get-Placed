from django import forms
from .models import Placement_Company_Detail,Profile,StudentBlogModel
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from allauth.account.forms import LoginForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class Job_Post_Form(forms.ModelForm):
    class Meta:
        model = Placement_Company_Detail
        fields = ('title','snippet','author','Company_image','Job_Description','apply_link','job_type')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Job Post'}),
            'apply_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of apply button'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author' : forms.Select(attrs={'class':'form-control','placeholder':"author's name"}),
            'job_type' : forms.Select(attrs={'class':'form-control','placeholder':"Job Type"}),
            'Job_Description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Body of the Blog'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control','placeholder':'Add short detail of job'}),
        }

class Edit_Post_Form(forms.ModelForm):
    class Meta:
        model = Placement_Company_Detail
        fields = ('title','snippet','Company_image','Job_Description','apply_link','job_type')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Job Post'}),
            'apply_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of apply button'}),
            # 'author' : forms.Select(attrs={'class':'form-control','placeholder':"author's name"}),
            'job_type' : forms.Select(attrs={'class':'form-control','placeholder':"Job Type"}),
            'Job_Description' : forms.Textarea(attrs={'class':'form-control','placeholder':'Body of the Blog'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control','placeholder':'Add short detail of job'}),
        }

class Blog_Post_Form(forms.ModelForm):
    class Meta:
        model = StudentBlogModel
        fields = ('title','snippet','author','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog Post'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author' : forms.Select(attrs={'class':'form-control','placeholder':"author's name"}),
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Body of the Blog'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control','placeholder':'Add snippet of Blog'}),
        }

class Edit_Blog_Post_Form(forms.ModelForm):
    class Meta:
        model = StudentBlogModel
        fields = ('title','snippet','author','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog Post'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author' : forms.Select(attrs={'class':'form-control','placeholder':"author's name"}),
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Body of the Blog'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control','placeholder':'Add snippet of Blog'}),
        }


class UserLoginForm(LoginForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))

class ProfilePageView(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ('bio','Gender','Mobile_Number','city','state','profile_pic','twitter_url','instagram_url','linkdin_url','github_url')
        widgets = {
                'bio': forms.Textarea(attrs={'class':'form-control','placeholder':'Write a summary about you...'}),
                # 'profile_pic': forms.ImageField(),
                'Gender': forms.Select(attrs={'class':'form-control'}),
                'Mobile_Number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Mobile number'}),
                'city': forms.TextInput(attrs={'class':'forms-control'}),
                'state': forms.Select(attrs={'class':'form-control'}),
                'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
                'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
                'linkdin_url': forms.TextInput(attrs={'class':'form-control'}),
                'github_url': forms.TextInput(attrs={'class':'form-control'}),
        }

class EditProfileFormPage(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ('bio','Gender','Mobile_Number','city','state','profile_pic','twitter_url','instagram_url','linkdin_url','github_url')
        widgets = {
                'bio': forms.Textarea(attrs={'class':'form-control','placeholder':'Write a summary about you...'}),
                # 'profile_pic': forms.ImageField(),
                'Gender': forms.Select(attrs={'class':'form-control'}),
                'Mobile_Number': forms.TextInput(attrs={'class':'form-control'}),
                'city': forms.TextInput(attrs={'class':'form-control'}),
                'state': forms.Select(attrs={'class':'form-control'}),
                'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
                'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
                'linkdin_url': forms.TextInput(attrs={'class':'form-control'}),
                'github_url': forms.TextInput(attrs={'class':'form-control'}),
        }

class EditProfileForm(UserChangeForm):
    date_joined = forms.CharField(max_length=100,disabled=True)
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"../accounts/password/change/\">this form</a>."))
    class Meta:
        model =User
        fields = ['username','first_name','last_name','email','date_joined']
        labels={
            'first_name' : 'First Name',
            'last_name':'Last Name',
            'email': 'Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'date_joined': forms.TextInput(attrs={'class':'form-control'}),
        }

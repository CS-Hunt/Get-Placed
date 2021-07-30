from django import forms
from .models import Placement_Company_Detail,Profile,StudentBlogModel,ResorcesModel
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
        fields = ('title','author','body','snippet')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog Post'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author' : forms.Select(attrs={'class':'form-control','placeholder':"author's name"}),
            'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Body of the Blog'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control','placeholder':'Add snippet of Blog'}),
        }

class ResorcesModelForm(forms.ModelForm):
    class Meta:
        model = ResorcesModel
        fields = ('title','docs','author','course1_title','course1_Img','course1_link','course2_title','course2_Img','course2_link','course3_title','course3_Img','course3_link','course4_title','course4_Img','course4_link','course5_title','course5_Img','course5_link',
        'channel1_title','channel1_Img','channel1_link','channel2_title','channel2_Img','channel2_link','channel3_title','channel3_Img','channel3_link','channel4_title','channel4_Img','channel4_link','channel5_title','channel5_Img','channel5_link',
        'Website1_title','Website1_Img','Website1_link','Website2_title','Website2_Img','Website2_link','Website3_title','Website3_Img','Website3_link','Website4_title','Website4_Img','Website4_link','Website5_title','Website5_Img','Website5_link',)
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog Post'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author' : forms.Select(attrs={'class':'form-control','placeholder':"author's name"}),
            'docs' : forms.TextInput(attrs={'class':'form-control','placeholder':'Link of documentation'}),
            'course1_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of course 1'}),
            'course1_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of course 1'}),
            'course2_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of course 2'}),
            'course2_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of course 2'}),
            'course3_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of course 3'}),
            'course3_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of course 3'}),
            'course4_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of course 3'}),
            'course4_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of course 3'}),
            'course5_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of course 3'}),
            'course5_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of course 3'}),

            'channel1_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of channel 1'}),
            'channel1_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of channel 1'}),
            'channel2_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of channel 2'}),
            'channel2_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of channel 2'}),
            'channel3_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of channel 3'}),
            'channel3_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of channel 3'}),
            'channel4_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of channel 3'}),
            'channel4_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of channel 3'}),
            'channel5_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of channel 3'}),
            'channel5_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of channel 3'}),

            'Website1_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of Website 1'}),
            'Website1_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of Website 1'}),
            'Website2_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of Website 2'}),
            'Website2_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of Website 2'}),
            'Website3_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of Website 3'}),
            'Website3_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of Website 3'}),
            'Website4_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of Website 3'}),
            'Website4_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of Website 3'}),
            'Website5_title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of Website 3'}),
            'Website5_link' : forms.TextInput(attrs={'class':'form-control','placeholder':'link of Website 3'}),
        }

class Edit_Blog_Post_Form(forms.ModelForm):
    class Meta:
        model = StudentBlogModel
        fields = ('title','snippet','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title of the Blog Post'}),
            # 'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
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

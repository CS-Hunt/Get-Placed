from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Placement_Company_Detail,Profile,StudentBlogModel,ResorcesModel
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from .forms import Job_Post_Form,UserLoginForm,ProfilePageView,EditProfileFormPage,EditProfileForm,Edit_Post_Form,Blog_Post_Form,Edit_Blog_Post_Form,ResorcesModelForm
from allauth.account.views import PasswordChangeView,LoginView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator

class HomeView(ListView):
    model = Placement_Company_Detail
    template_name = 'app/home.html'
    ordering = ['-post_date']
    context_object_name = "Placement_Company_Detail_list"    #default is object_list as well as model's_verbose_name_list and/or model's_verbose_name_plural_list, if defined in the model's inner Meta class
    paginate_by = 10


def AboutView(request):
    return render(request, 'app/About.html')

def TermsAndCondition(request):
    return render(request, 'app/Terms&Condition.html')

def JoinUsView(request):
    return render(request, 'app/join_us.html')

class CompanyDetailView(DetailView):
    model = Placement_Company_Detail
    template_name = 'app/Company_details.html'

    def get_context_data(self,*args,**kwargs):
        context = super(CompanyDetailView, self).get_context_data(*args,**kwargs)

        stuff = get_object_or_404(Placement_Company_Detail, id=self.kwargs['pk'])
        return context

class AddJobView(CreateView):
    model = Placement_Company_Detail
    form_class = Job_Post_Form
    template_name = 'app/add_job_post.html'
    # fields = '__all__'
    # fields = ('title','body')

class UpdateJobPostView(UpdateView):
    model = Placement_Company_Detail
    form_class = Edit_Post_Form
    template_name = 'app/update_job_post.html'
    # fields = ['title','title_tag','body']

class DeleteJobPostView(DeleteView):
    model = Placement_Company_Detail
    template_name = 'app/delete_post.html'
    success_url = reverse_lazy('home')

class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageView
    template_name = 'account/craete_user_profile_page.html'
    # fields = '__all__'
    success_url = reverse_lazy('home')


    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(UpdateView):
    model = Profile
    form_class = EditProfileFormPage
    template_name = 'account/edit_profile_page.html'
    def get_success_url(self):
        return reverse_lazy('show_profile', kwargs={'pk': self.kwargs['pk']})

class ShowProfileView(DetailView):
    model = Profile
    template_name = 'account/user_profile.html'

    def get_context_data(self,*args,**kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args,**kwargs)

        # StudentBlogModel = StudentBlogModel.objects.all()
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        # page_user_post = get_object_or_404(StudentBlogModel, id=self.kwargs['pk'])
        context["page_user"] = page_user
        # context["page_user_post"] = page_user_post
        context['page_user_post'] = StudentBlogModel.objects.filter(author=self.kwargs['pk']).order_by('-post_date')

        return context



class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'account/edit_profile.html'
    success_url = reverse_lazy('home')
    # fields = ['username','first_name','last_name']

    def get_object(self):
        return self.request.user

# Blog views

class BlogView(ListView):
    model = StudentBlogModel
    template_name = 'blog/home.html'
    ordering = ['-post_date']
    context_object_name = "StudentBlogModel_list"    #default is object_list as well as model's_verbose_name_list and/or model's_verbose_name_plural_list, if defined in the model's inner Meta class
    paginate_by = 10
    def get_context_data(self, *args,**kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['page_user'] = Profile.objects.all()
        return context


class BlogDetailView(DetailView):
    model = StudentBlogModel
    template_name = 'blog/Blog_details.html'


class AddBlogView(CreateView):
    model = StudentBlogModel
    form_class = Blog_Post_Form
    template_name = 'blog/add_blog_post.html'

class UpdateBlogPostView(UpdateView):
    model = StudentBlogModel
    form_class = Edit_Blog_Post_Form
    template_name = 'blog/update_blog_post.html'
    # fields = ['title','title_tag','body']


class DeleteblogPostView(DeleteView):
    model = StudentBlogModel
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')

# Resources view

class ResourcesView(ListView):
    model = ResorcesModel
    template_name = 'resources/resources.html'
    ordering = ['title']
    context_object_name = "ResorcesModel_list"    #default is object_list as well as model's_verbose_name_list and/or model's_verbose_name_plural_list, if defined in the model's inner Meta class

class AddResourcesView(CreateView):
    model = ResorcesModel
    form_class = ResorcesModelForm
    template_name = 'resources/add_resources.html'

class ResourcesDetailView(DetailView):
    model = ResorcesModel
    template_name = 'resources/resources_details.html'

def OnCampusView(request):
    data = Placement_Company_Detail.objects.filter(job_type='On-Campus').order_by('-post_date')
    paginator = Paginator(data, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/OnCampusJob.html',context={'page_obj':page_obj})

def OffCampusView(request):
    data = Placement_Company_Detail.objects.filter(job_type='Off-Drive').order_by('-post_date')
    paginator = Paginator(data, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/OffCampusJob.html',context={'page_obj':page_obj})

def Internship(request):
    data = Placement_Company_Detail.objects.filter(job_type='Internship').order_by('-post_date')
    paginator = Paginator(data, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/Internship.html',context={'page_obj':page_obj})

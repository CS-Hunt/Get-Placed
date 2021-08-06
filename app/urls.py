from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .forms import LoginForm
# from djago.allauth.account.views import LoginView

urlpatterns = [
    # path('login/',TemplateView.as_view(template_name="app/account/login.html")),
    path('', views.HomeView.as_view(), name='home'),
    path('Company-Job-Description/<int:pk>/',views.CompanyDetailView.as_view(), name="Job_Description"),
    path('Add_Job_Post/',views.AddJobView.as_view(),name="Add_Job_Post"),
    path('update_job_post/<int:pk>/',views.UpdateJobPostView.as_view(),name='update_job_post'),
    path('delete_post/<int:pk>/remove/',views.DeleteJobPostView.as_view(),name='delete_post'),
    # path('job/',views.JobView.as_view(),name="Job-view"),
    path('on-campus/',views.OnCampusView,name="on-campus"),
    path('off-campus/',views.OffCampusView,name="off-campus"),
    path('Internship/',views.Internship,name="Internship"),

    path('Blog/',views.BlogView.as_view(),name="blog"),
    path('Blog-Article/<int:pk>/',views.BlogDetailView.as_view(), name="Blog_Description"),
    path('Add_Blog_Post/',views.AddBlogView.as_view(),name="Add_Blog_Post"),
    path('update_blog_post/<int:pk>/',views.UpdateBlogPostView.as_view(),name='update_blog_post'),
    path('delete_blog_post/<int:pk>/remove/',views.DeleteblogPostView.as_view(),name='delete_blog_post'),

    path('resources/',views.ResourcesView.as_view(),name="resources"),
    path('resources-detail/<int:pk>/',views.ResourcesDetailView.as_view(), name="resources_detail"),
    path('Add_Resources/',views.AddResourcesView.as_view(),name="Add_resources"),

    path('edit_profile/',views.UserEditView.as_view(), name='user_edit'),
    path('<int:pk>/Profile/',views.ShowProfileView.as_view(),name="show_profile"),
    path('<int:pk>/edit_profile/',views.EditProfilePageView.as_view(),name="edit_profile"),
    path('create_profile/',views.CreateProfilePageView.as_view(),name="create_profile"),

    path('accounts/',include('allauth.urls')),
    path('accounts/login/', views.UserLogin.as_view(),name='account_login'),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
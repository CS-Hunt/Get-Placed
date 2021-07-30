from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

Job_Type = (
    ('Internship','Internship'),
    ('Off-Drive','Off-Drive'),
    ('On-Campus','On-Campus'),
)

class Placement_Company_Detail(models.Model):
    title = models.CharField(max_length=255)
    Company_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Job_Description = RichTextField(blank=True,null=True)
    snippet = models.TextField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)
    job_type = models.CharField(choices=Job_Type,max_length=50)
    apply_link = models.URLField(max_length=128)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
         
STATE_CHOICES=(
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Prasedh','Arunachal Prasedh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman & Diu','Daman & Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telengana','Telengana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
)

GENDER = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)
class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    Mobile_Number = models.CharField(max_length=12)
    Gender = models.CharField(choices=GENDER,max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(choices=STATE_CHOICES,max_length=50)
    twitter_url = models.CharField(max_length=255,null=True, blank=True)
    instagram_url = models.CharField(max_length=255,null=True, blank=True)
    linkdin_url = models.CharField(max_length=255,null=True, blank=True)
    github_url = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        # return reverse("article_detail", args={str(self.id)})      return to self blog
        return reverse("home")


class StudentBlogModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    snippet = models.TextField(max_length=255)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog") 

class ResorcesModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    docs = models.URLField(blank=True,null=True)

    # Best Cources
    course1_title = models.CharField(max_length=255,null=True, blank=True)
    course1_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    course1_link = models.URLField(blank=True,null=True)

    course2_title = models.CharField(max_length=255,null=True, blank=True)
    course2_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    course2_link = models.URLField(blank=True,null=True)

    course3_title = models.CharField(max_length=255,null=True, blank=True)
    course3_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    course3_link = models.URLField(blank=True,null=True)

    course4_title = models.CharField(max_length=255,null=True, blank=True)
    course4_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    course4_link = models.URLField(blank=True,null=True)

    course5_title = models.CharField(max_length=255,null=True, blank=True)
    course5_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    course5_link = models.URLField(blank=True,null=True)

    # Youtube Channels
    channel1_title = models.CharField(max_length=255,null=True, blank=True)
    channel1_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    channel1_link = models.URLField(blank=True,null=True)

    channel2_title = models.CharField(max_length=255,null=True, blank=True)
    channel2_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    channel2_link = models.URLField(blank=True,null=True)

    channel3_title = models.CharField(max_length=255,null=True, blank=True)
    channel3_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    channel3_link = models.URLField(blank=True,null=True)

    channel4_title = models.CharField(max_length=255,null=True, blank=True)
    channel4_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    channel4_link = models.URLField(blank=True,null=True)

    channel5_title = models.CharField(max_length=255,null=True, blank=True)
    channel5_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    channel5_link = models.URLField(blank=True,null=True)

    # Useful Websites
    Website1_title = models.CharField(max_length=255,null=True, blank=True)
    Website1_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    Website1_link = models.URLField(blank=True,null=True)

    Website2_title = models.CharField(max_length=255,null=True, blank=True)
    Website2_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    Website2_link = models.URLField(blank=True,null=True)

    Website3_title = models.CharField(max_length=255,null=True, blank=True)
    Website3_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    Website3_link = models.URLField(blank=True,null=True)

    Website4_title = models.CharField(max_length=255,null=True, blank=True)
    Website4_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    Website4_link = models.URLField(blank=True,null=True)

    Website5_title = models.CharField(max_length=255,null=True, blank=True)
    Website5_Img = models.ImageField(null=True, blank=True, upload_to="resources/")
    Website5_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
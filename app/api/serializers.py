from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

from app.models import ResorcesModel,Placement_Company_Detail

class ResorcesSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id', write_only=True)
    class Meta:
        model = ResorcesModel
        fields = ('id','title','author','docs','course1_title','course1_Img','course1_link','course2_title','course2_Img','course2_link','course3_title','course3_Img','course3_link','course4_title','course4_Img','course4_link','course5_title','course5_Img','course5_link',
        'channel1_title','channel1_Img','channel1_link','channel2_title','channel2_Img','channel2_link','channel3_title','channel3_Img','channel3_link','channel4_title','channel4_Img','channel4_link','channel5_title','channel5_Img','channel5_link',
        'Website1_title','Website1_Img','Website1_link','Website2_title','Website2_Img','Website2_link','Website3_title','Website3_Img','Website3_link','Website4_title','Website4_Img','Website4_link','Website5_title','Website5_Img','Website5_link',)
    
    # Get the current user from request context
    def validate_author(self, value):
        return self.context['request'].user
        
class Placement_Company_DetailAPI(ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id', write_only=True)
    class Meta:
        model = Placement_Company_Detail
        fields = ('id','title','snippet','author','Company_image','Job_Description','apply_link','job_type')
    
    # Get the current user from request context
    def validate_author(self, value):
        return self.context['request'].user
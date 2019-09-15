from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.


class Profile(models.Model):
    avatar = models.ImageField(upload_to='images/', blank=True)
    contact = HTMLField()
    email = models.EmailField(max_length=70, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    objects = models.Manager()

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls, search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    class Meta:
        ordering = ['user']


class Neighborhood(models.Model):
    locality = models.CharField(
        max_length=30, default="e.g Aries, Sagittarius, Leo")
    name = models.CharField(max_length=30)
    occupants_count = models.IntegerField(default=0, blank=True)
    # profile=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='hoods', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()

    @classmethod
    def search_neighborhood_by_name(cls, search_term):
        neighborhoods = cls.objects.filter(name__icontains=search_term)
        return neighborhoods

    @classmethod
    def one_neighborhood(cls, id):
        neighborhood = Neighborhood.objects.filter(id=id)
        return neighborhood

    @classmethod
    def all_neighborhoods(cls):
        neighborhoods = cls.objects.all()
        return neighborhoods



    @classmethod
    def get_neighborhood_by_id(cls, id):
        neighborhood = Neighborhood.objects.filter(id=Neighborhood.id)
        return neighborhood

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile


class Business(models.Model):
    name = models.CharField(max_length=30)
    description = HTMLField(blank=True)
    email = models.EmailField(max_length=70, blank=True)
    biz_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    biz_hood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, related_name='biz', null=True)

    '''
    this is added to ensure the linter has no errors saying class has no objects member in VS Code IDE
    '''
    objects = models.Manager()

    @classmethod
    def search_by_name(cls, search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

    @classmethod
    def get_neighborhood_businesses(cls, neighborhood_id):
        businesses = Business.objects.filter(neighborhood_id=id)
        return businesses

    @classmethod
    def get_hood_biz(cls, biz_hood):
        businesses = Business.objects.filter(biz_hood_pk=biz_hood)
        return businesses

    @classmethod
    def get_profile_businesses(cls, profile):
        businesses = Business.objects.filter(biz_owner__pk=profile)
        return businesses


class Join(models.Model):
    user_id = models.OneToOneField(User)
    hood_id = models.ForeignKey(Neighborhood)

    def __str__(self):
        return self.user_id


class Post(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', blank=True)
    description = HTMLField(blank=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_hood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    
    objects = models.Manager()

    @classmethod
    def search_post(cls, search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts

    @classmethod
    def get_hood_posts(cls, post_hood):
        posts = Post.objects.filter(post_hood=id)
        return posts

    @classmethod
    def search_by_name(cls, search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts

    @classmethod
    def all_posts(cls,id):
        posts = Post.objects.all()
        return posts

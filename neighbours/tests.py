from django.test import TestCase
from .models import *

# Create your tests here.


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Freya')
        self.profile = Profile.objects.create(
            user=self.user, email='jan@gmail.com', contact='contact')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_get_all_profiles(self):
        self.profile.save()
        profile = Profile.get_all_profiles()
        self.assertTrue(len(profile) > 0)

    def test_find_profile(self):
        self.profile.save()
        profile = Profile.find_profile('Freya')
        self.assertTrue(len(profile) > 0)


class NeighborhoodTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Freya')
        self.profile = Profile.objects.create(
            user=self.user, email='jan@gmail.com', contact='contact')

        self.hood = Neighborhood.objects.create(locality='locality', user_profile=self.user,
                                                name='firenatio', occupants_count=50)

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighborhood))

    def test_all_hoods(self):
        self.hood.save()
        hood = Neighborhood.all_neighborhoods()
        self.assertTrue(len(hood) > 0)


class BusinessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Freya')
        self.profile = Profile.objects.create(
            user=self.user, email='jan@gmail.com', contact='contact')

        self.biz = Business.objects.create(name='cbd',
                                           description='available and reliable', email='jan@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.biz, Business))

    def test_get_neighborhood_businesses(self):
        self.biz.save()
        biz = Business.get_neighborhood_businesses(biz_hood)
        self.assertTrue(len(biz) > 0)

    def test_search_biz(self):
        self.biz.save()
        biz = Business.search_by_name('cbd')
        self.assertTrue(len(biz) > 0)


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Freya')
        self.profile = Profile.objects.create(
            user=self.user, email='jan@gmail.com', contact='contact')

        self.post = Post.objects.create(name='sampleText',
                                        image='images/', description='desc')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_all_posts(self):
        self.post.save()
        post = Post.all_posts(id)
        self.assertTrue(len(post) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_by_name('sampleText')
        self.assertTrue(len(post) > 0)



from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from .utils import get_random_word
from django.template.defaultfilters import slugify
from django.db.models import Q
# Create your models here.
class ProfileManager(models.Manager):
    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Connection.objects.filter(Q(sender=profile) | Q(receiver=profile))
        print(qs)
        print("#########")

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)
        print("#########")

        available = [profile for profile in profiles if profile not in accepted]
        print(available)
        print("#########")
        return available
        

    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles

class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio here...", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    connections = models.ManyToManyField(User, blank=True, related_name='connections')
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()

    def get_connections(self):
        return self.connections.all()
    
    def get_connections_num(self):
        return self.connections.all().count()

    def get_posts_num(self):
        return self.posts.all().count()

    def fetch_all_author_posts(self):
        return self.posts.all()
    
    def get_absolute_url(self):
        return reverse("profiles:profile-detail-view", kwargs={"slug":self.slug})

    def get_likes_given_num(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value=='Like':
                total_liked += 1
        return total_liked

    def get_likes_received_num(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.liked.all().count()
        return total_liked


    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"
    
    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_first_name = self.first_name
        self.__initial_last_name = self.last_name
        

    def save(self, *args, **kwargs):
        x = False
        to_slug = self.slug
        if self.first_name != self.__initial_first_name or self.last_name != self.__initial_last_name or self.slug == '':
            if self.first_name and self.last_name:
                newSlug = slugify(str(self.first_name) + ' ' + str(self.last_name))
                x = Profile.objects.filter(slug=newSlug).exists()
                while x:
                    newSlug = slugify(newSlug + " " + str(get_random_word()))
                    x = Profile.objects.filter(slug=newSlug).exists()
            else:
                newSlug = str(self.user)
        self.slug = newSlug
        super().save(*args, **kwargs)

STATUS_CHOICES = (('send', 'send'),
                  ('accepted', 'accepted')
)

class ConnectionManager(models.Manager):
    def invatations_received(self, receiver):
        qs = Connection.objects.filter(receiver=receiver, status='send')
        return qs

class Connection(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ConnectionManager()

    def __str__(self) -> str:
        return f"{self.sender}-{self.receiver}-{self.status}"
# ./feedpage/models.py
from django.db import models
from django.utils import timezone # 장고는 created_at과 updated_at을 알아서 만들어 주지 않음. id는 만들어 줌
from django.contrib.auth.models import User   # 추가
from django.db.models.signals import post_save  # 추가
from django.dispatch import receiver   # 추가
# Create your models here.
class Feed(models.Model): # 모델 클래스명은 단수형을 사용 (Feeds(x) Feed(O))
    # id는 자동 추가
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, null=True, on_delete= models.CASCADE)    
    liked_users = models.ManyToManyField(User, blank=True, related_name='feeds_liked', through='Like')

    def update_date(self): # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):   # 추가
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    follows = models.ManyToManyField('self', through = 'Follow', blank=True, related_name = 'followed', symmetrical=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()


class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model): 
    follow_to = models.ForeignKey(Profile, related_name = 'follow_to', on_delete=models.CASCADE)
    follow_from = models.ForeignKey(Profile, related_name = 'follow_from', on_delete=models.CASCADE)

    def __str__(self):
        return '{} follows {}'.format(self.follow_from, self.follow_to)
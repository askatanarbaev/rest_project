from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.CharField(max_length=350, blank=True)
    profile_avatar = models.ImageField(upload_to='AvatorPicture/', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class PostImage(models.Model):
    image = models.ImageField(upload_to='postgram/')
    image_description = models.TextField(blank=True)
    image_likes = models.ManyToManyField('Profile', default=False, blank=True, related_name='likes')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create_image')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='update_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_description


class Comments(models.Model):
    comment_post = models.CharField(max_length=300)
    author_comment = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='author_comment')
    comment_image = models.ForeignKey('PostImage', on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment_post} by {self.author_comment}'







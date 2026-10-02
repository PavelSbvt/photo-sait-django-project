# from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# class Location(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts_images/')
    # location = models.ForeignKey(Location, related_name='photos')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


# class PostImage(models.Model):
#     post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='posts_images/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Image for {self.post.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
#
# class PostImage(models.Model):
#     post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='posts_images/', null=True, blank=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Image for {self.post.title}"


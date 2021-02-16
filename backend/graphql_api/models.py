from django.db import models


class User(models.Model):
    name = models.CharField(max_length=250)
    followers = models.ManyToManyField('graphql_api.User')

class Post(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
from django.db import models

from django.db import models

from django.contrib.auth.models import AbstractUser
# social_app/models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)



class Connection(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connections')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connected_to')


class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    visibility_choices = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('connections', 'Connections Only')
    ]
    visibility = models.CharField(max_length=20, choices=visibility_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


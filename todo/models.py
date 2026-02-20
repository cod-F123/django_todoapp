from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    do_it_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title
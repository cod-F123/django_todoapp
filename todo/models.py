from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

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
    
    
    def save(self, *args, **kwargs):
        
        if self.is_completed == True and self.do_it_at is None:
            self.do_it_at = timezone.now()
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser

class PageView(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    page_url = models.URLField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Page View: {self.page_url}"

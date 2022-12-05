from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Snack (models.Model):
    title  = models.CharField(max_length=255, help_text="the title of the snack ", default="Title")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default="description ")
    image = models.TextField(default= "no image provided")
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "my things"   
        ordering=['-pk']

    def get_absolute_url(self):
        return reverse('Snack_Detail',args=[self.id])
   
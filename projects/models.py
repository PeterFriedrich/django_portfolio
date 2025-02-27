from django.db import models

# Create your models here.
class Project(models.Model):
    # model for projects
    title = models.CharField(max_length=100) # short strings
    description = models.TextField() # longer strings
    technology = models.CharField(max_length=20)


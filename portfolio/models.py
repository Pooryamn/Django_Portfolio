from django.db import models

# Create your models here.
class Project(models.Model):
    # Property
    # in my web site, a project have a Title,Description,Image,Url
    Title = models.CharField(max_length=100) #maximum characters = 100
    Description = models.CharField(max_length=300)
    Image = models.ImageField(upload_to='portfolio/images/') # image will upload to this directory
    Url = models.URLField(blank=True)# balnk=True means the field will not be required


    def __str__(self):
        return self.Title

    
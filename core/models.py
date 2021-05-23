from django.db import models

class PortfolioApp(models.Model):
    title = models.CharField(max_length=50)
    img = models.FileField()
    github_link = models.URLField()
    url = models.URLField()
    description = models.TextField()
    photos = models.ManyToManyField('Photos')

    def __str__(self):
        return self.title
        
class Photos(models.Model):
    photo = models.FileField()

    class Meta:
        verbose_name_plural = 'Photos'

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Messages'
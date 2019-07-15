from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 20) 
    image = models.FileField(upload_to='images/')
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title
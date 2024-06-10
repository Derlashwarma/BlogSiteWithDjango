from django.db import models
from django.utils import timezone

class Blog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.edited_at = timezone.now()
        self.save()

    def short_description(self):
        short_desc = self.description.split()
        if len(short_desc) > 50:
            return ''.join(short_desc) + '...'
        else:
            return self.description
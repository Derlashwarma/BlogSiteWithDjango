from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.save()

    def short_description(self):
        short_desc = self.description.split()

        if len(short_desc) > 50:
            return ''.join(short_desc) + '...'
        else:
            return self.description
        
    


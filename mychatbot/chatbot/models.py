from django.db import models

from django.db import models

class ImageModel(models.Model):
    keywords = models.CharField(max_length=255)  # Store keywords associated with the image
    image = models.ImageField(upload_to='images/')  # Store the image file itself


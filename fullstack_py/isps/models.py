from django.db import models

# Create your models here.

class Provider:
    name = models.CharField(max_length=200, null=False, blank=False, default=None)
    lowest_price = models.FloatField(null=True, blank=True, default=0.0)
    # rating = 

# providers[7] —> { name, lowest_price, rating, max_speed, description, contact_no, email, image, url }
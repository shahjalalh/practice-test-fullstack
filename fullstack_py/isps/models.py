from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Provider:

    def user_directory_path(self, instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)

    name = models.CharField(max_length=200, null=False, blank=False, default=None)
    lowest_price = models.FloatField(null=True, blank=True, default=0.0)
    rating = GenericRelation(Rating, related_query_name="foos")
    max_speed = models.CharField(max_length=100, null=False, blank=False, default=None)
    description = models.TextField()
    contact_no = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=254)
    image = models.ImageField(upload_to=user_directory_path)
    url = models.URLField(max_length=254)

    def __str__(self):
        return self.name

# providers[7] —> { name, lowest_price, rating, max_speed, description, contact_no, email, image, url }
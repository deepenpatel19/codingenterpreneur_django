from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
# Create your models here.
from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL


class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User)  # Django models unleashed joincfe.com
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving...')
    print(instance.timestamp)
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
    print('saved.')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()


pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)

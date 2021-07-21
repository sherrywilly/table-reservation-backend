from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name="Location name")
    desc = models.TextField(blank=True, null=True, verbose_name="description")

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("locupdate", kwargs={'pk': self.pk})


class RestCategory(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("restcatupdate", kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse("", kwargs={"pk": self.pk})


class Restaurant(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10,10}$', message="Phone must be in the format: '+999999999'.Please enter 10 digits mobile number.")
    name = models.CharField(max_length=100, verbose_name="Restaurant name")
    description = models.TextField()
    address = models.TextField()
    phone = models.CharField(validators=[phone_regex], max_length=10)
    categorys = models.ManyToManyField(RestCategory)
    # lat = models.FloatField()
    # log = models.FloatField()
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.BooleanField(default=False)
    opentime = models.TimeField()
    closstime = models.TimeField()
    seatingCapacity = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to='rest/', blank=True, null=True)
    # logo and pics for the restaurent is needed here

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Restaurant, self).save(*args, **kwargs)

    def get_logo(self):
        try:
            url = self.logo.url
        except:
            url = ''

        return url

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("restaurantupdate", kwargs={'pk': self.pk})

    def get_detail_url(self):
        return reverse("rester", kwargs={'slug': self.slug})

    def activate_url(self):
        return reverse('rest-activate', kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50)
    shop = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_data(self):
        return 0

    def get_update_url(self):
        return reverse("catupdate", kwargs={'pk': self.pk, 'slug': self.shop.slug})

    def get_rest_update_url(self):
        return reverse('cat-update-rest', kwargs={'pk': self.pk})

    # def get_absolute_url(self):
    #     return reverse("", kwargs={"pk": self.pk})
    # @property
    # def get_items(self):
    #     _y = []
    #     _x = self.item_set.all()
    #     for i in _x:
    #         _y.append(i)

    #     return _y


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='items', blank=True, null=True)
    # image fierld required
    img = models.ImageField(upload_to='item/', blank=True,
                            null=True, verbose_name="Image")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_img(self):
        try:
            url = self.img.url
        except:
            url = ''

        return url

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("", kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse("", kwargs={"pk": self.pk})

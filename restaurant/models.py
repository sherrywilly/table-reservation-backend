from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.


class RestCategory(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("restcatupdate", kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse("", kwargs={"pk": self.pk})


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=12)
    categorys = models.ManyToManyField(RestCategory)
    lat = models.FloatField()
    log = models.FloatField()
    status = models.BooleanField(default=False)
    opentime = models.TimeField()
    closstime = models.TimeField()
    seatingCapacity = models.IntegerField()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to='rest/')
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


class Category(models.Model):
    name = models.CharField(max_length=50)
    shop = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("catupdate", kwargs={'pk': self.pk, 'slug': self.shop.slug})

    # def get_absolute_url(self):
    #     return reverse("", kwargs={"pk": self.pk})

    def get_items(self):
        _x = self.item_set.all()
        return _x


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    # image fierld required
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("", kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse("", kwargs={"pk": self.pk})

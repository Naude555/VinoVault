from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from django.utils import timezone


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Variety(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def default_date_received():
    return timezone.now().date()


def default_date_to_drink_start():
    return timezone.now().date()


def default_date_to_drink_end():
    return timezone.now().date() + timezone.timedelta(days=5 * 365)


class Wine(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    year = models.IntegerField()
    quantity = models.PositiveIntegerField()
    received_from = models.CharField(max_length=100, null=True, blank=True)
    date_received = models.DateField(
        default=default_date_received, blank=True, null=True
    )
    date_to_drink_start = models.DateField(
        default=default_date_to_drink_start, blank=True, null=True
    )
    date_to_drink_end = models.DateField(
        default=default_date_to_drink_end, blank=True, null=True
    )

    # Add more fields as needed

    def is_ready_to_drink(self):
        today = timezone.now().date()
        return self.date_to_drink_start <= today <= self.date_to_drink_end

    def is_getting_old(self):
        today = timezone.now().date()
        return self.date_to_drink_end <= today

    def get_absolute_url(self):
        return reverse("vinventory:wine_list")

    def __str__(self):
        return self.name

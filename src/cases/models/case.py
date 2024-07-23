from django.db import models

from ingatlan.base import Base


class Gallery(Base):
    case = models.ForeignKey('Case', on_delete=models.CASCADE, related_name='galleries')
    url = models.URLField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'


class Case(Base):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    province = models.CharField(max_length=255, null=False, blank=False)
    zip_code = models.CharField(max_length=10, null=False, blank=False)
    status = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)
    size = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    rooms = models.IntegerField(null=False, blank=False)
    bathrooms = models.IntegerField(null=False, blank=False)
    garages = models.IntegerField(null=False, blank=False)
    floors = models.IntegerField(null=False, blank=False)
    year_built = models.IntegerField(null=False, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'

    def __str__(self):
        return self.title

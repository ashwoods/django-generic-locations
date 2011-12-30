from django.contrib.gis.db import models
from django.contrib.contenttypes.models import ContentType
from django_countries import CountryField
from django.contrib.contenttypes import generic


class GenericLocation(models.Model):
    """Intermediary model for storing location data"""

    address           = models.CharField(max_length=100, blank=True, null=True, help_text="Street & street number")
    address_extra     = models.CharField(max_length=100, blank=True, null=True, help_text="Street extra line")
    city              = models.CharField(max_length=50, blank=True, null=True, help_text="i.e. New York, Paris, London")
    state_or_province = models.CharField(max_length=50, blank=True, null=True, help_text="US states i.e. TX, NY or EU provinces")
    country           = CountryField(null=True, blank=True)
    zipcode           = models.CharField(max_length=10, blank=True, null=True)

    computed_address  = models.CharField(max_length=100, null=True, blank=True, help_text="Do not edit manually, geocoder computed address")

    position          = models.PointField(srid=4326, spatial_index=True, geography=True, null=True, blank=True, help_text="Longitud (x) Latitude (y)")

    content_type      = models.ForeignKey(ContentType, blank=True, null=True, related_name="content_type")
    object_id         = models.PositiveIntegerField(blank=True, null=True)
    content_object    = generic.GenericForeignKey("content_type", "object_id")

    # needed to be able to make spatial computations
    objects = models.GeoManager()



    def __unicode__(self):
            return self.formatted_address()

    class Meta:
        unique_together = ('content_type', 'object_id')


    @property
    def lat_str(self):
        return "%.18f" % self.position.y

    @property
    def lng_str(self):
        return "%.18f" % self.position.x


    def formatted_address(self):
        return "%s %s %s" % (self.address, self.city, self.country)

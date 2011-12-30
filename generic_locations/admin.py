from django.conf import settings
from django.contrib.contenttypes import generic

from models import GenericLocation
from widgets import GoogleMapsPointWidget
from django.forms import ModelForm

class GenericLocationForm(ModelForm):
    class Meta:
        model = GenericLocation
        fields = ('address',
                  'address_extra',
                  'city',
                  'state_or_province',
                  'country',
                  'zipcode',
                  'computed_address',
                  'position',
            )
        widgets = {
            'position': GoogleMapsPointWidget(),
       }

class LocationInline(generic.GenericStackedInline):
    model = GenericLocation
    form  = GenericLocationForm
    extra = 1
    max_num=1
    classes = ('collapse open',)

    class Media:
        js = [
            'http://maps.google.com/maps/api/js?sensor=false',
            settings.STATIC_URL + '/js/jquery.livequery.min.js',
            settings.STATIC_URL +'/js/jq.generic.location.admin.js',

       ]

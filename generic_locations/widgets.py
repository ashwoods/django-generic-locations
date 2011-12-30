from django.forms.widgets import MultiWidget, TextInput
from django.contrib.gis.geos import Point


class GoogleMapsPointWidget(MultiWidget):
    """A double text input and google maps Widget for PointFields"""

    def __init__(self, attrs=None):
        widgets = (TextInput(attrs=attrs),TextInput(attrs=attrs))
        super(GoogleMapsPointWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            print value
            return ["%.18f" % value.x, "%.18f" % value.y]
        else:
            return [0,0]

    def value_from_datadict(self, data, files, name):
        long, lat = [widget.value_from_datadict(data, files, name + '_%s' % i) \
                                          for i, widget in enumerate(self.widgets)]

        location = Point(float(long),float(lat))


        return str(location)

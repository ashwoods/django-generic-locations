/* JS script for django google maps widget */


// TODO: make the selectors more flexible
$(document).ready(function() {

    var long_obj = $('#id_generic_locations-genericlocation-content_type-object_id-0-position_0')
    var lat_obj = $('#id_generic_locations-genericlocation-content_type-object_id-0-position_1')
    var address_obj = $('#id_generic_locations-genericlocation-content_type-object_id-0-computed_address')


    function AddressLookup(map,address,region) {

          var geocoder = new google.maps.Geocoder();
          var position = geocoder.geocode({'address': address,'region':region},

          function(results,status) {
              if (status == google.maps.GeocoderStatus.OK) {
                if (status != google.maps.GeocoderStatus.ZERO_RESULTS) {
                  map.setCenter(results[0].geometry.location);
                  var marker = new google.maps.Marker({map:map, position:results[0].geometry.location});
                  //p.setZoom(15);
                  address_obj.val(results[0].formatted_address)
                  lat_obj.val(results[0].geometry.location.lat())
                  long_obj.val(results[0].geometry.location.lng())
                }
              }
              else {
                alert("Could not find the address.");

              }
            }
          );
        }

    function resizeMap(map, latlng) {
        google.maps.event.trigger(map, "resize");
        map.setCenter(latlng)

        if (lat_obj.val() == 0 & long_obj.val() == 0) {
            map.setZoom(1);
        }

        else {
            var marker = new google.maps.Marker({map:map, position:latlng});
            map.setZoom(5);

        }
    }





    var latlng = new google.maps.LatLng(lat_obj.val(), long_obj.val());
    var mapOptions = {
        zoom: 5,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };


   $('#id_generic_locations-genericlocation-content_type-object_id-0-position_1')
   .after("<button id='search_address' style='margin-left:5px' type='button' value='Geocode'>Search Address</button>")
   .after("<button id='zoom' style='margin-left:5px' type='button' value='zoom'>Zoom</button>")
   .parent()
   .append("<div id='map_canvas' style='width:600px; height:300px; margin: 0px; margin-left: 0px;' ></div>")




    var map = new google.maps.Map(document.getElementById("map_canvas"),  mapOptions);
    if ($('#map_canvas').is(":visible")) {
        resizeMap(map, latlng)
    }

    $('.collapse-handler').click( function () { //TODO: xpath selector use child
        resizeMap(map, latlng)
    });

    $('#zoom').click(function(){
        map.setZoom(15)
    });

    $('#search_address').click( function () {
        var address = $('#id_generic_locations-genericlocation-content_type-object_id-0-address').val()
        var city    = $('#id_generic_locations-genericlocation-content_type-object_id-0-city').val()
        var state =   $('#id_generic_locations-genericlocation-content_type-object_id-0-state_or_province').val()
        var zipcode = $('#id_generic_locations-genericlocation-content_type-object_id-0-zipcode').val()
        var country = $('#id_generic_locations-genericlocation-content_type-object_id-0-country').val()
        var geocode = address + ',' + city + ',' + state + ',' + zipcode

        AddressLookup(map,geocode,country);

    });
});





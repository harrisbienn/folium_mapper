"""
NAME:           Mapper.py

COMPATIBILITY:  Python 3.10

DESCRIPTION:    This program allows the user to draw a bounding box polygon using a mapping interface and
retrieve the corner coordinates

TO RUN:
    -

DATA FORMAT:    Manual input

REQUIRES:       folium

TODO:           1)

AUTHOR:         Harris Bienn

ORGANIZATION:   The Water Institute of The Gulf

CONTACT:        hbienn@thewaterinstitute.org
"""

import os
import folium
from folium import plugins, features

# Create a map object with coordinates centered on Baton Rouge, LA.
m = folium.Map(location=[30.432555, -91.192306],
               zoom_start=7,
               crs="EPSG4326",
               )
# Enable inset map
insetmap = plugins.MiniMap(position='bottomright')
m.add_child(insetmap)

# Display cursor coordinates on screen
cformat = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
plugins.MousePosition(position='bottomleft',
                      separator=' | ',
                      prefix="Mouse:",
                      lat_formatter=cformat,
                      lng_formatter=cformat
                      ).add_to(m)

# Enable geolocation search
plugins.Geocoder(position='topright',
                 addmarker=True
                 ).add_to(m)

features.LatLngPopup().add_to(m)

# Allow map to be made full screen
plugins.Fullscreen(position="topright",
                   title="Make fullscreen",
                   title_cancel="Exit fullscreen",
                   force_separate_button=True,
                   ).add_to(m)

# Allow user to draw polygon and export bounding box and geojson
plugins.Draw(export=True,
             filename="boundingbox.geojson",
             position="topleft",
             draw_options={"rectangle": {'allowIntersection': False}},
             edit_options={"poly": {'allowIntersection': False}}
             ).add_to(m)

# Display the map
m

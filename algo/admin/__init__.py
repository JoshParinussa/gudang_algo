"""admin.py init."""
from django.contrib import admin

from .supplier import *
from .product import *
from .unit import *
from .tracking import *

admin.site.site_title = 'Gudang Algo'
admin.site.site_header = 'Gudang Algo'

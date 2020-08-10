"""Config admin.py."""
from django.contrib import admin

# Register your models here.
from algo.models import Unit


class UnitAdmin(admin.ModelAdmin):
    """Config admin."""
    list_display = ('name', )


admin.site.register(Unit, UnitAdmin)

from django.db import models

from .base import BaseModel

class Unit(BaseModel):
    """Unit."""
    name = models.CharField(max_length=128, verbose_name="nama satuan")

    def __str__(self):
        """String representation."""
        return self.name
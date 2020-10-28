from django.db import models
from system_users.models import BaseModel


class Advertisement(BaseModel):
    image = models.ImageField(upload_to='advertisement_images', blank=False, null=False)
    side = models.CharField(max_length=10, blank=False, null=False)
    is_applied = models.BooleanField(default=False)

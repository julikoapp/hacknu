from django.contrib import admin
from garbage import models

# Register your models here.

admin.site.register(models.Client)
admin.site.register(models.Operator)
admin.site.register(models.Brigada)
admin.site.register(models.Task)

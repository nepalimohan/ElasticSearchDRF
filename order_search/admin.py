from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.SalesOrder)
admin.site.register(models.SalesOrderItem)
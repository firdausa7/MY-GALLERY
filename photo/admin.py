from django.contrib import admin
from .models import Location, tags, Category

# Register your models here.
admin.site.register(Location)
admin.site.register(tags)
admin.site.register(Category)
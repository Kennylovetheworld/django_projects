from django.contrib import admin

# Register your models here.

from unesco.models import Site, Category, States, ISO, Region

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(States)
admin.site.register(ISO)
admin.site.register(Region)

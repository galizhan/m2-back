from django.contrib import admin

from m2.main.models import City, Level


# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

from django.contrib import admin

from m2.building.models import Building, BuildingImage, BuildingPrice, BuildingAdditional


class BuildingImageInline(admin.TabularInline):
    model = BuildingImage
    extra = 1


class BuildingPriceInline(admin.TabularInline):
    model = BuildingPrice
    extra = 1


class BuildingAdditionalInline(admin.TabularInline):
    model = BuildingAdditional
    extra = 1


# Register your models here.
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    inlines = [BuildingImageInline, BuildingPriceInline, BuildingAdditionalInline]
    autocomplete_fields = ['level', 'city']
    list_display = ['name', 'level', 'city', 'created_at']
    search_fields = ['name']

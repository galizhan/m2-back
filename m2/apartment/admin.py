from django.contrib import admin

from m2.apartment.models import Apartment, ApartmentImage


class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1
# Register your models here.
@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['building']
    inlines = [ApartmentImageInline]

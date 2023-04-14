from m2.investment.models import Investment, InvestmentDocuments, Favourite
from django.contrib import admin

class InvestmentDocumentInline(admin.TabularInline):
    model = InvestmentDocuments
    extra = 1
@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'description', 'user__username')
    inlines = [InvestmentDocumentInline]
    autocomplete_fields = ['user']
@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    search_fields = ('id', 'investment', 'user__username')

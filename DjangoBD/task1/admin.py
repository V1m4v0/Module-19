from django.contrib import admin
from .models import Buyer, Game, News

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'cost', 'size']
    list_filter = ['size', 'cost']
    search_field = ['title']
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['name', 'balance', 'age']
    list_filter = ['balance', 'age']
    search_field = ['name']
    list_per_page = 30
    readonly_field = ['balance']

admin.site.register(News)
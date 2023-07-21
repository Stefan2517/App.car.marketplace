from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('masina', 'stare')
    list_filter = ('stare',) # daca nu puneam virgula nu il lua ca si tuple
    search_fields = ('masina', 'descriere')

admin.site.register(Item, MenuItemAdmin)


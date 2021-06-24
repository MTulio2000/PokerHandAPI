from django.contrib import admin
from player.models import Player

class Players(admin.ModelAdmin):
    list_display = ('id','name','hand')
    list_display_links = ('id',)
    search_fields = ('nome','id')

admin.site.register(Player,Players)
from django.contrib import admin

from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

admin.site.register(Band, BandAdmin)


class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'type')

admin.site.register(Listing, ListAdmin)

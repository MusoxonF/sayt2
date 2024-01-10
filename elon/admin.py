from django.contrib import admin
from .models import Locations, Image, Kuzov, Yoqilgi, Uzatish, Uzatma, Car


admin.site.register(Locations)
admin.site.register(Image)
admin.site.register(Kuzov)
admin.site.register(Yoqilgi)
admin.site.register(Uzatish)
admin.site.register(Uzatma)
admin.site.register(Car)
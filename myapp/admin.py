from django.contrib import admin
from .models import (
    Slider, Advertisement, SocialLink, Celebrity, Trailer
)

admin.site.register(Slider)
admin.site.register(Advertisement)
admin.site.register(SocialLink)
admin.site.register(Celebrity)
admin.site.register(Trailer)

# 5 more needed
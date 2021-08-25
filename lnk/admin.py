from django.contrib import admin
from .models import profile,Social_Media,site_links,feedback
# Register your models here.
admin.site.register(profile)
admin.site.register(Social_Media)
admin.site.register(site_links)
admin.site.register(feedback)
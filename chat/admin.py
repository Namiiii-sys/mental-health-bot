from django.contrib import admin

from .models import *

admin.site.register(ChatMessage)
admin.site.register(DailyAffirmation)
admin.site.register(SupportResource)
from django.contrib import admin

from .models import News, Update, Social


admin.site.register(News)
admin.site.register(Update)
admin.site.register(Social)

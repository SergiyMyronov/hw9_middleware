from django.contrib import admin
from middleware.models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'path', 'method')


admin.site.register(Log, LogAdmin)

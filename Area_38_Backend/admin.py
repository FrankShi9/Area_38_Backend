from django.contrib import admin

from Area_38_Backend.models import User


@admin.register(User)
# Just a template, change below
class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('analysisID', 'status', 'result', 'review')
    list_filter = ('analysisID', 'status')

    fieldsets = (
        (None, {
            'fields': ('analysisID','status', 'result')
        }),
    )
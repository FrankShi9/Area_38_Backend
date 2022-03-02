from django.contrib import admin

from Area_38_Backend.models import User


@admin.register(User)
# Just a template, change below
class UserStatusAdmin(admin.ModelAdmin):
    list_display = ('analysisID', 'status', 'result', 'review')
    list_filter = ('analysisID', 'status')

    fieldsets = (
        (None, {
            'fields': ('analysisID', 'status', 'result')
        }),
    )


from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def my_protected_view(request):
    """A view that can only be accessed by logged-in users"""
    return render(request, 'login.vue', {'current_user': request.user})

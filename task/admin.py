from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):

    list_display = ('content','created')
    search_fields = ('content',)
    list_filter = ('created',)
    ordering = ('created',)
    # fields = ('title','price','authors')

    fieldsets = (
        (None, {
            'fields': ('content', )
        }),
        ('日期', {
            'fields': ('created', ),
        }),
    )

admin.site.register(Task,TaskAdmin)

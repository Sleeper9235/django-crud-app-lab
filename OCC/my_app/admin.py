from django.contrib import admin
from .models import Group, Thread
# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Group, GroupAdmin)
admin.site.register(Thread)
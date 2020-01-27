from django.contrib import admin
from .models import Crime
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title')


admin.site.register(Crime)
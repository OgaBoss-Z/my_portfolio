from django.contrib import admin
from .models import *

# Register your models here.
# Define inline image fields for the admin  
class ImageInline(admin.TabularInline):
   model = ProjectImage
   extra = 3
   
class PortfolioAdmin(admin.ModelAdmin):
   list_display = ['name', 'category', 'created']
   list_filter = ['name', 'created']
   prepopulated_fields = {'slug': ('name',)}
   inlines = [ImageInline]
admin.site.register(Portfolio, PortfolioAdmin)

admin.site.register(Category)



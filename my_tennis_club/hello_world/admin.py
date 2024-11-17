from django.contrib import admin
from .models import Hello

# Register your models here.
class HelloAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Hello, HelloAdmin)


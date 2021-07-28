from django.contrib import admin
from .models import Crew

# Register your models here.
class CrewAdmin(admin.ModelAdmin):
    list_display = ("title", "content",)

admin.site.register(Crew, CrewAdmin)
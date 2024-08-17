from django.contrib import admin
from .models import CrudModel
# Register your models here.
@admin.register(CrudModel)
class CrudAdmin(admin.ModelAdmin):
    list_display = ('id','name','book','game')
    
    
from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import *

# Register your models here.
class VanAdmin(admin.ModelAdmin):
    exclude=('user',)
    

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
            return True
        

    def has_delete_permission(self, request, obj=None):
        return True
    
    def has_view_permission(self, request, obj=None):
        return True

admin.site.register(Van, VanAdmin)



class MakeReservationAdmin(admin.ModelAdmin):
    exclude=('user',)
    list_display = ('name','surname')


    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(MakeReservation, MakeReservationAdmin)

class RentVanAdmin(admin.ModelAdmin):
    exclude=('user',)
    list_display = ('name','surname')


    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(RentVan, RentVanAdmin)
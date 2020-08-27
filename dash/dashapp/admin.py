from django.contrib import admin
from .models import BannedIP,UntrackedUserAgent,Visitor
from django import forms

def Active(modeladmin,request,queryset):
    queryset.update(status='act')

def Inactive(modeladmin,request,queryset):
    queryset.update(status='inact')   

class VisitorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name'] }),
        ('Start of Session',{'fields':['session_start'] }),
        ('End of Session' , {'fields':['last_update'] })
    ]
    list_display = ('name','status')
    actions = [Active,Inactive]
        
admin.site.register(Visitor,VisitorAdmin)

# Register your models here.
admin.site.register(BannedIP)
admin.site.register(UntrackedUserAgent)


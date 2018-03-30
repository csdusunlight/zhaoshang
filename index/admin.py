#coding:utf-8
'''
Created on 2018年3月30日

@author: lch
'''
from django.contrib import admin
from .models import MerchantApply
class MerchantApplyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'url', 'ww', 'qq', 'tel']
    list_display = ('date','name','tel','qq','url','ww')

admin.site.register(MerchantApply, MerchantApplyAdmin)
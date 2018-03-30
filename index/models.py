#coding:utf-8
'''
Created on 2018年3月30日

@author: lch
'''
from django.db import models
import datetime
class MerchantApply(models.Model):
    date = models.DateField(u"报名日期", default=datetime.date.today)
    url = models.URLField(u"店铺链接", max_length=20)
    name = models.URLField(u"联系人姓名", max_length=20)
    tel = models.URLField(u"联系人电话", max_length=20)
    qq = models.URLField(u"联系人QQ", max_length=20)
    ww = models.URLField(u"联系人旺旺", max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('-date',)
        verbose_name_plural = u"商家报名"
        verbose_name = u"商家报名"
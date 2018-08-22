#coding:utf-8
'''
Created on 2018年3月28日

@author: lch
'''
from django.http.response import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.views.generic.base import View
from django.shortcuts import render
from .models import MerchantApply
import logging
from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
logger = logging.getLogger('wafuli')
class IndexView(View):
    def get(self, request):
        template = 'index.html'
        return render(request, template)
    def post(self, request): 
        res = {'code':0}
        url = request.POST.get('url', '')
        name = request.POST.get('name', '')
        tel = request.POST.get('tel', '')
        qq = request.POST.get('qq', '')
        wangwang = request.POST.get('wangwang', '')
        content = ''
        try:
            MerchantApply.objects.create(url=url, name=name, tel=tel, qq=qq, ww=wangwang)
        except Exception as e:
            res['code'] = 1
            res['msg'] = str(e)
            return JsonResponse(res)
            
        url = url.replace('https','http')
        if url:
            content += '<p><a href="%s">商家店铺链接</a><p/>' % url
        if name:
            content += '<p>联系人姓名：%s</p>' % name
        if tel:
            content += '<p>联系人电话：%s</p>' % tel
        if qq:
            content += '<p>联系人QQ：%s</p>' % qq
        if wangwang:
            content += '<p>联系人旺旺：%s</p>' % wangwang
        try:
            from_email = settings.DEFAULT_FROM_EMAIL
            # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
            msg = EmailMultiAlternatives('商家报名', content, from_email, ['5815397@qq.com'])
             
            msg.content_subtype = "html"
             
            # 添加附件（可选）
#             msg.attach_file('./twz.pdf')
             
            # 发送
            msg.send()
        except Exception as e:
            logger.info("send email failed:" + str(e))
        return JsonResponse(res)
    


# def send_email(to_email, subject, content):
#     mail_host="smtp.126.com"  #设置服务器
#     mail_user="hunanjinyezi@126.com"    #用户名
#     mail_pass="jinyezi520"   #口令 
#     mail_postfix="126.com"  #发件箱的后缀
#     msg = MIMEText(content,_subtype='html',_charset='utf-8') #创建一个实例，这里设置为html格式邮件
#     msg['Subject'] = subject    #设置主题
#     msg['From'] = u"福利联盟<" + mail_user + ">"
#     msg['To'] = to_email
#     try:  
#         s = smtplib.SMTP()  
#         s.connect(mail_host)  #连接smtp服务器
#         s.login(mail_user,mail_pass)  #登陆服务器
#         res = s.sendmail(mail_user, [to_email,], msg.as_string())  #发送邮件
#         s.close()  
#         return 0
#     except Exception as e:
#         print('error')
#         print (e)
#         return 1

def product(request):
    template = 'product.html'
    return render(request, template)

def aboutus(request):
    template = 'aboutus.html'
    return render(request, template)

def cooperate(request):
    template = 'cooperate.html'
    return render(request, template)
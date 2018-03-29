#coding:utf-8
'''
Created on 2018年3月28日

@author: lch
'''
from django.http.response import HttpResponse, JsonResponse
from email.mime.text import MIMEText
import smtplib
from django.views.generic.base import View
from django.shortcuts import render
class IndexView(View):
    def get(self, request):
        template = 'index.html'
        return render(request, template)
    def post(self, request): 
        url = request.POST.get('url', '')
        name = request.POST.get('name', '')
        tel = request.POST.get('tel', '')
        qq = request.POST.get('qq', '')
        wangwang = request.POST.get('wangwang', '')
        content = ''
        if url:
            content += '商家店铺链接：' + 'https://wafuli.cn/' + '\n'
        if name:
            content += '联系人姓名：' + name + '\n'
        if tel:
            content += '联系人电话：' + tel + '\n'
        if qq:
            content += '联系人QQ：' + qq + '\n'
        if wangwang:
            content += '联系人旺旺：' + wangwang + '\n'
        print (content)
        code = send_email('690501772@qq.com', '会议纪要', content)
        return JsonResponse({'code':code})
    


def send_email(to_email, subject, content):
    mail_host="smtp.126.com"  #设置服务器
    mail_user="hunanjinyezi@126.com"    #用户名
    mail_pass="jinyezi520"   #口令 
    mail_postfix="126.com"  #发件箱的后缀
    msg = MIMEText(content,_subtype='html',_charset='utf-8') #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = subject    #设置主题
    msg['From'] = u"福利联盟<" + mail_user + ">"
    msg['To'] = to_email
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        res = s.sendmail(mail_user, [to_email,], msg.as_string())  #发送邮件
        s.close()  
        return 0
    except Exception as e:
        print('error')
        print (e)
        return 1


# coding=utf-8
# 第三方 SMTP 服务
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#
# mail_host = "smtp.126.com"  # 设置服务器
# mail_user = "uhuiforciti@126.com"  # 用户名
# mail_pass = "uhuiforciti123"  # 口令
# 
# sender = 'confirm@uhui.com'
# receivers = ['929527511@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
# 
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
# 
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# 
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")
# 导入smtplib和MIMEText
#############
# 要发给谁，这里发给2个人
mailto_list = ["aaa@juyimeng.com", "bbb@juyimeng.com"]
#####################
# 设置服务器，用户名、口令以及邮箱的后缀
mail_host = "smtp.126.com"
mail_user = "uhuiforciti"
mail_pass = "uhuiforciti126"
mail_postfix = "126.com"


######################
def send_mail(to_list, sub, content):
    '''
to_list: 发给谁
sub: 主题
content: 内容
send_mail("aaa@126.com", "sub", "content")
    '''
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False
if __name__ == '__main__':
    if send_mail(mailto_list, "subject", "content"):
        print("发送成功")
    else:
        print("发送失败")


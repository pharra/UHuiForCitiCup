#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendConfirmMail(to_addr, address):
    # address 为登录判断的一条request
    from_addr = 'No-Reply@uhuiforciti.cn'
    password = 'pj4lkqMF4b'
    smtp_server = 'smtp.ym.163.com'
    msg = MIMEText('请点击下方链接确认注册\n %s' % address, 'plain', 'utf-8')
    msg['From'] = _format_addr('No-Reply <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('U惠网注册确认', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    try:
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        return True
    except smtplib.SMTPException as smtpe:
        print(str(smtpe))
        return False
    finally:
        server.quit()

if __name__ == "__main__":
    sendConfirmMail('527293764@qq.com', '佳佳是zz')
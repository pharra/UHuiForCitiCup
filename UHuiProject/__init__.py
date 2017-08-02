from wsgiref import headers

import pymysql
from django.http import HttpResponse


from UHuiProject.settings import DEBUG

pymysql.install_as_MySQLdb()
HttpResponse.type = 'HttpResponse'
if DEBUG is True:
    print('http')




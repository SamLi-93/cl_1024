# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class Cl1024Pipeline(object):
#     def process_item(self, item, spider):
#         return item

from email.header import Header
from email.mime.text import MIMEText
import smtplib
import re
import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class Cl1024Pipeline(object):
    def __init__(self):
        self.file = codecs.open('tset.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):

        for i in item['movie_name']:
            print "~~~~~~~~~~~~~~~~~~~\n"
            print i
            print "~~~~~~~~~~~~~~~~~~~~\n"
        line = 'the list:' + '\n'
        for i in range(len(item['movie_name'])):
            movie_name = {"movie_name": item['movie_name'][i].decode('utf-8')}
            url = {"url": 'http://cl.miicool.info/' + item['url'][i]}
            if re.match(r'.+\\u0031\\u0037\\u003\d|.+\\u0031\\u0036\\u003[7-9]|.+\\u817f|.+\\u4e1d\\u000d\\u000a',
                        str(movie_name)):
                line = line + json.dumps(movie_name, ensure_ascii=False) + '\n'
                line = line + json.dumps(url, ensure_ascii=False) + '\n'

        self.file.write(line)

        from_addr = 'mclaren1234@163.com'
        password = 'ly19940306'
        to_addr = '342447974@qq.com'
        smtp_server = 'smtp.163.com'

        msg = MIMEText(line, 'plain', 'utf-8')
        msg['From'] = 'mclaren1234@163.com'
        msg['To'] = '342447974@qq.com'
        msg['Subject'] = Header('1024', 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

    def close_spider(self, spider):
        self.file.close()

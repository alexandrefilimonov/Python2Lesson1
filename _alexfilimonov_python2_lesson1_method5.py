#5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип 
#на кириллице.

import re
from subprocess import Popen, PIPE
from threading import Thread

class Pinger(object):
    def __init__(self, hosts):
        for host in hosts:
            pa = PingAgent(host)
            pa.start()

class PingAgent(Thread):
    def __init__(self, host):
        Thread.__init__(self)        
        self.host = host

    def run(self):
        p = Popen('ping '+host, stdout=PIPE)
        p1=p.stdout.read().decode('Utf-8')
        print(p1)
        #m = re.search('Average = (.*)ms', p.stdout.read())
        #if m: print 'Round Trip Time: %s ms -' % m.group(1), self.host
        #else: print 'Error: Invalid Response -', self.host


hosts = [
    'https://yandex.ru/',
    'https://www.youtube.com/'
]
Pinger(hosts)

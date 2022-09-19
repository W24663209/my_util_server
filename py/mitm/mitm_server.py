# -*- coding: utf-8 -*-
import asyncio
import json
import re
import socket
import threading

from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.addons import export
from web_socket import start as web_socket_start
from web_socket import send as web_socket_send

'''
抓包工具
'''


def getIP(domain):
    host = re.findall('\/\/(.*?)\/', domain)
    myaddr = socket.getaddrinfo(host[0], 'http')
    print('ip\t%s' % myaddr[0][4][0])
    return myaddr[0][4][0]


def get_ip_list(domain):  # 获取域名解析出的IP列表
    ip_list = []
    try:
        addrs = socket.getaddrinfo(domain, None)
        for item in addrs:
            if item[4][0] not in ip_list:
                ip_list.append(item[4][0])
    except Exception as e:
        print(str(e))
        pass
    return ip_list


def generate(flow, old_host, new_host):
    '''
    替换host
    :param flow:
    :param old_host:
    :param new_host:
    :return:
    '''
    flow.request.url = flow.request.url.replace(old_host, new_host)
    headers = flow.request.headers
    method = flow.request.method
    print('请求url:\t%s' % flow.request.url.replace(new_host, ''))
    curl_text = "curl '%s'" % flow.request.url
    curl_text += " -X '%s'" % method.upper()
    for header in headers.fields:
        curl_text += " -H '%s:%s'" % (header[0].decode('UTF-8'), header[1].decode('UTF-8'))
    if method.upper().__eq__('POST') or method.upper().__eq__('PUT'):
        curl_text += "--data-raw '%s'" % flow.request.text
    curl_text += ' --compressed'
    # if flow.request.url.startswith('http'):
    # curl_text += ' --insecure -o %s.json' % uuid.uuid1()
    print(curl_text)
    print('\n')


def contains_of_url(blacklist, url):
    '''
    list包含url中
    :param blacklist:
    :param url:
    :return:
    '''
    for black in blacklist:
        if url.__contains__(black):
            return True
    return False


class Addon(object):

    def request(self, flow):
        pass

    def response(self, flow):
        curl_command = export.curl_command(flow)
        raw_request = export.raw_request(flow)
        raw_response = export.raw_response(flow)
        data = {
            'curl_command': curl_command,
            'raw_request': raw_request.decode("utf-8"),
            'raw_response': raw_response.decode("utf-8")
        }
        web_socket_send(json.dumps(data))


class ProxyMaster(DumpMaster):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        try:
            DumpMaster.run(self)
        except KeyboardInterrupt:
            self.shutdown()


def start_web_socket():
    asyncio.run(web_socket_start())


if __name__ == "__main__":
    # options = Options(listen_host='0.0.0.0', listen_port=8088, mode="socks5")
    threading.Thread(target=web_socket_start, ).start()
    options = Options(listen_host='0.0.0.0', listen_port=8899, http2=True)
    config = ProxyConfig(options)
    master = ProxyMaster(options, with_termlog=False, with_dumper=False)
    master.server = ProxyServer(config)
    master.addons.add(Addon())
    master.run()

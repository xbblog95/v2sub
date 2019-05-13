#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from node import Node


class Shadowsocks(Node):

     password = ''

     def __init__(self, ip, port, remark, security, password):
        super(Shadowsocks, self).__init__(ip, port, remark, security)
        self.password = password

     def formatConfig(self) :
         ssConfig = {
             "log": {
                 "access": "",
                 "error": "",
                 "loglevel": "warning"
             },
             "inbounds": [
                 {
                     "port": 1080,
                     "listen": "0.0.0.0",
                     "protocol": "socks",
                     "sniffing": {
                         "enabled": True,
                         "destOverride": [
                             "http",
                             "tls"
                         ]
                     },
                     "settings": {
                         "auth": "noauth",
                         "udp": True
                     },
                 }
             ],
             "outbounds": [
                 {
                     "tag": "proxy",
                     "protocol": "shadowsocks",
                     "settings": {
                         "servers": [
                             {
                                 "address": self.ip,
                                 "method": self.security,
                                 "ota": False,
                                 "password": self.password,
                                 "port": int(self.port),
                                 "level": 1
                             }
                         ]
                     },
                     "streamSettings": {
                         "network": "tcp"
                     },
                     "mux": {
                         "enabled": False
                     }
                 },
                 {
                     "tag": "direct",
                     "protocol": "freedom"
                 },
                 {
                     "tag": "block",
                     "protocol": "blackhole",
                     "settings": {
                         "response": {
                             "type": "http"
                         }
                     }
                 }
             ],
             "routing": {
                    "strategy": "rules",
                    "settings": {
                        "domainStrategy": "AsIs",
                        "rules": [{
                            "type": "field",
                            "ip": [
                                "0.0.0.0/8",
                                "10.0.0.0/8",
                                "100.64.0.0/10",
                                "127.0.0.0/8",
                                "169.254.0.0/16",
                                "172.16.0.0/12",
                                "192.0.0.0/24",
                                "192.0.2.0/24",
                                "192.168.0.0/16",
                                "198.18.0.0/15",
                                "198.51.100.0/24",
                                "203.0.113.0/24",
                                "::1/128",
                                "fc00::/7",
                                "fe80::/10"
                            ],
                            "outboundTag": "direct"
                        }]
                    }
                }
         }
         return ssConfig


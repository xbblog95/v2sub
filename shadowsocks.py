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
          "log" : {
              "access" : "/var/log/v2ray/access.log",
              "error":"/var/log/v2ray/error.log",
              "logLevel": "none"
          },
          "inbounds": [
            {
              "port": 1080,
              "listen": "127.0.0.1",
              "protocol": "socks",
              "settings": {
                "udp": True
              },
              "tag": "in"
            }
          ],
          "outbounds": [
            {
              "settings" : {},
              "protocol":"freedom",
              "tag" : "direct"
            },
            {
                "settings" : {},
                "protocol":"blackhole",
                "tag" : "blocked"
            }
          ],
          "routing": {
            "strategy": "rules",
            "settings": {
              "domainStrategy": "AsIs",
              "rules": [
                {
                  "type" : "field",
                  "ip" : [
                    "geoip:cn",
                    "geoip:private"
                  ],
                  "outboundTag": "direct"
                },
                {
                  "type":"field",
                  "inboundTag":["in"],
                  "outboundTag":"out"
                }
              ]
            }
          }
        }
         ssConfig['outbounds'].append({
             "tag": "out",
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
         })
         return ssConfig


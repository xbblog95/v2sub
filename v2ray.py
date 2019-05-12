#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from node import Node


class V2ray(Node):
    uuid = ''
    alterId = 0
    network = ''
    camouflageType = ''
    camouflageHost = ''
    camouflagePath = ''
    camouflageTls = ''

    def __init__(self, ip, port, remark, security, uuid, alterId, network, camouflageType, camouflageHost, camouflagePath, camouflageTls):
        super(V2ray, self).__init__(ip, port, remark, security)
        self.uuid = uuid
        self.alterId = alterId
        self.network = network
        self.camouflageHost = camouflageHost
        self.camouflagePath = camouflagePath
        self.camouflageTls = camouflageTls
        self.camouflageType = camouflageType

    def formatConfig(self):
        v2rayConf = ''
        if self.network == 'tcp' or self.network == 'auto':
            # tcp下
            v2rayConf = {
                "inbound": {
                    "port": 1080,
                    "listen": "127.0.0.1",
                    "protocol": "socks",
                    "settings": {
                        "udp": True
                    }
                },
                "outbound": {
                    "protocol": "vmess",
                    "settings": {
                        "vnext": [{
                            "address": self.ip,
                            "port": int(self.port),
                            "users": [
                                {
                                    "id": self.uuid,
                                    "alterId" : self.alterId
                                }
                            ]
                        }]
                    }
                },
                "outboundDetour": [{
                    "protocol": "freedom",
                    "tag": "direct",
                    "settings": {}
                }],
                "routing": {
                    "strategy": "rules",
                    "settings": {
                        "domainStrategy": "IPOnDemand",
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
        elif self.network == 'kcp':
            # kcp 下
            v2rayConf = {
                "inbound": {
                    "port": 1080,
                    "listen": "127.0.0.1",
                    "protocol": "socks",
                    "settings": {
                        "udp": True
                    }
                },
                "outbound": {
                    "protocol": "vmess",
                    "settings": {
                        "vnext": [{
                            "address": self.ip,
                            "port": int(self.port),
                            "users": [
                                {
                                    "id": self.uuid,
                                    "alterId": self.alterId
                                }
                            ]
                        }]
                    },
                    "streamSettings" : {
                        "network": "kcp",
                        "kcpSettings": {
                            "mtu": 1350,
                            "tti": 50,
                            "uplinkCapacity": 12,
                            "downlinkCapacity": 100,
                            "congestion": False,
                            "readBufferSize": 2,
                            "writeBufferSize": 2,
                            "header": {
                                "type": self.camouflageType,
                            }
                        }
                    }
                },
                "outboundDetour": [{
                    "protocol": "freedom",
                    "tag": "direct",
                    "settings": {}
                }],
                "routing": {
                    "strategy": "rules",
                    "settings": {
                        "domainStrategy": "IPOnDemand",
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
        elif self.network == 'ws':
            # ws
            v2rayConf = {
                "inbound": {
                    "port": 1080,
                    "listen": "127.0.0.1",
                    "protocol": "socks",
                    "settings": {
                        "udp": True
                    }
                },
                "outbound": {
                    "protocol": "vmess",
                    "settings": {
                        "vnext": [{
                            "address": self.ip,
                            "port": int(self.port),
                            "users": [
                                {
                                    "id": self.uuid,
                                    "alterId": self.alterId
                                }
                            ]
                        }]
                    },
                    "streamSettings": {
                        "network": "ws",
                        "security": self.camouflageTls,
                        "tlsSettings": {
                            "allowInsecure": True,
                        },
                        "wsSettings" : {
                            "path": self.camouflagePath,
                            "headers" : {
                                "Host": self.camouflageHost
                            }
                        }
                    }
                },
                "outboundDetour": [{
                    "protocol": "freedom",
                    "tag": "direct",
                    "settings": {}
                }],
                "routing": {
                    "strategy": "rules",
                    "settings": {
                        "domainStrategy": "IPOnDemand",
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
        else:
            # h2
            v2rayConf = {
                "inbound": {
                    "port": 1080,
                    "listen": "127.0.0.1",
                    "protocol": "socks",
                    "settings": {
                        "udp": True
                    }
                },
                "outbound": {
                    "protocol": "vmess",
                    "settings": {
                        "vnext": [{
                            "address": self.ip,
                            "port": int(self.port),
                            "users": [
                                {
                                    "id": self.uuid,
                                    "alterId": self.alterId
                                }
                            ]
                        }]
                    },
                    "streamSettings": {
                        "network": "ws",
                        "security": self.camouflageTls,
                        "tlsSettings": {
                            "allowInsecure": True,
                        },
                        "httpSettings": {
                            "path": self.camouflagePath,
                            "host": [
                                self.camouflageHost
                            ]
                        }
                    }
                },
                "outboundDetour": [{
                    "protocol": "freedom",
                    "tag": "direct",
                    "settings": {}
                }],
                "routing": {
                    "strategy": "rules",
                    "settings": {
                        "domainStrategy": "IPOnDemand",
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
            return v2rayConf

#!/usr/bin/python
# -*- coding: utf-8 -*-

class QcloudApi:
    def __init__(self, module, config):
        self.module = module
        self.config = config

    def _factory(self, module, config):
        if (module == 'cdb'):
            from modules.cdb import Cdb
            service = Cdb(config)
        elif (module == 'cvm'):
            from modules.cvm import Cvm
            service = Cvm(config)
        elif (module == 'image'):
            from modules.image import Image
            service = Image(config)
        elif (module == 'lb'):
            from modules.lb import Lb
            service = Lb(config)
        elif (module == 'sec'):
            from modules.sec import Sec
            service = Sec(config)
        elif (module == 'trade'):
            from modules.trade import Trade
            service = Trade(config)
        elif (module == 'monitor'):
            from modules.monitor import Monitor
            service = Monitor(config)
        elif (module == 'cdn'):
            from modules.cdn import Cdn
            service = Cdn(config)
        else:
            raise ValueError, 'module not exists'

        return service

    def setSecretId(self, secretId):
        self.config['secretId'] = secretId

    def setSecretKey(self, secretKey):
        self.config['secretKey'] = secretKey

    def setRequestMethod(self, method):
        self.config['method'] = method

    def setRegion(self, region):
        self.config['region'] = region

    def generateUrl(self, action, params):
        service = self._factory(self.module, self.config)
        return service.generateUrl(action, params)

    def call(self, action, params):
        service = self._factory(self.module, self.config)

        methods = dir(service)
        for method in methods:
            if (method == action):
                func = getattr(service, action)
                return func(params)

        return service.call(action, params)

def main():
    module = 'cdn'
    action = 'UploadCdnEntity'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'post'
    }
    params = {
        'entityFileName': '/test_____don.html',
        'entityFile': 'c:/xampp/htdocs/index.html'
    }
    service = QcloudApi(module, config)
    print 'URL:\n' + service.generateUrl(action, params)
    print service.call(action, params)

if (__name__ == '__main__'):
    main()

'''
Created on 2013-7-5

@author: Administrator
'''

import logging

class Log(object):

    @classmethod
    def getDefaultLogger(cls):
        if(cls.__default == None):
            cls.__default = cls.__getDefaultLogger()

        return cls.__default



    __default = None
    @classmethod
    def __getDefaultLogger(cls):
        _log = logging.getLogger('default')
        _formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        _file = logging.FileHandler(_log.name + '.log')
        _file.setFormatter(_formatter)
        _file.setLevel(logging.DEBUG)
        _console = logging.StreamHandler()
        _console.setFormatter(_formatter)
        _file.setLevel(logging.NOTSET)
        _log.addHandler(_file)
        _log.addHandler(_console)
        return _log

if __name__ == '__main__':
    Log.getDefaultLogger().error('dddddddddddddddd')
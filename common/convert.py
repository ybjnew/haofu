from datetime import datetime

class Convert(object):

    @staticmethod   
    def toStr(input, default = ''):
        try:
            return str(input)
        except:
            return default

    @staticmethod   
    def toInt(input, default = 0):
        try:
            return int(input)
        except:
            return default

    @staticmethod   
    def toFloat(input, default = 0.0):
        try:
            return float(input)
        except:
            return default

    @staticmethod   
    def toDateTime(input, default = datetime.min, format = '%Y-%m-%d %H:%M:%S'):
        try:
            return datetime.strptime(input, format)
        except:
            return default

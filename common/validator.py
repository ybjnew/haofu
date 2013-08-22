

import re

class Validator(object):

    __reEmail = re.compile(r"^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))$", re.IGNORECASE)
    __reUri = re.compile(r"^(https?|s?ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$", re.IGNORECASE)
    __reNumber = re.compile(r"^-?(?:\d+|\d{1,3}(?:,\d{3})+)?(?:\.\d+)?$")
    __reDigits = re.compile(r"^\d+$")
    __reDate = re.compile(r"^\d{4}-(?:0\d|1[0-2])-(?:[0-2]\d|3[01])$")
    __reTime = re.compile(r"^(?:[01]\d|2[0-3])\:[0-5]\d\:[0-5]\d$")
    __reDateTime = re.compile(r"^\d{4}-(?:0\d|1[0-2])-(?:[0-2]\d|3[01])( (?:[01]\d|2[0-3])\:[0-5]\d\:[0-5]\d)?$")
    __reMobile = re.compile(r"^(((13[0-9]{1})|(15[0-9]{1}))+\d{8})$")

    @classmethod
    def required(cls, input):
        if input is None or len(input) == 0:
            return False
        return True

    @classmethod
    def range(cls, input, min = None, max = None):
        count = len(input)
        if min is not None:
            if max is not None:
                if count >= min and count <= max:
                    return True
                return False
            else:
                if count >= min:
                    return True
                return False
        else:
            if max is not None:
                if count <= max:
                    return True
                else:
                    return False
            else:
                raise ValueError(r'min and max should not both be empty')

    @classmethod
    def rangeBytes(cls, input, min = -1, max = -1):
        count = len(input)
        for c in input:
            if ord(c) > 127:
                count = count + 1
        if min >= 0:
            if max >= 0:
                if count >= min and count <= max:
                    return True
                return False
            else:
                if count >= min:
                    return True
                return False
        else:
            if max >= 0:
                if count <= max:
                    return True
                else:
                    return False
            else:
                raise ValueError(r'min and max should not be both empty')

    @classmethod
    def rangeLength(cls, input, min = -1, max = -1):
        count = len(input)
        if min >= 0:
            if max >= 0:
                if count >= min and count <= max:
                    return True
                return False
            else:
                if count >= min:
                    return True
                return False
        else:
            if max >= 0:
                if count <= max:
                    return True
                else:
                    return False
            else:
                raise ValueError(r'min and max should not be both empty')

    @classmethod
    def rangeWords(cls, input, min = -1, max = -1):
        count = len(re.compile(r'/\b\w+\b/').findall())
        if min >= 0:
            if max >= 0:
                if count >= min and count <= max:
                    return True
                return False
            else:
                if count >= min:
                    return True
                return False
        else:
            if max >= 0:
                if count <= max:
                    return True
                else:
                    return False
            else:
                raise ValueError(r'min and max should not be both empty')

    @classmethod
    def isEmail(cls, input):  
        return cls.__reEmail.match(input)

    @classmethod
    def isUri(cls, input):
        return cls.__reUri.match(input)

    @classmethod
    def isNumber(cls, input):
        return cls.__reNumber.match(input)

    @classmethod
    def isDigits(cls, input):
        return cls.__reDigits.match(input)

    @classmethod
    def isDate(cls, input):
        return cls.__reDate.match(input)

    @classmethod
    def isTime(cls, input):
        return cls.__reTime.match(input)

    @classmethod
    def isDateTime(cls, input):
        return cls.__reDateTime.match(input)

    @classmethod
    def isMobile(cls, input):
        return cls.__reMobile.match(input)

    @classmethod
    def isRegExp(cls, input, exp, options = None):
        __re = re.compile(exp, options)
        return __re.match(input)
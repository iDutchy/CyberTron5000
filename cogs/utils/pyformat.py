"""

A python package made to make Python formatting easier for us all.
Technically useless, aesthetically pleasing.

Made by nizcomix
Contact on discord ♿niztg#7532 (350349365937700864) for questions

"""

import discord


class NativePython(object):
    """For functions that can help using Native Python"""
    
    def __init__(self):
        pass
    
    def listify(self, list: list, char='\n', limit: int = None):
        """
        Puts everything in a pretty list for you.

        :param list:
        :param char:
        :param limit:
        :return:
        """
        if not limit:
            return f"{char}".join(list)
        else:
            return f"{char}".join(list[:limit])
    
    def hyper_replace(self, text, old: list, new: list):
        """
        Allows you to replace everything you need in one function using two lists.
        :param text:
        :param old:
        :param new:
        :return:
        """
        msg = str(text)
        for x, y in zip(old, new):
            msg = str(msg).replace(x, y)
        return msg
    
    def bool_help(self, value: bool, true: str = None, false: str = None):
        """Returns a custom bool message without you having to write a pesky if/else.
        :param true:
        :param false:
        :return:
        """
        if value:
            return true
        else:
            return false


class Discord(object):
    def __init__(self, bot_user_id):
        self.bot_user_id = bot_user_id
    
    def fieldify(self, limit: int, names: list, values: list):
        pass

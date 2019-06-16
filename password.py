import random

class Password(object):
    def __init__(self, len=8):
        self.len = len

    def generate_password(self):
        '''Generate a password in random in the lenght of len.'''
        # Reference:
        # Google: python generate random password -> https://www.practicepython.org/solution/2014/06/06/16-password-generator-solutions.html
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        passlen = self.len
        p =  "".join(random.sample(s,passlen ))
        return p
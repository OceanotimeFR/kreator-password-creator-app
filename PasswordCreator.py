from imports import randint

class PasswordCreator():
    def __init__(self):
        self.asciiCharRange:list = [33,126]
        self.pwdCharList:list = []
        self.pwdLength:int = 0
        self.pwd = ""
    
    def isEmpty(self, l:list):
        return len(l) == 0

    def creator(self):
        checkEmpty = self.isEmpty(self.asciiCharRange)
        if not checkEmpty:
            self.pwdCharList = []
            for i in range(self.pwdLength):
                asciiRandInt:int = randint(*self.asciiCharRange)
                randomChar:int = chr(asciiRandInt)
                self.pwdCharList.append(randomChar)
            self.pwd:str = " ".join(self.pwdCharList)
            return 0
        return 1

    def call(self):
        self.pwdLength = int(input(">> Password size : "))
        self.creator()
        print(self.pwd)
        
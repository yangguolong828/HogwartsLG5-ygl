class MyException(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

raise MyException("value1","value2")

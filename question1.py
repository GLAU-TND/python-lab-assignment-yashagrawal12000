class MyException(Exception):
    def __init__(self,v):
        self.v = v
    def __str__(self):
        return str(self.v)
def xyz(a,b):
    c = a+b
    if(c>150):
        raise MyException('Err')


a = int(input('enter a number'))
b = int(input('enter a number'))
sum = a+b
if(sum>150):
    print(sum)
else:
    print('Custom Expection Occourd')

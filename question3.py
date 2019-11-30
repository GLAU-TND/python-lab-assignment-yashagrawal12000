try:
    i = int(input())
    print('No Error')
except Exception as e:
    print(e,type(e))
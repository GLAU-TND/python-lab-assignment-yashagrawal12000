c = (1,2,3,4,54,6,7,8,9)
try:
    c.remove(5)
    c = 5+'s'
    c = float('hello')

except AttributeError as e:
    print("AttributeError",e)
except TypeError as e:
    print("TypeError",e)
except ValueError as e:
    print("ValueErrror",e)
finally:
    print("Process Complete")
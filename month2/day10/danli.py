
class MyTest(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
            return cls.instance
        else:
            return cls.instance


a = MyTest()
b = MyTest()

print(id(a))
print(id(b))








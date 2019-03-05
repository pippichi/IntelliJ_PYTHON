class logging():
    def __init__(self, level):
        self.level = level

    def __call__(self, func):  # 接受函数
        print("开始__call__函数")
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=self.level,
                func=func.__name__))
            print("结束wrapper")
            print("开始func")
            func(*args, **kwargs)
        print("开始wrapper")
        return wrapper  # 返回函数


@logging(level='INFO')
def say(something):
    print("say {}!".format(something))

def logging1(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print ("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging1(level='INFORMATION')
def say1(something):
    print("say {}!".format(something))

def html_tags(tag_name):
    print("begin of outer function")
    def wrapper_(func):
        print("begin of inner wrapper function")
        def wrapper(*args,**kwargs):
            content = func(*args,**kwargs)
            print("<{tag}>{content}</{tag}>".format(tag=tag_name,content=content))
        print("end of inner wrapper function")
        return wrapper
    print("end of outer function")
    return wrapper_

@html_tags("b")
def hello(name="qyf"):
    return "hello {name}".format(name=name)


if __name__ =='__main__':
    say("bad")
    say1("good")
    hello()
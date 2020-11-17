import time
def decrator(func):
    def wrapper(*args,**kw):#封装到了里面 ,即我们认为wrapper就是对传进来的func的封装
        #*args为可变参数
        #**kw为关键字参数，可为任意数量（为了同一结构
        #当不知道传的参数的数量的时候（*args,**kw）一定可以
        print(time.time())
        func(*args,**kw)
    return wrapper

@decrator
def f1(func_name):
    # print(time.time())
    print('this is a function'+func_name)
 
@decrator
def f2(func_name1,func_name2):
    print('this is a function2'+func_name1+func_name2)

@decrator
def f3(func_name1,func_name2,**kw):#**kw为带关键字参数（可任意数量
    print('this is a function2'+func_name1+func_name2)
    print(type(kw))
    print(kw)

f3('t1','t2',a = 1,b = 2,c = '123')

f1('test_func')
f2('fff1---','fff2')
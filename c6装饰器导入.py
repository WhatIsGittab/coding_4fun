import time
#time.time()---Unix时间戳
def f1():
    # print(time.time())
    print('this is a function')

def f2():
    print('this is a function2')

def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)
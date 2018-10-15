 
 
 
 
 
'''
# 可迭代对象
    所有你可以使用 for .. in .. 语法的叫做一个迭代器：列表，字符串，文件……你经常使用它们是因为你可以如你所愿的读取其中的元素，

    但是你把所有的值都存储到了内存中，
    如果你有大量数据的话这个方式并不是你想要的。

# 生成器
生成器是可以迭代的，但是你 只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时生成数据:

yield关键字
    类似 return 的关键字，只是这个函数返回的是个生成器。

    以下面的createGenerator函数为例：
    你必须要理解：当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象

    函数内的代码什么时候执行呢？当你使用for进行迭代的时候.

    第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值.

    然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。

'''
 
# mylist = [1, 2, 3]
# mylist = [x*x for x in range(3)]   #生成一个列表 可迭代对象也是生成器
# mylist = (x*x for x in range(3))   #生成一个元组 是生成器不是可迭代对象

# for i in mylist:
#     print(i)


def createGenerator():
    mylist = range(3)
    mylist2 = range(6)
    for i in mylist :
        yield i 
    print("next:\n")
    for i in mylist2 :
        yield i 
    
mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
for i in mygenerator:
    print(i)
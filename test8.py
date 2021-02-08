# num = 1

# def test():
#     global num
#     num = 100
#     print(num)


# print(num)
# test()
# print(num)

num = [1]

def test1():
    num[0] = 100
    print(num[0])

print(num[0])
test1()
print(num[0])


# f = open('data.txt')
# print(f.readable())
# # print(f.readlines())
# print(f.readline())
# print(f.readline())
# f.close()


# with语句块，可以将文件打开之后，操作完毕，自动关闭这个文件
# 图片的话mode要使用“rb”，读取二进制的格式
# 正常的文本，可以使用rt，也就是他的默认格式
with open('data.txt')as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
def print_file_info(file_name):
    f = None
    '''
    如果在 try 块中出现异常，f 变量可能未被赋值(f的值还是None，不存在的东西怎么可能关闭呢)，
    导致在 finally 块中关闭未打开的文件会引发 NameError。
    '''
    try:
        f = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        print("出现了文件不存在的异常！")
        print(f"No such file or directory: {file_name}")
    else:
        contents = f.read()
        print(contents)
    finally:
        if f:
            f.close()




def append_file_info(file_name, data):
   with open(file_name, "a", encoding="utf-8") as f:
    f.write(data)
    f.write("\n")

if __name__ == '__main__':

    print_file_info("dsaads")
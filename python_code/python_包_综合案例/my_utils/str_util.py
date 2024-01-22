def str_reverse(s):
    """

    :param s:
    :return:
    """
    s_reverse = s[::-1]
    print(s_reverse)
    return s_reverse


def substr(s,x,y):
    s_slice = s[x:y:1]
    print(f"切片后的字符串为：{s_slice}")
    return s_slice

if __name__ == '__main__':
    str_reverse("sd")
    substr("0123456", 2, 5)
#
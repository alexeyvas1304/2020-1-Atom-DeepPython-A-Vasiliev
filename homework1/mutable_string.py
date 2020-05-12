from ctypes import sizeof, c_void_p, c_char, c_int, c_long

str_header_size = sizeof(c_void_p) * 3 + sizeof(c_long) + sizeof(c_int) * 4


def str_writable_view(obj):
    return (c_char * len(obj)).from_address(id(obj) + str_header_size)


def reverse_string(s):
    for i in range(len(s) // 2):
        s[i], s[-(i + 1)] = s[-(i + 1)], s[i]


if __name__ == "__main__":
    s = "hello world"
    print(s)
    print(id(s))
    print('-----------------')
    try:
        reverse_string(s)
    except TypeError:
        print('Generally strings are immutable')
    print('-----------------')
    reverse_string(str_writable_view(s))
    print("But if you try properly, all is possible:")
    print(s)
    print(id(s))

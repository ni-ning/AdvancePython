# -*- coding:utf-8 -*-

# 500G 文件 特殊只有一行，特殊分割符号 {|}


def my_readline(f, newline):
    buf = ''
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096 * 10)
        if not chunk:
            yield buf
            break
        buf += chunk


with open('input') as f:
    for line in my_readline(f, '{|}'):
        print(line)

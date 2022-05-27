#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    p = 'роцессорп'
    tmp = list(p)

    s = tmp[-1]
    for i in range(len(p)-1, -1, -1):
        tmp[i] = tmp[i-1]
    tmp[0] = s

    p = ''.join(tmp)
    print(p)
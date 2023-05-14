def every_odd_element(sorted_list):
    buf = []
    for i in sorted_list:
        if i % 2 != 0:
            buf.append(i)

    return buf

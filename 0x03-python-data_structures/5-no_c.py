#!/busr/bin/pyhton3

def no_c(my_string):
    str_len = len(my_string)
    x = 0

    for i in range(str_len - 1):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            x += 1    
        my_string[i] == my_string[i + x]

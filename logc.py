def xor2(a, b):
    if bool(a) == bool(b):
        return False
    else:
        return a or b


def xor3(x, y, z):  # not correct in global opinion
    if x == y == z == 1:
        return False
    elif x == 1 and y == z == 0:
        return True
    elif y == 1 and x == z == 0:
        return True
    elif z == 1 and x == y == 0:
        return True
    else:
        return False

def how_many(string_):  # function can help to avoid situation when
    num_of_o = 0        # number of Xs greater number of Os and vice versa
    num_of_x = 0
    while string_.find('O') != -1:
        num_of_o += 1
        string_ = string_.replace('O', "_", 1)
    while string_.find('X') != -1:
        num_of_x += 1
        string_ = string_.replace('X', "_", 1)
    nums = [num_of_o, num_of_x]
    return nums

def simplerotate(string_):  # clockwise
    string_fake = string_.copy()
    string_[2] = string_fake[0]
    string_[5] = string_fake[1]
    string_[8] = string_fake[2]
    string_[1] = string_fake[3]
    string_[7] = string_fake[5]
    string_[0] = string_fake[6]
    string_[3] = string_fake[7]
    string_[6] = string_fake[8]
    return string_
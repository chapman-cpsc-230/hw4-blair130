def H_eps(x):
    if x < 0:
        result = 0
    else:
        result = 1
    return result

def test_H():
    x_str = raw_input ("Enter the value of x:")
    x = float(x_str)
    print H_eps(x)

test_H()

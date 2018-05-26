"""
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print
the binary representation. If the number cannot be represented accurately in binary with at most 32
characters, print "ERROR:'
"""
import tensortools.testing as tt


def binary_from_double(doub):
    converted = 0
    for i in range(1, 31):
        doub = doub * 2
        if doub >= 1:
            converted += 1 / (10 ** i)
            doub -= 1

        if doub == 0:
            break
    else:
        print('ERROR')
        return

    print(converted)
    return converted


assert binary_from_double(0.5) == 0.1
assert binary_from_double(0.75) == 0.11
assert binary_from_double(0.875) == 0.111
assert tt.approx(binary_from_double(0.5625), 0.1001)

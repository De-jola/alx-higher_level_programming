#!/usr/bin/python3
def print_argv(argv):
    i = len(argv) - 1
    if i == 0:
        print("{:d} argument.".format(i))
        return
    else:
        if i == 1:
            print("{:d} argument:".format(i))
        else:
            print("{:d} arguments:".format(i))
        n = 1
        while n <= i:
            print("{:d}: {:s}".format(n, argv[n]))
            n += 1


if __name__ == "__main__":
    import sys
    print_argv(sys.argv)

import sys

def shrink(input_string):
    print(input_string[:8])

def enlarge(input_string):
    if len(input_string) == 8:
        print(input_string)
    else:
        print(input_string.ljust(8, 'Z'))

if len(sys.argv) < 2:
    print("none")
else:
    index = 1
    while index < len(sys.argv):
        param = sys.argv[index]
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)
        index += 1
input()
#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    argc = len(args) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "s" if argc > 1 else ""))
        for i in range(argc):
            print("{}: {}".format(i + 1, args[i + 1]))

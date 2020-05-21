import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-param1',    '--param1', dest = 'param1', type = float,   default=1.2)
    parser.add_argument('-param2',    '--param2', dest = 'param2', type = str,     default='DEFAULT')
    parser.add_argument('-param3',    '--param3', dest = 'param3', type = int,     default=1)
    args = parser.parse_args()

    print("args.param1 {}".format(args.param1))
    print("args.param2 {}".format(args.param2))
    print("args.param3 {}".format(args.param3))

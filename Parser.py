import argparse
def ParseCmd():
    parser = argparse.ArgumentParser(description='State input.')
    parser.add_argument('-l', '--list', metavar='N', type=int, nargs='+',
                        help='List of integers for state of 8-puzzle, e.g. 1 2 3 4 5 6 7 8 0\nAdd the spaces between!')

    args = parser.parse_args()._get_kwargs()
    return args[0][1]
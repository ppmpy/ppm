from argparse import ArgumentParser, Namespace

parser = ArgumentParser(
    description='Python Project manager parsers'
)

parser.add_argument(
    '-v', '--version',
    action='version',
    version='PPM: 0.0.0',
    help='Show version information'
)

parser.add_argument(
    '-i', '--init',
    action='store_true',
    default=False,
    help='Create a python project control',
)

parser.add_argument(
    '-a', '--about',
    action='store_true',
    default=False,
    help='About PPM',
)

parser.add_argument(
    '-u', '--update',
    action='store_true',
    default=False,
    help='Software update',
)

init_parser = parser.add_subparsers(dest='controls')
init_parser.add_parser(
    'init',
    help='Create a python project control',
    description='test'
)

if __name__ == '__main__':
    args: Namespace = parser.parse_args()
    print(args.command)

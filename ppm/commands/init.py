from argparse import Namespace
from pick import pick
from ppm.configure import parser
from ppm.projects import py_config

args:Namespace = parser.parse_args()

control = args.controls

if control == 'init':
    title = "Please choose a project type:"
    options = ["Python"]
    option, index = pick(options, title, indicator="->", default_index=0)
    py_config()

if control is None:
    print('Please specify command.')
    print('Use ppm --help for more information.')
    exit(1)
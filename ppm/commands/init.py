from argparse import Namespace
from pick import pick
from ppm.configure import parser
from ppm.projects import py_config

args:Namespace = parser.parse_args()

control = args.controls

if control == 'init':
    title = "Choose what type of project to be: "
    options = ["Python"]
    option, index = pick(options, title, indicator="->", default_index=0)
    py_config()

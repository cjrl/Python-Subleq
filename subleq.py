# Subleq Parser
# Copyright (C) 2013 Chris Lloyd
# Released under GNU General Public License
# See LICENSE for more details.
# https://github.com/cjrl
# lloyd.chris@verizon.net

from sys import argv
from subleq_parser import SubleqParser
from subleq_vm import SubleqVM

def execute_file(file_name):
    p = SubleqParser()
    SubleqVM.execute(p.parse(open(file_name).read()))

if len(argv) > 1:
    execute_file(argv[1])
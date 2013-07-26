# Subleq Virtual Machine 
# Copyright (C) 2013 Chris Lloyd
# Released under GNU General Public License
# See LICENSE for more details.
# https://github.com/cjrl
# This Subleq Virtual Machine was based on the pseudocode from the OSIC Wikipedia article:
# http://en.wikipedia.org/wiki/One_instruction_set_computer

class SubleqVM:
    @staticmethod 
    def execute(mem):
        pointer = 0
        running = True
        input_buffer = []
        while running:
            try:
                a = mem[pointer]
                b = mem[pointer+1]
                c = mem[pointer+2]
                if b == -1:
                    if not input_buffer:
                        input_buffer.extend(list(input()))
                    user_in = input_buffer.pop(0)
                    if user_in.isdigit():
                        mem[a] = int(user_in)
                    else:
                        mem[a] = int(ord(user_in)) 
                elif b == -2:
                    print(chr(mem[a]), end="")
                else:
                    mem[b] -= mem[a]
                if mem[b] > 0 or c == -1:
                    pointer += 3
                else:
                    if c == -2:
                        running = False
                    pointer = c
            except IndexError:
                running = False
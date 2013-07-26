Python Subleq Interpreter
==========================

Written by Chris Lloyd in Python 3.3

Released under the GNU General Public License

What is Subleq?
----------------
Simply put it's a one instruction language.
Learn more here:
- http://esolangs.org/wiki/Subleq
- http://mazonka.com/subleq/
- http://en.wikipedia.org/wiki/One_instruction_set_computer

Why Subleq?
--------------
I found it interesting that the subleq instruction is able to emulate many other common instructions seen in other languages such as assembly. After reading about it I wanted to play around with it, but I could only find a few parsers and interpreters so I wrote my own.

Contents Overview
-----------------
- SubleqParser: Takes subleq input and outputs integer array for the virtual machine
- SubleqVM: Interpreters output from SubleqParser 
- subleq.py: Provides command-line interface for interpreting subleq code

Basic Examples:
-----------
Create a file called input.subleq containing:
    
    # Hello world!
    # Taken with modifications from http://mazonka.com/subleq/

    # output *p; 
    a; p Z; Z a; Z
    a:0 -2

    # p++
    m1 p;

    #check if p<E
    a; E Z; Z a; Z;
    p a -2

    Z Z -2

    . p:H Z:0 m1:-1
    . H: "Hello, World!" 10 E:E

Make sure subleq.py, subleq_parser.py, and subleq_vm.py are in the same folder, then in the console type:
    ```
    python subleq.py input.subleq
    ```
This should produce the output Hello, World!

Implementation specifics
-------------------------
    # Special Characters 
    # ? pointers to the next instruction
    # . tells the parser the line has no instructions
    # : defines labels in the form label_name:

    # Implied Instructions
    a      # equals a a ?
    a b    # equals a b ?
    a b c  # equals a b c

    # Special Address Examples
    a -2   # outputs value stored at a, in this case 0
    a -1   # gets input and stores it in a
    z z -2 # exits the program by jumping to -2
    . z:0 a:0 
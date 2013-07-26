 # Subleq Parser
 # Copyright (C) 2013 Chris Lloyd
 # Released under GNU General Public License
 # See LICENSE for more details.
 # https://github.com/cjrl
 # lloyd.chris@verizon.net

class SubleqParser:

    tokens = []
    label_table = {}

    def parse(self,string):
        string = self.expand_literals(string)
        string = string.replace('\n',';')
        string = string.replace('#',';#')
        string = string.replace(':',': ')
        string = string.replace('.','. ')
        self.tokens = [token.split() for token in string.split(';') if not '#' in token and token.strip()]
        self.parse_labels()
        self.expand_instructions()
        self.update_labels()
        self.tokens = [token for token in sum(self.tokens,[]) if not token is '.']
        self.resolve_labels()
        return [int(token) for token in self.tokens]

    def resolve_labels(self):
        for i, token in enumerate(self.tokens):
            if token in self.label_table:
                self.tokens[i] = self.label_table[token]
            if token is '?':
                self.tokens[i] = i+1

    def update_labels(self):
        for i, label in enumerate(self.label_table):
            self.label_table[label] = self.get_label_index(label)

    def get_label_index(self,label):
        index = 0
        address, x = self.label_table[label]
        for i in range(address):
            index += len(self.tokens[i])
            if '.' in self.tokens[i][0]:
                index -= 1 
        if '.' in self.tokens[address][0]:
            return index + x - 1
        return index

    def expand_instructions(self):
        for token_index, token in enumerate(self.tokens):
            if not token[0] is '.':
                oprands = [token[0],token[0],-1]
                for i, oprand in enumerate(token):
                    oprands[i] = oprand
                self.tokens[token_index] = oprands

    def parse_labels(self):
        for token_index, token in enumerate(self.tokens):
            for oprand_index, oprand in enumerate(token):
                if ':' in oprand:
                    token.remove(oprand)
                    self.label_table[oprand[:-1]] = (token_index,oprand_index) 

    def expand_literals(self,string):
        in_literal = False
        expanded_string = ""
        for char in string:
            if char is '"' or char is "'":
                in_literal ^=True
            elif in_literal:
                expanded_string += str(ord(char)) + ' '
            else:
                expanded_string += char
        return expanded_string
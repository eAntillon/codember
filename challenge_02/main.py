class MiniCompiler():

    def __init__(self, source_code):
        self.source_code = source_code
        self.counter = 0
    def compile(self):
        for char in self.source_code:
            if char == '#':
                self.counter += 1
            elif char == '@':
                self.counter -= 1
            elif char == '*':
                self.counter *= self.counter
            elif char == '&':
                print(self.counter, end='')
            else:
                pass

if __name__ == '__main__':
    source_code = open('message_02.txt', 'r').read()
    compiler = MiniCompiler(source_code)
    compiler.compile()
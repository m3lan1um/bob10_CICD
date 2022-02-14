class Hello:
    def say(self):
        print('hello, world')
    
    def add(self, a, b):
        result = a + b
        print('x + y = {result}'.format(result=result))
        return result

if __name__ == '__main__':
    h = Hello()
    h.say()
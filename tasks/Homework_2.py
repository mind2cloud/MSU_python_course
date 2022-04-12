#Homework_2
def mult_func(N):
    def g(x):
        return x*N
    return g

def pow_func(N):
    def g(x):
        return x**N
    return g

Functions = {'mult': mult_func, 'pow': pow_func}
UserFunctions = {}

# func f mult 3

while(True):
    command = input()

    if command == '!q':
        break

    args = command.split()
    if (len(args) == 4):
        if (args[0] != 'func')
            print('wrong command')
            continue
        if args[2] in Functions:
            print('Wrong function type')
            continue
        if args[3].isdigit():
            print('Third argument must be a number')

        UserFunctions[args[1]] = Functions[args[2]](int(args[3]))
    if(len(args) == 2):
        if args[0] in UserFunctions:
            x = UserFunctions[args[0]](int(args[1]))
            print(x)
            continue
        else:
            print('wrong command')
            continue
    print('command isn\'t detected')

print('Bye!')
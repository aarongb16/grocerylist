import collections

def main():
    input_lines = []
    while True:
        try:
            l = input('> ')
            input_lines.append(l)
            input_lines.sort()
        except EOFError:
            break
    print('\n')
    
    contador = {}
    for product in input_lines:
        if product in contador:
            contador[product] += 1
        else:
            contador[product] = 1
    for key, value in contador.items():
        print(value,key.upper())

if __name__ == '__main__':
    main()


import sys

def rectangle(x, y, type_):
    if type_ == 'A':    
        if x < 1 or y < 1:
            print("El ancho y alto deben ser al menos 1 para dibujar un rectngulo.")
            return

        if y == 1:
            print('o' + '-' * (x - 2) + ('o'))
        else:
            print('o' + '-' * (x - 2) + ('o'))
            for i in range(y - 2):
                if x == 1:
                    print('|')
                else:
                    print('|' + ' ' * (x - 2) + '|')
        print('o' + '-' * (x - 2) + ('o'))

    elif type_ == 'B':
        if x < 1 or y < 1:
            print("El ancho y alto deben ser al menos 1 para dibujar un rectngulo.")
            return

        if y == 1:
            print('B' + '/' * (x - 2) + ('B'))
        else:
            print('B' + '/' * (x - 2) + ('B'))
            for i in range(y - 2):
                if x == 1:
                    print('/')
                else:
                    print('/' + ' ' * (x - 2) + '/')
        print('B' + '/' * (x - 2) + ('B'))

    elif type_ == 'C':
        if (x < 1 or y < 1):
            print("El ancho y alto deben ser al menos 1 para dibujar un rectngulo.")
            return

        if y == 1:
            print('0x' + 'A' * (x - 2) + ('x0'))
        else:
            print('0x' + 'A' * (x - 2) + ('x0'))
            for i in range(y - 2):
                if x == 1:
                    print('x0')
                else:
                    print('x0' + 'B' * (x - 2) + '0x')
        print('0x' + 'A' * (x - 2) + ('x0'))

    elif type_ is not ['A', 'B', 'C']:
        print("Tipo debe ser A, B o C")
        return

def main():
    if len(sys.argv) == 4:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            type_ = str(sys.argv[3]).upper()
            if type_ not in ['A', 'B', 'C']:
                print("Tipo debe ser A, B o C")
                return
            rectangle(x, y, type_)
        except ValueError:
            print("Los argumentos deben ser números enteros")
    else:
        print("Uso: python main.py <ancho> <alto> <tipo>")
        print("Tipo puede ser A, B o C")
        print("Ejemplo: python main.py 5 3 A")

if __name__ == "__main__":
    main()


print("Para conevertir una MAC de decimal a hexadecimal presione 1 (21252894938 --> 64:16:7F:4C:A1:E0),")
print("Para conevertir una MAC de hexadecimal a decimal presione 2 (64:16:7F:4C:A1:E0 --> 21252894938):")
selected=input()

if selected=='1':
    print('Ingrese la dirección MAC de tipo decimal:')
    try:
        MAC = int(input())
        print(f'La dirección MAC es: {(str(hex(MAC))).upper()}')
    except Exception as e:
        print(e)

if selected=='2':
    print('Ingrese la dirección MAC de tipo hexadecimal:')
    MAC = input()
    print(f'La dirección MAC es: {int(MAC, 16)}')
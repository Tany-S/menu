print ('Bienvenido al sistema')
  x = input ('Usario: ')
  contrasena = '12356' con = input ('Introduce la contraseC1a: ') while con
!=contrasena:
  print ('la contraseC1a no es correcta: ')
    cont = input ('intenta otra vez: ')
    print ('contraseC1a correcta') opcion = 0 while opcion
  !=5:
     print ('1.Division de 2 numeros')
      print ('2.Divisores')
      print ('3.Capicua')
      print ('4.Cambio de base')
      print ('5.Salir') opcion = int (input ('ingrese una opcion: ')) if
  opcion == 1
:
     a = float (input ('ingrese 1: '))
     b = float (input ('ingrese 2: '))
  c = 0 while a
!=0:
  d = b - a c = c + 1 print ('su resultado es:', d) if opcion
  == 2:
     c = int (input ('ingrese: ')) for
  i
  in
range (c)
  :if
    c %
    i == 0
  :
    print ('su divisor es: ') if opcion
    == 4:
     x = int (input ('ingrese numero:'))
     y = int (input ('cambio de base:')) while
  x !=
  0:
  d = x
  %y c = d * 10 print ('el cambio es:', c)

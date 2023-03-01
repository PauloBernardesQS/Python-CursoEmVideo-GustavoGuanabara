s = (input("\033[4;34mDigite algo:\033[m "))
print("\033[32mO valor de s é:\033[m ", (type(s)))
print("\033[32mO valor de s pode ser convertido a um valor numerico:\33[m ", s.isnumeric())
print("\033[32mO valor de s contem somente letras maiusculas:\033[m ", s.isupper())
print("\033[32mO valor de s contem somente letras minusuculas:\033[m ", s.islower())
print("\033[32mEsta capitalizada:\033[m ", s.istitle())
print("\033[32mO valor de s é um valor alfabetico:\033[m ", s.isalpha())
print("\033[32mO valor de s tem valor alfabetico e/ou numerico:\033[m ", s.isalnum())




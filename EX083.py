exp = input("Digite sua expressão matematica -> ")
if exp.count("(") == exp.count(")") and exp.count("[") == exp.count("]") and exp.count("{") == exp.count("}"):
    print("Sua expressão matematica esta valida!")
else:
    print("Sua expressão esta invalida!")
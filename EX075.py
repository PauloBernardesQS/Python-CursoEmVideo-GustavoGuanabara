produtos = ("Caneta1",1.35,
          "Caneta2",2.35,
          "Caneta3",3.35,
          "Caneta4",4.35,
          "Caneta5",5.35)
for prod in range(0, len(produtos)):
        if prod % 2 == 0:
                print(f"{produtos[prod]}")
        else:
                print(f"R${produtos[prod]}")

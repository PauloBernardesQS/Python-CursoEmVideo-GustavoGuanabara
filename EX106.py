while True:
    resp = input("Função ou Biblioteca -> ")
    if resp == "fim":
        break
    print(f"Processando dados sobre {resp}...")
    from time import sleep
    sleep(1)
    help(resp)
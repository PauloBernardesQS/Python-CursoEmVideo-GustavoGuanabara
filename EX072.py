times = ("Palmeiras", "Corinthias", "Atletico", "Fluminense", "Atletico-PR", "Internacional", "Flamengo", "Bragantino", "Santos", "São Paulo", "Ceara", "Botafogo", "Avai", "Goias", "America-MG","Atletico-Go", "Fortaleza", "Jucentude")
print(f"Os cinco primeiros colocados da seria a são: {times[0:5]}")
print(f"Os quatro ultimos colocados são: {times[-5::]}")
print(f"Times em ordem alfabetico {sorted(times)}")
print(f"O flamento esta na posição {times.index('Flamengo') + 1}")
""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time Corinthians. """
times = ("Palmeiras", "Grêmio", "Atlético - MG", "Flamengo", "Botafogo", "Bragantino", "Fluminense", "Athletico - PR",
         "Internacional", "Fortaleza", "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", "Vasco", "Bahia", "Santos",
         "Goiás", "Coritiba", "América - MG")
print("-=" * 20)
print(f"Lista de times do Brasileirão: {times}")
print("-=" * 20)
print(f"Os 5 primeiros são {times[0:5]}")
print("-=" * 20)
print(f"Os últimos 4 colocados são {times[-4:]}")
print("-=" * 20)
print(f"Os times em ordem alfabética são {sorted(times)}")
print("-=" * 20)
print(f"o Corinethians está na {times.index('Corinthians')} posição")
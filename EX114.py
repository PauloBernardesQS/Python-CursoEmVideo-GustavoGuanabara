
import urllib.request
try:
    url = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError:
    print("Erro na conexão com a internet ou a URL não foi encontrada")
else:
    print("Conexão Feita")
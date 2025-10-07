import requests, json

def apidolar():


    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    #requests vai pegar os dados no formato
    dados = requests.get(url, timeout=10).content

    cotação = json.loads(dados)

    return cotação['USDBRL']['ask']






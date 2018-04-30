#def nomefuncao(parametros):
def conversor(valdolar, valcotac):
    #processamento
    valreal = valdolar * valcotac
    return valreal

if __name__ == "__main__":
    #entradas
    print("Digite o valor em dolar")
    # float significa numero decimal
    valdolar = float(input())
    print("Digite o valor da cotacao do dolar em reais")
    valcotac = float(input())
    retorno = conversor(valdolar, valcotac)
    #saida
    print("O valor em reais e: ", retorno)

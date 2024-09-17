"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
o escopo global é o escopo onde todo o código é alcansável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1 #Escopo "global"

def escopo(): #Escopo 1
    global x
    x = 10

    def outra_funcao(): #Escopo 2
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x) #escopo global
escopo() #escopo 1 + 2 (pois tem a função x e y)
print(x) #escopo global passa a ser o x do escopo 1
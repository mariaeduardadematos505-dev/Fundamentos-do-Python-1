dic =  {
'nomes':['ana','julia'],
'idades':[20,18]


}



print(dic.keys())
print(dic.values())


for dados in dic.values():
    print(dados)


nome = input('nome: ')
idade = input('idade: ')



dic['nomes'].append(nome)
dic['idades'].append(idade)


print(dic)


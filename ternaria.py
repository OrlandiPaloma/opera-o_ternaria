idade = input('qual sua idade? ')

if not idade.isnumeric():
    print('você precisa digitar apenas numeros')
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
    msg = "Pode acessar" if maior_idade else "Não pode acessar"
    print(msg)

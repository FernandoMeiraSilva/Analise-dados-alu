# Manipulando dados
"""
idade = 5
print ("A idade é:", idade)

idade = 10
print ("A idade agora é:", idade)

idade = 15
print ("A idade agora é:", idade)

nome = 'Fernando'
print ("O nome é:", nome)
"""

# tipos de variaveis 
'''
i = 5
type(i)

f = 5.0
type(f)

s = 'Fernando'
type(s)

b = True
type(b)

nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_semestre = 8.45
situacao_aluno = True
print ("O aluno", nome_aluno, "tem", idade_aluno, "anos, sua média do semestre foi", media_semestre, "e sua situação é", situacao_aluno)
'''
#variaveis numericas
'''
seguranca = 5
s_seguranca = 3000

docente = 10
s_docente = 6000

diretoria = 1
s_diretoria = 12500

qtde_funcionarios = seguranca + docente + diretoria
soma_salarios = s_seguranca + s_docente + s_diretoria
print("A quantidade de funcionários é:", qtde_funcionarios)
print("A soma dos salários é:", soma_salarios)

diferenca_salario = s_diretoria - s_seguranca 
print('A diferença entre o maior salário e o menor salário é:', diferenca_salario)

media = (s_seguranca*seguranca + s_docente*docente + s_diretoria*diretoria) / qtde_funcionarios
print('A média salarial é:', media)
'''

#Strings
'''
s1 = 'Fernando'
s2 = 'Daniel'
print(type(s1), type(s2)) #type() mostra qual é o tipo de variavel que eu tenho 

#metodos
texto = 'Geovana Alessandra dias Sanyos'
texto.upper() #transforma todas as letras em maiusculas
texto.lower() #transforma todas as letras em minusculas
texto.strip() #remove os espaços em branco do inicio e do final da string
texto.replace('y', 't') #substitui a letra y pela letra t, mas pode substituir qualquer letra ou palavra

texto = texto.strip().replace('y', 't'). upper() 
texto 
'''
#chr(79) + chr(108) + chr(225) chr é usado para mostrar o caracter que corresponde ao numero da tabela ascii

#Coletando dados
'''
nome = input('Digite seu nome: ')   #quando precisa coletar um dados usamos o input()
nome 
idade = int(input('Digite sua idade: '))  #quando precisa que o dado seja de um tipo especifico, usamos o int() para inteiro, float() para decimal e str() para string
idade
print(type(idade))
'''
'''
ano_entrada= int(input('Digite o ano de entrada: '))

nota_entrada = float(input("Digite a nota do teste"))
print(f'Idade de entrada {ano_entrada} - nota do teste {nota_entrada}') # O f antes mostra para o codigo que vai ter inserção de valores e fica mais fácil de ser entendido para qm esta lendo o codigo. A outras maneiras de usar a formatação .format() e %s, %d, %f. ele ficaria assim print('Idade de entrada {} - nota do teste {}'.format(ano_entrada, nota_entrada)) ou print('Idade de entrada %d - nota do teste %.2f' %(ano_entrada, nota_entrada)) o %s é usado para string, %d para inteiro e %f para decimal. O .2f é usado para mostrar apenas 2 casas decimais.
'''
#Atividades
'''
nome = input('Qual é o seu nome?')
idade = int(input('Qual é a sua idade?'))
altura = float(input('Qual é a sua altura em metros? '))
print(f'Olá, {nome}, a sua idade é {idade} anos e a sua altura é: {altura}')
'''
#Atividade 2
'''
numb1 = int(input('Digite o primeiro número: '))
numb2 = int(input('Digite o segundo número: '))
numb3 = int(input('Digite o teceiro número:'))
resultado = numb1+numb2+numb3
print(f'O resultado dos dois números é: {resultado}')
'''
'''
numb1 = int(input('Digte o primeiro valor'))
numb2 = int(input('Digite o segundo valor'))
resultado = numb1-numb2
print(f'O resultado da subtração é {resultado}')
'''
'''
numb1 = int(input('Digite o primeiro valor'))
numb2 = int(input('Digite o segundo valor'))
resultado = numb2*numb1
print(f'O resultado da multiplicação dos números é {resultado}')
'''
'''
numb1 = int(input('Digite o primeiro valor mas ele não pode ser zero'))
numb2 = int(input('Digite o segundo valor mas ele não pode ser zero'))
resultado = numb1/numb2
print(f'O resultado da divisão do primeiro valor pelo segundo valor é {resultado}')
'''
'''
numb1 = int(input('Digite o número que vai ir na base '))
numb2 = int (input('Digite o número que vai ir no expoente'))
resultado = numb1**numb2
print(f'O resultado é {resultado}')
'''
'''
numb1 = int(input('Digite o primeiro número '))
numb2 = int(input('Digite o segundo número '))
resultado = numb1%numb2
print(f'O resultador é {resultado}')
'''
'''
nota1 = float(input('Digite a primeria nota'))
nota2 = float(input('Digite a segunda nota'))
nota3 = float(input('Digite a terceira nota'))
media = (nota1+nota2+nota3)/3
print(f'A média das notas né {media}')
'''
'''
nota1 = float(input('Digita a primeria nota'))
nota2 = float(input('Digite a segunda nota'))
nota3 = float(input('Digite a terceira nota'))
nota4 = float(input('Digite a quarta nota'))
media = ((nota1*5)+(nota2*12)+(nota3+20)+(nota4*15))/4
print(f'O resultado é {media}')
'''
'''
frase = str(input('escreva algo '))
print(f'A sua palavra foi {frase}')
'''
'''
texto = input('Digite algo ')
texto_maiusculo = texto.upper()
print(texto_maiusculo)
'''
'''
frase = input('Digite algo para tirar os espaços em branco ')
frase_espaco = frase.strip().lower()
print(frase_espaco)
'''
'''
frase = input('Digite algo')
frase = frase.replace('e', 'f') # precisa colocar a letra que vc quer trocar e depois vc coloca a letra que vc quer colocar no lugar dela 
print(frase)
'''
'''
frase = input('Digita algo')
frasea = frase.replace('a', '@')
print(frasea)
'''
'''
frase = input('Digita algo')
frasea = frase.replace('s', '$')
print(frasea)
'''

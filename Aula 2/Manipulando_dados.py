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
ano_entrada= int(input('Digite o ano de entrada: '))

nota_entrada = float(input("Digite a nota do teste"))
print(f'Idade de entrada {ano_entrada} - nota do teste {nota_entrada}') # O f antes mostra para o codigo que vai ter inserção de valores e fica mais fácil de ser entendido para qm esta lendo o codigo 


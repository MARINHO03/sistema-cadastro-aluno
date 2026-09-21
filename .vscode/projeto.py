def cadastrar_alunos():
    turma=int(input('quantos alunos tem na turma?: '))
    alunos=[]
    for i in range(turma):
        nome=input('digite seu nome: ')
        idade=int(input('digite sua idade:'))
        nota=float(input('digite sua media:'))
        alunos.append({"nome":nome, "idade":idade, "nota":nota })
    print(alunos)   
    return alunos
alunos=cadastrar_alunos()
soma=0
for aluno in alunos:
    soma= soma +aluno['nota']

media = soma / len(alunos)
def buscar_aluno (alunos):
    nome_busca=input('digite o aluno que deseja encontrar: ')
    for  aluno in alunos:
        if aluno ['nome'] == nome_busca:
            print(aluno)
            return aluno
    print('aluno não encontrado')
    return None 

def alunos_removidos (alunos):
    nome_remover=input('digite o aluno que deseja remover:')
    for i, aluno in enumerate(alunos):
        if aluno['nome'] == nome_remover:
            removido=alunos.pop(i)
            print(f'o aluno removido foi: {removido}')
            return(removido)
    print( 'aluno não encontrado')
    return None
while True:
    print('1- adicionar aluno')
    print('2- buscar aluno')
    print('3- listar alunos')
    print('4- remover aluno')
    print('5- media da turma')
    print('6- sair')
    opcao = input('digite a opção desejada: ')

    if opcao == '1':
        adicionar_aluno(alunos)
    elif opcao =='2':
        buscar_aluno(alunos)

    elif opcao =='4':
        alunos_removidos(alunos)
    elif opcao == '5':
       soma=0
       for aluno in alunos:
            soma= soma + aluno['nota']
       media = soma / len(alunos)
       print(f' a media da turma é {media:.2f}') 
    elif opcao == '6': 
        print('saindoo...')
        break
    else:
        print('opcao invalida')


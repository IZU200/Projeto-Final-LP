def cadastrar_alunos(alunos):
 matricula = imput("Matrícula do aluno: "). strip()
    if matricula in alunos:
        print("Aluno já cadastrado!")
    return
Nome = imput("nome do aluno: "). strip()
alunos[martricula] = {"nome": nome, "disciplinas": set(), "notas: {}}
print (f"aluno {nome} cadastro com matrícula {matricula}.")

def cadastrar_disciplina(disciplinas):
    for cod, notas in alunos[matricula]["notas"].items():
        if notas:
            medias.append(sum(notas) / len(notas))
            if not medias
            print("Aluno não possui notas cadastradas.")
    return None
    return sum(medias) / len(medias)

def aprovado_em_todas(alunos, matricula):
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return None
        for cod, notas in alunos[matricula]["notas"].items():
            if notas:
                media = sum(notas) / len(notas)
                if media < 6.0:
                    return False
                else:
                    return False
                    return True

def alterar_nome_aluno(alunos):
    matricula = input("Matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return
        novo = input("Novo nome: ").strip()
        alunos[matricula]["nome"] = novo
        print("Nome alterado com sucesso.")

def alterar_nome_disciplina(disciplinas):
    codigo = input("Código da disciplina: ").strip()
    if codigo not in disciplinas:
        print("Disciplina não encontrada!")
        return
        novo = input("Novo nome: ").strip()
        disciplinas[codigo]["nome"] = novo
        print("Nome da disciplina alterado com sucesso.")

def excluir_aluno(alunos, disciplinas):
    matricula = input("Matrícula do aluno a excluir: ").strip()
    if matricula not in alunos:
        print("Aluno não encontrado!")
        return
        for cod in alunos[matricula]["disciplinas"]:
            if cod in disciplinas:
                disciplinas[cod]["alunos"].discard(matricula)
                del alunos[matricula]
                print("Aluno excluído.")

def excluir_disciplina(disciplinas, alunos):
    codigo = input("Código da disciplina a excluir: ").strip()
    if codigo not in disciplinas:
        print("Disciplina não encontrada!")
        return
        for m in disciplinas[codigo]["alunos"]:
            if m in alunos:
                alunos[m]["disciplinas"].discard(codigo)
                alunos[m]["notas"].pop(codigo, None)
                del disciplinas[codigo]
                print("Disciplina excluída.")

                      

        

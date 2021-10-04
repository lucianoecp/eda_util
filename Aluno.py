class Aluno:
    def __init__(self, nome: str, n1: float , n2: float):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.media= (n1*2 + n2*3) / (3+2)

    def exibe_aluno(self):
        print(f"Nome do aluno: {self.nome}\nNota 1: {self.n1}\nNota 2: {self.n2}\nMedia: {self.media}\n")  

def input_aluno():
    nome = input("Digite o nome: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    return Aluno(nome,n1,n2)

def copia_alunos(lst_alunos):
    L = []
    for a in lst_alunos:
        L.append(a)

    return L



def ger_lst_alunos():

    lst_alunos = []

    lst_alunos.append(Aluno('Crystal Miguéis Carmo',5.5, 7.8))
    lst_alunos.append(Aluno('António Caires Sanches',6, 9))
    lst_alunos.append(Aluno('Rute Duarte Velasco',5, 9.5))
    lst_alunos.append(Aluno('Antônio Barrocas Milhães',10, 8))
    lst_alunos.append(Aluno('Angélico Assis Azevedo',7.3,6.7))
    lst_alunos.append(Aluno('Sara Miranda Roriz',8.5,8))
    lst_alunos.append(Aluno('Ivy Luz Meneses',6,7.9))
    lst_alunos.append(Aluno('Kyle Soverosa Laranjeira',5.1,9.2))

    return lst_alunos

def get_atr_media(a):
    ps1=2
    ps2=3
    return (a.n1*ps1 + a.n2*ps2) / (ps1+ps2)

def lista_alunos(alunos):
    cont = 0
    for a in alunos:
        cont+=1
        print(f'[{cont}]')
        a.exibe_aluno()

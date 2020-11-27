class Pessoa(object):
    def __init__(self, IDPessoa, Nome, Sobrenome, Nascimento, CPF, RG, Telefone, Rua, Numero, Complemento, Cidade, Estado, TipoPessoa):
        self.IDPessoa = IDPessoa
        self.Nome = Nome
        self.Sobrenome = Sobrenome
        self.Nascimento = Nascimento
        self.CPF = CPF
        self.RG = RG
        self.Telefone = Telefone
        self.Rua = Rua
        self.Numero = Numero
        self.Complemento = Complemento
        self.Cidade = Cidade
        self.Estado = Estado
        self.TipoPessoa = TipoPessoa

class Funcionario(Pessoa):
    def __init__(self,IDFunc,IDPessoa, Nome, Sobrenome, CPF, RG, Telefone, Rua, Numero, Complemento, Cidade, Estado, TipoPessoa, Cargo, Salario, JornDeTrab, Setor):
        super().__init__(IDPessoa, Nome, Sobrenome, CPF, RG, Telefone, Rua, Numero, Complemento, Cidade, Estado, TipoPessoa)
        self.IDFunc = IDFunc
        self.Cargo = Cargo
        self.Salario = Salario
        self.JornDeTrab = JornDeTrab
        self.Setor = Setor

class Usuario(Funcionario):
    def __init__(self, IDFunc, login, senha, status):
        super().__init__(IDFunc)
        self.__login = login
        self.__senha = senha
        self._status = status


class MostraMais(Funcionario):

    def mostrafunc(self):
        print(f'O funcionário com código:{self.IDFunc}, Nome: {self.Nome}, Sobrenome: {self.Sobrenome},CPF: {self.CPF}, possui o cargo de {self.Cargo} e salário R${self.Salario} trabalhando na parte da {self.JornDeTrab} no setor {self.Setor}')
        return


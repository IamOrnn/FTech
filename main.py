from cadastros import Pessoa, Funcionario, MostraMais

Enzo = Pessoa(2, 'Enzo', 'Carlos', 19760616, 66692648793, 465727578, 21988988422, 'Rua Javari', 703, '', 'Duque_de_Caxias', 'Duque_de_Caxias', 'Funcionario')
EnzoFunc = Funcionario(1, Enzo.IDPessoa, Enzo.Nome, Enzo.Sobrenome, Enzo.Nascimento, Enzo.CPF, Enzo.RG, Enzo.Telefone, Enzo.Rua, Enzo.Numero, Enzo.Complemento, Enzo.Cidade, Enzo.Estado, Enzo.TipoPessoa, 'Ajudante', 1200, 'Manha', 'Curral')

EnzoFunc.mostrafunc()

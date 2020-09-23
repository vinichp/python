# -*- coding: UTF-8 -*-
def cadastrar(nomes):
	print 'Digite o nome'
	nome = raw_input()
	nomes.append(nome)

	
def listarNomes(nomes):
	print 'listando nomes'
	for nome in nomes:
		print nome
		
def removerNome(nomes):
	print 'Digite o nome a ser removido'
	nome = raw_input()
	nomes.remove(nome)
	
def alterarNome(nomes):
	print 'Digite o nome a ser alterado'
	nome = raw_input()
	if(nome in nomes):
		print('nome existe na lista')
		print('Digite um nome nome:')
		novo_nome = raw_input()
		index = nomes.index(nome)
		nomes[index] = novo_nome
	else:
		print('nome nao existe na lista')
		
def procurar(nomes):
	print 'Digite o nome a ser procurado'
	nome = raw_input()
	if(nome in nomes):
		print('nome existe na lista')
		index = nomes.index(nome)
		print 'na posicao %s' % index
	else:
		print('nome nao existe na lista')
			
	
	
def menu():
	nomes = []
	escolha = ''
	while(escolha != '0'):
		print 'Digite: 1 para cadastrar, 2 para listar nomes, 3 para remover um nome, 4 para alterar um nome, 5 para procurar, 0 para terminar'
		escolha = raw_input()
		if(escolha == '1'):
			cadastrar(nomes)
		if(escolha == '2'):
			listarNomes(nomes)
		if(escolha == '3'):
			removerNome(nomes)	
		if(escolha == '4'):
			alterarNome(nomes)	
		if(escolha == '5'):
			procurar(nomes)	
				
menu()				
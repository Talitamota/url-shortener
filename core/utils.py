from string import ascii_letters, digits

from random import choice, randrange

dados = ascii_letters + digits

def gera_hash():
	return ''.join(choice(dados) for i in range(randrange(5,11)))
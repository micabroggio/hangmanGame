# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.letc = []
		self.lete = []


	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word and letter not in self.letc:
			self.letc.append(letter)
			return True
		elif letter not in self.word:
			self.lete.append(letter)
			return False
		else:
			print('\nEssa letra já foi escolhida anteriormente.')
			print('Escolha outra.')
			return False


	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if len(self.lete) < 6:
			return False
		else:
			return True


	# Método para verificar se o jogador venceu
	def hangman_won(self):
		ind = []
		for i in self.letc:
			for ind2, char in enumerate(self.word):
				if char == i:
					ind.append(ind2)
		if len(ind) == len(self.word):
			return True
		else:
			return False


	# Método para não mostrar a letra no board
	def hide_word(self):
		new_hide = list('_' * len(self.word))
		for i in self.letc:
			ind = []
			for ind2, char in enumerate(self.word):
				if char == i:
					ind.append(ind2)
			for j in ind:
				new_hide[int(j)] = i
		print('"' + "".join(new_hide) + '"')

	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.lete)])


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("E:\\backup\\apostilas_e_cursos\\cursos\\python_fundamentos_para_analise_dados\\cap05\\lab03\\palavras.txt", "rt") as f:
            bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())
	print('\n\n>>>>>>>>>>Hangman<<<<<<<<<<')

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while game.hangman_won() is False and game.hangman_over() is False:

		# Verifica o status do jogo
		game.print_game_status()

		print('\nPalavra')
		game.hide_word()

		print("\nletras corretas:")
		print(game.letc)

		print("\nletras incorretas:")
		print(game.lete)

		letra = str(input("\nEscolha uma letra:"))

		if game.guess(letra) is True:
			print('\nletra correta')
		else:
			if len(game.lete) < 6:
				print('\nletra incorreta')
				print('Você tem mais ' + str(6-len(game.lete)) + ' tentativas.')
			else:
				print('\nletra incorreta')

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won() is True:
		print('\n==============================')
		print('Parabéns! Você venceu!')
		print('A palavra era ' + game.word)
		print('==============================')
	else:
		game.print_game_status()
		print('\n==============================')
		print('Game over! Você foi enforcado.')
		print('A palavra era ' + game.word)
		print('==============================')
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
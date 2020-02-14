# -* condig: utf-8 *-
# Forca game
# By Adcode



def sorted_word_game(file='comida.txt'):
    from random import choice
    import os

    db_file = '/home/junior/Dropbox/Scripts/Python/learn_path/DSA_ACADEMY/05_OOP/forca_game/'

    with open(db_file + file, 'r') as db_file:
        data = db_file.read()

        return choice(data.split('\n'))





class Grafico:

    # Atributos

    person = [
        """
     _____
    |   |
    O   |
        |
        |
        |
      _____
    """,
        """
     _____
    |   |
    O   |
    |   |
        |
        |
      _____
    """,
        """
     _____
    |   |
    O   |
    |   |
   /|   |
        |
      _____
    """,
        """
     _____
    |   |
    O   |
    |   |
   /|\\ |
        |
      _____
    """,
        """
     _____
    |   |
    O   |
    |   |
   /|\\ |
    |   |
      _____
    """,
        """
     _____
    |   |
    O   |
    |   |
   /|\\ |
    |   |
   /  _____
    """,
        """
     _____
    |   |
    O   |
    |   |
   /|\\ |
    |   |
   / \\_____
    """
    ] # Modelagem do inforcado
    line_board = sorted_word_game()
    word_game_split = [char for char in line_board]

    def __init__(self):
        """""
            Constructor criado para inicializar o grafico do jogo com a palavra sorteada.
        """""
        print(f'{"=-" * 50}')
        print('Bem vindo !'.rjust(50))
        print('Jogo da Forca V1'.rjust(53))
        print(f'{"=-" * 50}')


    def print_grafic(self, lvl_inforc: (int), round: (int), player_word_list: [list] ):
        """
            Este método será utilizado para exibir o grafico do jogo,
            sempre que chamado.
            Quando está na primeira rodada do game, não e printado as letras do player.
        """
        # Printando o grafico do enforcado
        try:
            print(f'{self.person[lvl_inforc]}', end='')
        except IndexError:
            pass

        # Quando a rodada começar, não executar o print das letras do player.
        if not round == 0:
            # Printando letras do usuario.
            for char in player_word_list:
                print(f'{char} ', end='')


    def print_table_word(self):
        print(1)



class Game_rule(Grafico):
    """
    Esta classe será responsavel por modelar o desenho do enforcado,
    atráves do erro ou do acerto do jogador, para cada jogada, será
    executado um desejo com o status atual.
  """

    # Atributos
    word_game = sorted_word_game()  # Sorteando a palavra para o game.
    player_char_current = ''  # Ira armazenar o caractere armazenado pelo usuário.
    word_game_split = [char for char in word_game]  # Ira armazenar a palavra escolhida, de forma separada
    # TODO Verificar por que esta variavel foi criada
    final_word_to_win = word_game_split.copy()

    player_word_list = [str() for x in range(len(word_game_split))]  # Ira armazenar as letras do usuario.
    POINT_CURRENT = 0 # Recebe o número de acertos na jogada atual
    LEVEL_INFORC = 0  # Quantidade maxima de erros que se pode obter == 7
    MAX_POINT_PLAYER = len(word_game_split) # Quantidade maxima de pontos na rodada que o jogador podera fazer
    CURRENT_ROUND = 0 # Armazenara o número atual da rodada.
    ROUND_SIZE = len(final_word_to_win)# Tamanho do round atual ( Baseado no tamanho da palavra sorteada)


    def get_play_round(self):
        """""
            Ler caractere inserido pelo player e modifica  o atributo '__play_char_current'
            Soma 1 n round atual.
        """""
        # Lendo jogada
        self.player_char_current = input('\nInforme um letra: ').lower()  # Obtendo resposta do jogador
        self.CURRENT_ROUND += 1


    def update_play_list(self):
        """""
            Atualiza a lista de palavras do jogador, com novas letras.
            point_number: Numero de acertos na rodada atual.point_number: int
        """""

        #char_count = self.__word_game_split.count(self.__player_char_current)

        index_current = 0
        index_current_list = [] # Ira servir como lista auxiliar para coletar dentro do looping index das ocorrencias de palavras

        # Pegar o index de todas as posições (Se existir mais de uma), e armazenar em uma lista.
        while True:
            if self.player_char_current in self.word_game_split:
                #  Pegando o index da letra atual e adicionando na lista.
                index_current_list.append(self.word_game_split.index(self.player_char_current))
                index_current = self.word_game_split.index(self.player_char_current)
                # Adicionado Nulo no index a qual o player acertou a palavra.
                self.word_game_split[index_current] = ''
            else:
                break

        # Atualizando lista da palavra do player.
        for element in index_current_list:
            self.player_word_list[element] = self.player_char_current

        print(f'Lista usuario: {self.player_word_list}')


    def check_status_game(self):

        if self.player_word_list == self.final_word_to_win:
            self.print_grafic(self.LEVEL_INFORC, self.CURRENT_ROUND, self.player_word_list)
            print('\nParabens você ganhou')
            print(f'A palavra foi {self.word_game}')
            exit(0)
        elif self.LEVEL_INFORC == 7:
            self.print_grafic(self.LEVEL_INFORC, self.CURRENT_ROUND, self.player_word_list)
            print('\nVoce perdeu !')
            print(f'A palavra era {self.word_game}')
            exit(0)


    def update_player_chance(self):
        """""
            Verifica se o jogador acertou ou não a palavra.
            Caso tenha acertado, será verificado a quantidade de letras acertadas.
            Caso não, o nivel do enforcamento ira aumentar.
        """""
        # Caso o jogador tenha acertado
        if self.player_char_current in self.final_word_to_win:
            # Verificando quantos caracteres o jogador acertou
            self.POINT_CURRENT = self.final_word_to_win.count(self.player_char_current)
        else:
            self.LEVEL_INFORC += 1 # Caso o jogador tenha errado, o nivel de enforcamento ira aumentar.

        print(f'Quantidade de erros: {self.LEVEL_INFORC}')
        print(f'Quantidade de letras acertadas: {self.POINT_CURRENT}')



class Main(Game_rule, Grafico):
    def __init__(self):
        super().__init__() # Chamando o constructor da subclass


    def play(self):
        for round in range(self.ROUND_SIZE):
            self.print_grafic(self.LEVEL_INFORC, self.CURRENT_ROUND, self.player_word_list)
            self.get_play_round()
            self.update_play_list()
            self.update_player_chance()
            self.check_status_game()




    # TODO Codificar fluxo do game.
    # TODO Verificar erro ou acerto.
    # TODO Preencher letra ou exibi menssagem de erro.
    # TODO Em caso de acerto atualizar grafico com letra.
    # TODO Verificar se jogador ganhou ou perdeu.



g1 = Main()
g1.play()





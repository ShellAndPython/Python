def sort_word(file='nomes.txt'):
    from random import choice

    db_file = '/home/junior/Dropbox/Scripts/Python/' \
              'learn_path/DSA_ACADEMY/05_OOP/forca_game/'

    with open(db_file + file, 'r') as db_file:
        data = db_file.read()

        return choice(data.split('\n')).strip()


person = [
    """
    +___+
    |   |
        |
        |
        |
        |
        |
        |
    ========
    """,
    """
    +___+
    |   |
    O   |
    |   |
        |
        |
        |
        |
    ========
    """,
    """
    +___+
    |   |
    O   |
    |   |
   /|   |
        |
        |
        |
    ========
    """,
    """
    +___+
    |   |
    O   |
    |   |
   /|\  |
        |
        |
        |
    ========
    """,
    """
    +___+
    |   |
    O   |
    |   |
   /|\  |
    |   |
        |
        |
    ========
    """,
    """
    +___+
    |   |
    O   |
    |   |
   /|\  |
    |   |
   /    |
        |
    ========
    """,
    """
    +___+
    |   |
    O   |
    |   |
   /|\  |
    |   |
   / \  |
        |
    ========
    """
]


class ForcaGame:

    def __init__(self, word):
        self.word_split = [char for char in word]
        self.list_player_word = ['_' for char in range(len(word))]
        self.inforcado_level = 0  # Para controlar o print do enforcado
        self.GAME_OVER = len(word)  # Nivel maximo de tentativas
        self.round = 0  # Rodada atual
        self.point = 0  # Letras acertadas na rodada atual
        self.correct_word = wrong_word = 0  # Contador de acertos e erros

        # Armazena letras acertadas e erradas
        self.char_dict = {'char_good': [],
                          'char_bad': [],
                          }

        self.play(word)


    def play(self, word):
        try:
            while self.GAME_OVER != 0:
                self.print_grafic_game(word)  # Boas vindas
                self.set_resp_player()  # Ler letra do jogador
                self.update_game_status()  # Atualizar status do game
                self.check_final_game(word)  # Checar se jogador ganhou
        except KeyboardInterrupt:
            print('\n\nJogo encerrado !')
            exit(0)

    def print_grafic_game(self, word):

        self.clear_scream()
        if self.round == 0:
            print('JOGO DA FORCA')
            print()
            try:
                print(person[self.inforcado_level])
            except IndexError:
                pass
            self.print_char_player(word)
            print()
        else:
            self.print_char_used()
            try:
                print(person[self.inforcado_level])
            except IndexError:
                pass
            self.print_char_player(word)
            print()

    def print_char_player(self, word):
        print(f'Um nome que possui {len(word)} letras: ', end='')
        for line in self.list_player_word:
            print(f'{line}', end='')
        print()


    def print_char_used(self):
        print()
        print('Letras acertadas: ')
        for char in self.char_dict['char_good']:
            print(f'{char} ', end='')
        print()
        print()
        print('Letras Erradas: ')
        for char in self.char_dict['char_bad']:
            print(f'{char} ', end='')


    def set_resp_player(self):
        self.player_char = input('Digite uma letra: ').lower()


    def update_game_status(self):
        self.update_round()  # Atualiza round atual do game
        self.check_char_player(self.player_char)


    def check_char_player(self, char):
        if char in self.word_split and not self.check_char_iqual():
            self.char_dict['char_good'].append(char)
            self.update_point_round()  # Atualiza os acertos do round atual
            self.update_player_list()  # Atualiza a lista do jogador
            self.update_word_split()  # Atualiza a palavra base
        elif self.check_char_iqual(): # Caso a palavra seja repetida
            pass
        else:
            self.char_dict['char_bad'].append(self.player_char)
            self.update_inforc()
            self.update_lost_chance()


    def check_char_iqual(self):
        """
        Criado para checar se a palavra ja existe
        :return: True se o caractere ja foi digitado
        """
        if self.player_char in self.char_dict['char_good'] or \
                self.player_char in self.char_dict['char_bad']:
            return True


    def check_final_game(self, word_game):
        print(self.list_player_word)
        if ''.join(self.list_player_word) == word_game:
            self.print_grafic_game(word_game)
            print(f'Parabens voce ganhou a palavra era "{word_game}"\n\n')
            exit(0)
        elif self.GAME_OVER == 0:
            self.print_grafic_game(word_game)
            print(f'voce perdeu, a palavra era "{word_game}"\n\n')
            exit(0)


    def update_lost_chance(self):
        self.GAME_OVER -= 1


    def update_player_list(self):
        for index, char in enumerate(self.word_split):
            if char == self.player_char:
                self.list_player_word.pop(index)
                self.list_player_word.insert(index, char)


    def update_word_split(self):
        for index, char in enumerate(self.word_split):
            if char == self.player_char:
                self.word_split[index] = ''


    def update_point_round(self):
        self.point = self.word_split.count(self.player_char)


    def update_round(self):
        self.round += 1


    def update_inforc(self):
        self.inforcado_level += 1


    def clear_scream(self):
        from os import system
        system('cls || clear')

def main():

    player = ForcaGame(sort_word())


if __name__ == '__main__':
    main()

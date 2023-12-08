import random

# Oyun tahtası boyutları
BOARD_SIZE = 3

# Oyun tahtası
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# Oyunu başlatan fonksiyon
def start_game():
    print('X Oyununa Hoş Geldiniz!')
    print('Oyun Tahtası Boyutu: {}x{}'.format(BOARD_SIZE, BOARD_SIZE))
    print_board()
    play_game()

# Oyun tahtasını ekrana yazdıran fonksiyon
def print_board():
    for row in board:
        print('|'.join(row))

# Oyuncunun hamlesini alıp işleyen fonksiyon
def get_move(player):
    while True:
        move = input('{} için hamlenizi girin (örn. 1,2): '.format(player))
        try:
            x, y = move.split(',')
            x = int(x) - 1
            y = int(y) - 1
            if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
                print('Hatalı hamle, lütfen tekrar deneyin.')
                continue
            if board[x][y] != '-':
                print('Bu hücre dolu, lütfen tekrar deneyin.')
                continue
            return x, y
        except ValueError:
            print('Hatalı hamle, lütfen tekrar deneyin.')

# Oyunu oynatan fonksiyon
def play_game():
    players = ['X', 'O']
    current_player = random.choice(players)
    while True:
        print('{} sırası.'.format(current_player))
        x, y = get_move(current_player)
        board[x][y] = current_player
        print_board()
        if check_win(current_player):
            print('{} kazandı!'.format(current_player))
            break
        if check_draw():
            print('Berabere!')
            break
        current_player = players[(players.index(current_player) + 1) % len(players)]

# Kazananın kontrolünü sağlayan fonksiyon
def check_win(player):
    # Satırları kontrol et
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Sütunları kontrol et
    for i in range(BOARD_SIZE):
        if all([board[j][i] == player for j in range(BOARD_SIZE)]):
            return True

    # Çaprazları kontrol et
    if all([board[i][i] == player for i in range(BOARD_SIZE)]) or all([board[i][BOARD_SIZE-1-i] == player for i in range(BOARD_SIZE)]):
        return True

    return False

# Beraberliği kontrol eden fonksiyon
def check_draw():
    return all([cell != '-' for row in board for cell in row])

# Oyunu başlat
start_game()
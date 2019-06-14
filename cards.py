import random

class Card:

    def __init__(self, i, f, n):
        self.index = i
        self.face = f
        self.number = n

    def __str__(self):
        return (str(self.number) + ' of ' + self.face)


class Deck:

    def __init__(self):
        self.cards = []
        faces = ['Spade', 'Club', 'Heart', 'Diamond']
        for i in range(4):
            for n in range(1, 14):
                self.cards.append(Card(i*n, faces[i], n))

    
    def draw(self):
        drawn_card = random.choice(self.cards)
        del self.cards[drawn_card.index]
        return drawn_card
    
class Player:

    def __init__(self):
        self.cards = []
        self.value = {}

    def assign(self, card):
        self.cards.append(card)

    def __str__(self):
        res_str = ''
        for card in self.cards:
            res_str += card.face[0] + '-' + str(card.number) + " "
        return res_str

class TeenPati:

    # __win_order = {'all': 0, 'seq': 0, 'flush': 0, 'two_pair': 0, 'highest': 0}

    def __init__(self, playerCount):
        self.deck = Deck()
        self.players = []
        for _ in range(playerCount):
            self.players.append(Player())

    def start(self):
        plist = [self.players * 3]

        for pgroup in plist:
            for player in pgroup:
                player.assign(self.deck.draw())

    def evaluate(self, player):
        cards = player.cards
        c1, c2, c3 = (cards[0], cards[1], cards[2])
        assorted = [c1.number, c2.number, c3.number]
        assorted.sort()
        if c1.number == c2.number and c1.number == c3.number:
            return 'all'
        elif (assorted[0] + 1) == assorted[1] and (assorted[0] + 2) == assorted[2]:
            return 'seq'
        elif c1.face == c2.face and c1.face == c3.face:
            return 'flush'
        elif c1.number == c2.number or c1.number == c3.number:
            return 'two_pair'
        else:
            return 'highest'

    def see(self):
        for player in self.players:
            print(self.evaluate(player))

    def winner(self):
        for player in self.players:
            print('h')


game = TeenPati(2)
game.start()
game.see()
print(game.players[0])
print(game.players[1])

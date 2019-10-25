from mamba import description, context, it
from expects import expect, equal

class Game(object):
    def __init__(self, player1, player2):
        pass

    def score(self):
        return (0, 0)

with description('Tennis') as self:
    with it('starts with 0 - 0 score'):
        rafa_nadal = "Rafa Nadal"
        roger_federer = "Roger Federer"
        game = Game(rafa_nadal, roger_federer)

        expect(game.score()).to(equal((0, 0)))

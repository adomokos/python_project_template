from mamba import description, context, it
from expects import expect, equal

from sample.tennis import Game

with description('Tennis') as self:
    with context('for an even score'):
        with it('starts with 0 - 0 score'):
            rafa_nadal = "Rafa Nadal"
            roger_federer = "Roger Federer"
            game = Game(rafa_nadal, roger_federer)

            expect(game.score()).to(equal((0, 0)))

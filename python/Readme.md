Why Classes Exist:

Imagine you're making a game.

Without classes:

player1_name = "Noman"
player1_health = 100

player2_name = "Ali"
player2_health = 80

Now imagine 100 players.

Chaos.

With classes:

class Player:
    pass

Now you can create:

p1 = Player()
p2 = Player()
p3 = Player()

One blueprint.
Many objects.

Think:

Class = Building blueprint
Object = Actual building
__author__ = 'sabatha'


class DodgeBall:
    def __init__(self, n, k, l, balls):

        self.n = n  # The number of blocks on the court (width)
        self.k = k  # The number of block the player occupies
        self.l = l  # Time the game takes in seconds

        self.balls = balls  # The position in which the ball will be thrown

        self.court = self.create_court()  # List containing the court blocks from 1 to n, from left to right
        self.player = self.create_player()  # List containing the block numbers the player occupies

    def play_game(self):
        """
        We need to pop the first value from self.balls every time a shot is fired.
        """
        game_over = 0
        time = 0
        o = self.l  # Store the original time safely
        while self.l > game_over:

            a = self.control_player()

            if self.l == 0:
                print 'Complete'
            elif time == o:
                print 'complete'
                return 'time: %s' % time
            elif not a:
                time += 1
                if time == o:
                    print 'Complete'
                return 'lasted %s seconds' % time
            else:
                self.l -= 1
                time += 1
                x = self.balls[0]
                self.balls.remove(x)

    def create_court(self):
        court = {}
        for x in range(1, self.n + 1):
            court[x] = x
        c = court.values()
        return c

    def create_player(self):
        player = {}
        for x in range(1, self.k + 1):
            player[x] = x
        p = player.values()
        return p

    def move_player(self, direction):
        if direction == 'right':
            pp = [v + 1 for v in self.player]  # We add 1 to each space the player occupies
            for x in pp:
                if x > self.court[-1]:  # i cannot be larger than the last block on the court
                    return False
                else:
                    return pp
        elif direction == 'left':
            pp = [v - 1 for v in self.player]
            for x in pp:
                if x < 1:  # i cannot be smaller than 1 as 1 is the first block on the court
                    return False
                else:
                    return pp

    def control_player(self):
        b = self.balls[0]
        p = self.player[-1]
        f = self.player[0]

        if b > p + 2:
            if self.move_player('right'):
                self.player = self.move_player('right')
                return True
            pass
        elif b < p - 2:
            if self.move_player('left'):
                self.player = self.move_player('left')
                return True
            pass
        elif b > p + 1:
            if self.move_player('right'):
                self.player = self.move_player('right')
                return True
            pass
        elif b < f - 1:
            if self.move_player('left'):
                self.player = self.move_player('left')
                return True
            pass
        elif b > p:
            if self.move_player('right'):
                self.player = self.move_player('right')
                return True
            pass
        elif b < f:
            if self.move_player('left'):
                self.player = self.move_player('left')
                return True
            pass
        elif self.court[-1] == p:
            if self.move_player('left'):
                self.player = self.move_player('left')
                return True
            pass
        elif self.court[0] == f:
            if self.move_player('right'):
                self.player = self.move_player('right')
        else:
            return False

while True:
    y = raw_input('court-size player-size time')
    z = raw_input('balls')

    y = y.split()
    z = z.split()

    y = [int(i) for i in y[0:]]
    z = [int(i) for i in z[0:]]

    game = DodgeBall(y[0], y[1], y[2], z)
    print game.play_game()
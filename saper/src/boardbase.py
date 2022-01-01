class BoardBase:
    """ A base board game with random generated bombs.
    """
    min_size = 2
    max_size = 15
    board = []

    def __init__(self, n, m, bomb_number):
        self.n = n
        self.m = m
        self.bomb_number = bomb_number
        self.total_set_as_bomb = 0

    '''
    Check of all parameters are valid, if not throws Exception
    '''
    def is_board_valid(self):
        if not BoardBase.min_size <= self.n <= BoardBase.max_size:
            raise Exception('N is not valid')
        elif not BoardBase.min_size <= self.m <= BoardBase.max_size:
            raise Exception('M is not valid')
        elif not 0 < self.bomb_number <= self.n * self.m:
            raise Exception('Number of bombs is not valid')

        return True

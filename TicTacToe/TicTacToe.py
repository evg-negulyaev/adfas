class TicTacToe:
    def __init__(self, inp):
        self.field = [[inp[0], inp[1], inp[2]],
                      [inp[3], inp[4], inp[5]],
                      [inp[6], inp[7], inp[8]]]

    def to_string(self):
        result = ''
        for i in range(3):
            for j in range(3):
                result += self.field[i][j] + ' '
            result = result.strip()
            result += '\n'
        result = result.strip()
        return result
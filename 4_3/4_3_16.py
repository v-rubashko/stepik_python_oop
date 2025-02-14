class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.default_horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.default_vertical = [1, 2, 3, 4, 5, 6, 7, 8]
        all_potential_movement = [(chr(ord(self.horizontal) + 1), self.vertical + 2),
                                       (chr(ord(self.horizontal) + 1), self.vertical - 2),
                                       (chr(ord(self.horizontal) - 1), self.vertical + 2),
                                       (chr(ord(self.horizontal) - 1), self.vertical - 2),
                                       (chr(ord(self.horizontal) + 2), self.vertical + 1),
                                       (chr(ord(self.horizontal) + 2), self.vertical - 1),
                                       (chr(ord(self.horizontal) - 2), self.vertical + 1),
                                       (chr(ord(self.horizontal) - 2), self.vertical - 1)]
        self.potential_movement = []
        for i in range(8):
            if all_potential_movement[i][0] in self.default_horizontal and all_potential_movement[i][1] in self.default_vertical:
                self.potential_movement.append(all_potential_movement[i])

    def get_char(self):
        return 'N'

    def can_move(self, target_horizontal, target_vertical):
        return True if (target_horizontal, target_vertical) in self.potential_movement else False

    def move_to(self, new_horizontal, new_vertical):
        if self.can_move(new_horizontal, new_vertical):
            self.horizontal = new_horizontal
            self.vertical = new_vertical
            all_potential_movement = [(chr(ord(self.horizontal) + 1), self.vertical + 2),
                                      (chr(ord(self.horizontal) + 1), self.vertical - 2),
                                      (chr(ord(self.horizontal) - 1), self.vertical + 2),
                                      (chr(ord(self.horizontal) - 1), self.vertical - 2),
                                      (chr(ord(self.horizontal) + 2), self.vertical + 1),
                                      (chr(ord(self.horizontal) + 2), self.vertical - 1),
                                      (chr(ord(self.horizontal) - 2), self.vertical + 1),
                                      (chr(ord(self.horizontal) - 2), self.vertical - 1)]
            self.potential_movement = []
            for i in range(8):
                if all_potential_movement[i][0] in self.default_horizontal and all_potential_movement[i][
                    1] in self.default_vertical:
                    self.potential_movement.append(all_potential_movement[i])


    def draw_board(self):
        item = {}
        for v in self.default_vertical[::-1]:
            line = ''
            for h in self.default_horizontal:
                if (h, v) == (self.horizontal, self.vertical):
                    line += self.get_char()
                elif self.can_move(h, v):
                    line += '*'
                else:
                    line += '.'
            print(line)





knight = Knight('c', 3, 'white')

knight.draw_board()
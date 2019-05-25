class Spiral:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
	# States:
        # 0 = right
        # 1 = down
        # --- increase step
        # 2 = left
        # 3 = up
        # --- increase step
        self.state = 0
        self.curr = 0
        self.step = 1

    # Return current coordinates
    def coords(self):
        return (self.x, self.y)

    # Calculate next spiral coordinates
    # Could be made shorter and more clever, but works
    def next_step(self):
        if self.state == 0:
            self.x += 1
            self.curr += 1
            if self.curr == self.step:
                self.state = 1
                self.curr = 0

        elif self.state == 1:
            self.y += 1
            self.curr += 1
            if self.curr == self.step:
                self.state = 2
                self.curr = 0
                self.step += 1

        elif self.state == 2:
            self.x -= 1
            self.curr += 1
            if self.curr == self.step:
                self.state = 3
                self.curr = 0

        elif self.state == 3:
            self.y -= 1
            self.curr += 1
            if self.curr == self.step:
                self.state = 0
                self.curr = 0
                self.step += 1


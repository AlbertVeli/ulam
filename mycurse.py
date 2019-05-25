import curses

class Curse:

    def __init__(self):
        # Init curses
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)

    def get_yx(self):
        return self.stdscr.getmaxyx()

    def str_at(self, s, x, y):
        self.stdscr.addstr(y, x, s, curses.A_REVERSE)
        self.stdscr.refresh()

    def waitkey(self):
        self.stdscr.getch()

    def cleanup(self):
        # Cleanup curses
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

from random import choice
import tkinter as tk
from tkinter import messagebox


class Cell(tk.Button):
    """
    Класс описывает клетку игрового поля
    """
    def __init__(self, master, x, y, *args, **kwargs):
        super(Cell, self).__init__(master, width=3, font='Arial 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = x + 10 * y


class Game:
    """
    Класс описывает игровое поле
    """
    window = tk.Tk()
    HUMAN = 'X'
    COMP = 'O'
    EMPTY = ' '
    SIZE = 10
    TIE = 'Ничья'
    HUMAN_TURN = 'Ваш ход'
    COMP_TURN = 'Ходит компьютер ...'
    HUMAN_WIN = 'Вы победили!'
    COMP_WIN = 'Компьютер победил'
    END_GAME = {
        TIE: TIE,
        HUMAN: COMP_WIN,
        COMP: HUMAN_WIN
    }

    def __init__(self):
        self.window.title("Обратные крестики-нолики")

        self.window.resizable(False, False)
        self.label = tk.Label(self.window, text="Ваш ход")
        self.new_game_btn = tk.Button(self.window, text="Новая игра")
        self.help_btn = tk.Button(self.window, text="Как играть", command=self.help)
        self.new_game_btn.config(command=self.new_game)
        self.buttons = []
        for i in range(self.SIZE):
            tmp = []
            for j in range(self.SIZE):
                btn = Cell(self.window, j, i, text=self.EMPTY)
                btn.config(command=lambda button=btn: self.click(button))
                tmp.append(btn)
            self.buttons.append(tmp)

        self.empty_cells = set(range(100))
        self.active_player = self.HUMAN

    def click(self, cell: Cell):
        """
        Обработка хода игрока
        """
        move = cell.number
        if self.active_player == self.HUMAN:
            cell.config(state=tk.DISABLED, disabledforeground='blue')
            self.empty_cells.remove(move)
            result = self.check_end_game(cell.x, cell.y, self.HUMAN)
            if result == self.HUMAN:
                self.end_game(result)
            self.check_tie()
            # Ход компьютера
            self.active_player = self.COMP
            result = self.comp_move()
            if result:
                self.end_game(result)

    def comp_move(self):
        """
        Выбирается случайное пустое поле, если компьютер после хода на это поле проигрывает -
        выбирается другое поле (если такое осталось).
        """
        checked_moves = set()
        while self.empty_cells.difference(checked_moves):
            rand_move = choice(tuple(self.empty_cells.difference(checked_moves)))
            checked_moves.add(rand_move)
            x, y = rand_move % self.SIZE, rand_move // self.SIZE
            if self.check_end_game(x, y, self.COMP):
                self.buttons[y][x]['text'] = self.EMPTY
            else:
                self.empty_cells.remove(rand_move)
                self.active_player = self.HUMAN
                self.buttons[y][x].config(state=tk.DISABLED, disabledforeground='green')
                break
        else:
            return self.check_end_game(x, y, self.COMP)
        return self.check_tie()

    def create_widgets(self):
        """
        Создание игрового поля
        """
        self.label.grid(row=0, column=2, stick='nwes', columnspan=6)
        self.new_game_btn.grid(row=0, column=8, stick='nwes', columnspan=2)
        self.help_btn.grid(row=0, column=0, stick='nwes', columnspan=2)
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                btn = self.buttons[i][j]
                btn.grid(row=i + 1, column=j, stick='nwes')

    def start(self):
        """
        Создаёт игру при запуске приложения
        """
        self.create_widgets()
        self.window.mainloop()

    def check_end_game(self, x, y, player):
        """
        Проверяет ход на условие окончания игры
        """
        self.buttons[y][x]['text'] = player
        end_game = player * 5
        if end_game in ''.join([self.buttons[i][x]['text'] for i in range(self.SIZE)])\
                or end_game in ''.join([self.buttons[y][j]['text'] for j in range(self.SIZE)])\
                or end_game in self.get_principal_diag(x, y) or end_game in self.get_secondary_diag(x, y):
            return player

    def get_principal_diag(self, x, y):
        """
        Возвращает для точки элементы диагонали параллельной главной
        """
        if x > y:
            return ''.join([self.buttons[i][j]['text'] for i, j in zip(range(0, 10 - x + y), range(x - y, 10))])
        else:
            return ''.join([self.buttons[i][j]['text'] for i, j in zip(range(y - x, 10), range(0, 10 - y + x))])

    def get_secondary_diag(self, x, y):
        """
        Возвращает для точки элементы диагонали параллельной побочной
        """
        if x + y > 9:
            return ''.join([self.buttons[i][j]['text'] for i, j in zip(range(x + y - 9, 10), range(9, y - x, -1))])
        else:
            return ''.join([self.buttons[i][j]['text'] for i, j in zip(range(x + y, - 1, -1), range(0, x + y + 1))])

    def check_tie(self):
        """
        Проверяет остались ли пустые ячейки
        """
        if not self.empty_cells:
            return self.end_game(self.TIE)

    def end_game(self, result):
        """
        Завершает игру при чьей-либо победе или ничье
        """
        self.label['text'] = self.END_GAME[result]
        [[btn.config(state=tk.DISABLED) for btn in row] for row in self.buttons]

    def new_game(self):
        """
        Создает новую игру
        """
        [child.destroy() for child in self.window.winfo_children()]
        self.__init__()
        self.create_widgets()

    def help(self):
        messagebox.showinfo("Справка", "Обратные крестики-нолики» на поле 10 x 10 с правилом «Пять в ряд» – "
                                       "проигрывает тот, у кого получился вертикальный, горизонтальный или диагональный"
                                       " ряд из пяти своих фигур (крестиков/ноликов).Игра проходит в режиме"
                                       " человек против компьютера.")


game = Game()
game.start()



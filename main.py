
import arcade

# Ссылка на сайт с библиотекой https://pypi.org/project/arcade/
# Tutorial https://api.arcade.academy/en/latest/examples/platform_tutorial/step_01.html


SCREEN_WIDTH = 800              # Ширина игрового окна
SCREEN_HEIGHT = 600             # Высота игрового окна
SCREEN_TITLE = "Game ping-pong" # Название игрового окна
WINDOW_POSITION = True          # Окно создается в центре экрана

class Ball(arcade.Sprite):
    """Класс Мяч наследуется от класса arcade.Sprite"""
    def __init__(self):
        """Инициализатор с параметрами: filename, scale"""
        super().__init__('ball.png', 0.05)

        """Скорость движения мяча задается сразу в инициализаторе,
        поэтому мяч начинает двигаться сразу после создания"""
        self.change_x = 1       # скорость перемещения мяча по оси x.
        self.change_y = 1       # скорость перемещения мяча по оси у

    def update(self):
        """Переопределенный метод описывает движение мячика"""
        self.center_x += self.change_x      # перемещаем спрайт-мяч по оси x
        self.center_y += self.change_y      # перемещаем спрайт-мяч по оси x
        if self.right >= SCREEN_WIDTH:      # если правая граница спрайта достигла правого края окна
            self.change_x = -self.change_x  # меняем скорость перемещения спрайта на противоположную
        if self.left <= 0:                  # если правая граница спрайта достигла левого края окна
            self.change_x = -self.change_x  # меняем скорость перемещения спрайта на противоположную
        if self.top >= SCREEN_HEIGHT:       # если верхняя граница спрайта достигла верхнего края окна
            self.change_y = -self.change_y  # меняем скорость перемещения спрайта на противоположную
        if self.bottom <= 0:                # если нижняя граница спрайта достигла нижнего края окна
            self.change_y = -self.change_y  # меняем скорость перемещения спрайта на противоположную


class Bar(arcade.Sprite):
    """Класс Ракетка наследуется от класса arcade.Sprite"""
    def __init__(self):
        """Инициализатор с параметрами: filename, scale"""
        super().__init__('bar.png', 0.4)

    def update(self):
        """Переопределенный метод описывает движение ракетки"""
        self.center_x += self.change_x      # перемещаем спрайт-ракетку по оси x
        if self.right >= SCREEN_WIDTH:      # если правая граница спрайта достигла правого края окна
            self.right = SCREEN_WIDTH       # остановим движение
        if self.left <= 0:                  # если левая граница спрайта достигла левого края окна
            self.left = 0                   # остановим движение


class Game(arcade.Window):
    """Класс Game наследуется от класса arcade.Window"""
    def __init__(self, width, height, title, position):
        """Инициализатор класса может принимать много параметров,
        в нашем случает это параметры: ширина, высота и название и позиция игрового окна"""
        super().__init__(width, height, title,center_window=position)
        self.bar = Bar()                    # создаем объект класса Bar
        self.ball = Ball()                  # создаем объект класса Ball
        self.setup()                        # метод задает начальное положение спрайтов в игровом окне

    def update(self, delta):
        """Метод отслеживает события, происходящие со спрайтами"""
        if arcade.check_for_collision(self.bar, self.ball): # Если произошло столкновение мячика с ракеткой
            # self.ball.change_x = -self.ball.change_x
            self.ball.change_y = -self.ball.change_y        # меняем направление по координате y на противоположное
        self.ball.update()      # получает новые координаты спрайта-мяч на игровом поле
        self.bar.update()       # получает новые координаты спрайта-ракетка на игровом поле

    def setup(self):
        """Метод задает начальное положение спрайтов в окне"""
        self.bar.center_x = SCREEN_WIDTH / 2    # горизонтальное положение ракетки
        self.bar.center_y = 15                  # вертикальное положение ракетки
        self.ball.center_x = SCREEN_WIDTH / 2   # горизонтальное положение мячика
        self.ball.center_y = SCREEN_HEIGHT - 20      # вертикальное положение мячика


    def on_draw(self):
        """Метод отображает созданные спрайты в игровом окне"""
        self.clear((255,0,255))     # очистим окно и установим для него фоновый цвет
        self.bar.draw()             # отобразим на игровом поле спрайт-ракетку
        self.ball.draw()            # отобразим на игровом поле спрайт-мяч


    def on_key_press(self, key: int, modifiers: int):
        """Метод отслеживает событие нажатия клавиши"""
        if key == arcade.key.RIGHT:     # если нажата клавиша --->
            self.bar.change_x = 10      # ракетка движется вправо
        if key == arcade.key.LEFT:      # если нажата клавиша <---
            self.bar.change_x = -10     # ракетка движется влево

    def on_key_release(self, key: int, modifiers: int):
        """Метод отслеживает событие отпускания клавиши"""
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:   # если клавиша RIGHT или LEFT отпущена
            self.bar.change_x = 0                               # скорость движения ракетки = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, WINDOW_POSITION)

    arcade.run()
import turtle

# Настройки
screen = turtle.Screen()
screen.bgcolor("white")  # Цвет фона экрана
screen.title("Рисование квадрата с turtle")

# Создаём черепашку
my_turtle = turtle.Turtle()
my_turtle.pensize(3)  # Устанавливаем толщину линии
my_turtle.speed(5)  # Устанавливаем скорость рисования (от 1 до 10)

# Цвета для сторон квадрата
colors = ["red", "blue", "green", "yellow"]

# Рисуем квадрат
for color in colors:
    my_turtle.color(color)  # Устанавливаем цвет пера
    my_turtle.forward(100)  # Двигаем черепашку вперёд на 100 пикселей
    my_turtle.left(90)      # Поворачиваем черепашку на 90 градусов влево

# Завершаем работу
turtle.done()
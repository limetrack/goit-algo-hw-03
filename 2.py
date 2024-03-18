import turtle

def koch_snowflake_segment(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake_segment(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake(order, size):
    t = turtle.Turtle()
    t.speed(0)  # найвища швидкість малювання
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Створення трьох сегментів сніжинки
    for _ in range(3):
        koch_snowflake_segment(t, order, size)
        t.right(120)

    turtle.done()

def main():
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    size = 300  # можна змінити розмір сніжинки за бажанням
    koch_snowflake(order, size)

if __name__ == "__main__":
    main()

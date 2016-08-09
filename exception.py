while True:
    try:
        x = int(input('数字を入力してください: '))
        break
    except (TypeError, NameError, ValueError):
        print("数字じゃないじゃん")

    print('もういちど！')
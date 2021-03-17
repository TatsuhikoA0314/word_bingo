import check_bingo

# インプット
# サイズ取得（S）
grid_num = int(input())
# ワードビンゴ格納用の配列作成
bingo = []

# S回ループしてビンゴを二次元配列に入れていく
for i in range(grid_num):
    input_bingo = input()
    # 入力された文字列を空白で分けていく
    bingo.append(input_bingo.split(' '))

# 文字列数を取得（N）
words_num = int(input())
# 文字列格納用の配列作成
words_list = []

# N回ループして文字列を配列に入れていく
for i in range(words_num):
    input_words = input()
    words_list.append(input_words)

# 条件に当てはまっている場合のみビンゴかチェックする
# 特に課題内に記載がなかったためコメントアウトしています
if check_bingo.inputs_check(grid_num, bingo, words_num, words_list):

    # 関数を呼び出して縦横斜めにわけてビンゴかどうか調べる
    # 検索方向を指定
    direction = 'col'
    col_result = check_bingo.col_row_check(grid_num, bingo, words_list, direction)
    # 検索方向を指定
    direction = 'row'
    row_result = check_bingo.col_row_check(grid_num, bingo, words_list, direction)
    # 検索方向を指定
    direction = 'left_right'
    left_right_result = check_bingo.dia_check(grid_num, bingo, words_list, direction)
    # 検索方向を指定
    direction = 'right_left'
    right_left_result = check_bingo.dia_check(grid_num, bingo, words_list, direction)

    # 関数の返り値の真偽を確認し、もし、一つでも真ならば'yes'を
    # もし、全て偽ならば'no'を表示する
    if col_result:
        print('yes')
    elif row_result:
        print('yes')
    elif left_right_result:
        print('yes')
    elif right_left_result:
        print('yes')
    else:
        print('no')


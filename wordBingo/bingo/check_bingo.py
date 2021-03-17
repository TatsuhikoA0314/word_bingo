# ビンゴチェック用関数

# 各入力値の妥当性のチェック
def inputs_check(grid_num, bingo, words_num, words_list):
    """ inputs_checkの説明
        入力された数値がすべて条件に当てはまっているかチェックする
    Args:
    ----------
    grid_num (INT):
        グリッドのサイズ（S）
    bingo (STRIN二次配列):
        入力されたビンゴ内文字列を空白で分けたもの
    words_list (STRING配列):
        入力された文字列を空白で分けたもの
    words_num (INT):
        文字列数（N）

    Returns:
    ----------
    bool:
        True なら条件当てはまっている, False なら条件に当てはまっていない

    Example:
    ----------
    >>> inputs_check(INT, SRTING配列, INT)
        True or False
    """
    # 問題なければ初期値が返り値になる
    check_input = True

    # 入力された数値が指定範囲内かチェック
    if not 3 <= grid_num <= 1000:
        check_input = False

    if not 1 <= words_num <= 2000:
        check_input = False

    # 入力された文字列の各文字数が指定範囲内かチェック
    for i in range(grid_num):
        for j in range(grid_num):
            if not 1 <= len(bingo[i][j]) <= 100:
                check_input = False

    for index, word in enumerate(words_list):
        if not 1 <= len(word) <= 100:
            check_input = False
    return check_input
        
# 縦横方向を調べる
def col_row_check(grid_num, bingo, words_list, direction):
    """ col_row_checkの説明
        判定する数を減らすため、縦横列の中で一つでも外れたら、
        その瞬間列の最後まで確認せず横列を移動し次の縦列の判定を開始する。
        逆に当たった場合は、条件に重複がないと書かれているので、
        検索を早めるためにその文字列を削除する
        列の最後までいければ、ビンゴと判定し、Trueを返す。いけなければ、Falseを返す
    Args:
    ----------
    grid_num (INT):
        グリッドのサイズ（S）
    bingo (STRIN二次配列):
        入力されたビンゴ内文字列を空白で分けたもの
    words_list (STRING配列):
        入力された文字列を空白で分けたもの
    direction (STRING):
        縦横の検索方向の指定

    Returns:
    ----------
    bool:
        True ならビンゴ, False ならビンゴでない

    Example:
    ----------
    >>> col_row_check(INT, SRTING二次配列, SRTING配列, 'row' or 'col')
        True or False
    """
    # 二重ループを抜ける際に使う印
    flg = False
    # 値渡しを行う
    words = list(words_list)
    # 横列を一つずつ進める
    for dir_first in range(grid_num):
        # 縦列を一つずつ進める
        for dir_second in range(grid_num):
            # 全ての文字列を現在のグリッドと比較する
            for word in range(len(words)):
                # 最初に検索方向を調べる
                if direction == 'col':
                    grid_word = bingo[dir_second][dir_first]
                elif direction == 'row':
                    grid_word = bingo[dir_first][dir_second]
                # 同じ文字列が存在するか判定
                if grid_word == words[word]:
                    # もし、列の最後までいけたら、Trueを返す。
                    # そうでなければループを終了し、下のグリッドに進む
                    if (dir_second + 1) == grid_num:
                        return True
                    else:
                        # 重複がないためwords配列から文字列を削除する
                        del words[word]
                        break
                # 文字列を全て比較し終えたら横に進むために
                # flgをTrueにし、二重のループを抜ける
                else:
                    if  (word + 1) == len(words):
                        flg = True
                        break
            # もし、flgがTrueだった場合、横に一つずらすためにループから出る
            if flg:
                flg = False
                break
        # もし、現在の横列が最後であった場合Falseを返す
        if (dir_first + 1) == grid_num:
            return False

# 斜め方向調べる
def dia_check(grid_num, bingo, words_list, direction):
    """ dia_checkの説明
        判定する数を減らすため、斜め列の中で一つでも外れたら、その瞬間Falseを返す。
        列の最後までいければ、ビンゴと判定し、Trueを返す
        いけなければ、Falseを返す

    Args:
    ----------
    grid_num (INT):
        グリッドのサイズ（S）
    bingo (STRIN二次配列):
        入力されたビンゴ内文字列を空白で分けたもの
    words_list (STRING配列):
        入力された文字列を空白で分けたもの
    direction (STRING):
        縦横の検索方向の指定

    Returns:
    ----------
    bool:
        True ならビンゴ, False ならビンゴでない

    Example:
    ----------
    >>> dia_check(INT, SRTING二次配列, SRTING配列, 'left_right' or 'right_left')
        True or False
    """
    
    # 値渡しを行う
    words = list(words_list)
    
    for dia in range(grid_num):
        # 全ての文字列を現在のグリッドと比較する
        if direction == 'left_right':
            for word in range(len(words)):
                # 左上から右下へは縦横の数値を同じでグリッドを特定し判定する
                if bingo[dia][dia] == words[word]:
                    # もし、列の最後までいけたら、Trueを返す。
                    # そうでなければ、次のグリッドに進む
                    if (dia + 1) == grid_num:
                            return True
                    else:
                        # 重複がないためwords配列から文字列を削除する
                        del words[word]
                        break
                # 文字列を全て比較し終えたら次に進むために
                else:
                    if  (word + 1) == len(words):
                        return False
        # 右上から左下
        elif direction == 'right_left':
            # ループを逆にすることで右上から左下への検索を可能にする  
            for rev in reversed(range(grid_num)):
                for word in range(len(words)):
                    # 右上から左下へグリッドを特定し判定する
                    if bingo[dia][rev] == words[word]:
                        # もし、列の最後までいけたら、Trueを返す。
                        # そうでなければ、次のグリッドに進む
                        if rev == 0:
                                return True
                        else:
                            # 重複がないためwords配列から文字列を削除する
                            del words[word]
                            # 次に進むために一つ右上にずらす
                            dia += 1
                            break
                    # 文字列を全て比較し終えたら次に進むために
                    else:
                        if  (word + 1) == len(words):
                            return False

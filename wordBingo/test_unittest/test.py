import unittest
import bingo.check_bingo as bingo


class BingoTest(unittest.TestCase):

    # 入力された値の確認
    def test_input(self):
       # 各引数に値を入れる
        test_grid_num = 3
        test_bingo = [['orange', 'apple', 'cube'], ['batch', 'web', 'cloud'], ['sql', 'https', 'http']]
        test_words_num = 7
        test_words_list = ['web', 'https', 'windows', 'batch', 'keyboard', 'apple', 'cpu']
        # Trueが帰ってきたら、OK
        self.assertEqual(bingo.inputs_check(test_grid_num, test_bingo, test_words_num, test_words_list), True)
    

    # 縦方向のテスト
    def test_col(self):
       # 各引数に値を入れる
        test_grid_num = 3
        test_bingo = [['orange', 'apple', 'cube'], ['batch', 'web', 'cloud'], ['sql', 'https', 'http']]
        test_words_num = 7
        test_words_list = ['web', 'https', 'windows', 'batch', 'keyboard', 'apple', 'cpu']
        test_direction = 'col'
        # Trueが帰ってきたら、OK
        self.assertEqual(bingo.col_row_check(test_grid_num, test_bingo, test_words_list, test_direction), True)
    
    # 横方向のテスト
    def test_row(self):
        test_grid_num = 3
        test_bingo = [['orange', 'apple', 'cube'], ['batch', 'keyboard', 'web'], ['sql', 'http', 'https']]
        test_words_list = ['web', 'https', 'windows', 'batch', 'keyboard', 'apple', 'cpu']
        test_direction = 'row'
        # Trueが帰ってきたら、OK
        self.assertEqual(bingo.col_row_check(test_grid_num, test_bingo, test_words_list, test_direction), True)
    
    # # 左上から右下へテスト
    def test_left_right(self):
        test_grid_num = 3
        test_bingo = [['apple', 'orange', 'cube'], ['batch', 'web', 'cloud'], ['sql', 'http', 'https']]
        test_words_list = ['web', 'https', 'windows', 'batch', 'keyboard', 'apple', 'cpu']
        test_direction = 'left_right'
        # Trueが帰ってきたら、OK
        self.assertEqual(bingo.dia_check(test_grid_num, test_bingo, test_words_list, test_direction), True)
    
    # 右上から左下へテスト
    def test_right_left(self):
        test_grid_num = 3
        test_bingo = [['orange', 'cube', 'apple'], ['batch', 'web', 'cloud'], ['cpu', 'http', 'https']]
        test_words_list = ['web', 'https', 'windows', 'batch', 'keyboard', 'apple', 'cpu']
        test_direction = 'right_left'
        # Trueが帰ってきたら、OK
        self.assertEqual(bingo.dia_check(test_grid_num, test_bingo, test_words_list, test_direction), True)
    

if __name__ == "__main__":
    unittest.main()

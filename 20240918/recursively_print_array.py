# Hi-lock: (("後処理" (0 (quote 6-my-face) prepend)))
# Hi-lock: (("前処理" (0 (quote 5-my-face) prepend)))
# Hi-lock: (("\\_<element\\_>" (0 (quote 3-my-face) prepend)))
# Hi-lock: (("\\_<print\\_>" (0 (quote 2-my-face) prepend)))
# Hi-lock: (("\\_<print_array\\_>" (0 (quote 1-my-face) prepend)))

# ================================================================
# 定数の定義
# ================================================================
MY_ARRAY = [
    1, 2, 3,
    [
        4, 5,
        [
            6, 7, [8, [81, 82, 83, ]]
        ],
        9,  10
    ],
    11,  12
]


UNIT_INDENT="--> "
MAX_DEPTH=10

# ================================================================
# 関数の定義
# ================================================================
def print_array(array, depth:int=0):
    if depth > MAX_DEPTH:
        print(f"\n\n!!!! too deep: {depth=} !!!!\n")
        return

    for element in array:
        type_element = type(element)
        if  type_element  == list:

            # インデントの幅の設定
            indent_on_brackets = UNIT_INDENT*depth
            depth+=1
            indent_on_elements = UNIT_INDENT*depth

            # 開き括弧の表示（前処理）
            print(f"\n{indent_on_brackets}[\n{indent_on_elements}", end="")

            # 再帰的呼び出し
            print_array(element, depth)

            # 閉じ括弧の表示（後処理）
            print(f"\n{indent_on_brackets}],", end="")

        else:
            # 要素の出力
            print(f"{element},", end="")
# ================================================================
# エントリーポイント
# ================================================================
if __name__ == '__main__':
    print_array(MY_ARRAY)
    # ↓ 配列の終端での改行がprint_array()内で狙い通りには出力できないので、
    # ↓ 呼び出し後に手動で改行を挿入している。
    print("\n")

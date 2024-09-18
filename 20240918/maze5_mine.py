# Hi-lock: (("後処理" (0 (quote 6-my-face) prepend)))
# Hi-lock: (("前処理" (0 (quote 5-my-face) prepend)))
# Hi-lock: (("\\_<search\\_>" (0 (quote 1-my-face) prepend)))

# ################################################################
# 定数の定義
# ################################################################
# ################################
# サンプルと同じく（本と同じく）、ゴールへの経路が1つしか無い迷路
# ################################
MAZE_1 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 7, 0, 0, 9, 9, 0, 9, 9],
    [9, 0, 9, 9, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 9, 9, 9, 9],
    [9, 9, 0, 9, 0, 9, 0, 1, 9],
    [9, 0, 0, 9, 0, 0, 0, 9, 9],
    [9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9]
]

# ################################
# ゴールへの経路が複数（6つ）ある迷路
# ################################
MAZE_6 = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 7, 0, 0, 8, 9, 0, 9, 9],
    [9, 0, 9, 9, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 9, 8, 9, 9],
    [9, 9, 0, 9, 0, 9, 0, 1, 9],
    [9, 0, 0, 9, 0, 0, 0, 9, 9],
    [9, 0, 8, 0, 0, 9, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9]
]

MAZE = MAZE_6

# 進行方向をセット
MOVINGS = [[0, -1, "UP"], [-1, 0, "LEFT"], [0, 1, "DOWN"], [1, 0, "RIGHT"]]

# ################################################################
# 広域変数の定義
# ################################################################
LOGS_TO_GOAL=[]
max_depth = 0

# ################################################################
# 関数の定義
# ################################################################
def search(log):
    global max_depth
    depth = len(log)
    if  max_depth < depth:
        max_depth = depth

    x, y = log[-1] # 最後の位置を取得
    print(f"<<<<<<<<<<<<<<<< position [{x}, {y}], {depth}")

    if MAZE[x][y] == 1:
        print(f"getting goal: {log=} !!!!")
        LOGS_TO_GOAL.append(list(log))
        return

    # 上下左右の4方向のそれぞれに進めるかどうかを試す
    for moving in MOVINGS:

        # 説明変数を更新する
        next_x         = x + moving[0]
        next_y         = y + moving[1]
        next_direction =     moving[2]
        print(f"moving {next_direction} from [{x=}, {y=}] to [{next_x=}, {next_y=}]")

        if MAZE[next_x][next_y] != 9:
            print(f"[{next_x=}, {next_y=}] is space, not wall")
            if [next_x, next_y] not in log:
                # 過去に（※1）移動していない場所であれば移動
                # ※1. 全ての探索における履歴を検証しているのではなく、
                #      検証対象の履歴は今次呼び出し時の引数 log に限られる。
                print(f"approaching [{next_x=}, {next_y=}] for the first time")

                log.append([next_x, next_y]) # プッシュ（前処理）
                search(log)                  # 再帰的呼び出し
                log.pop(-1)                  # ポップ（後処理）

        else:
            print(f"[{next_x=}, {next_y=}] is wall, stopping up to {log=}")

    print(f">>>>>>>>>>>>>>>> position [{x}, {y}], {depth}")
    return
# ################################################################
# エントリーポイント
# ################################################################
if __name__ == '__main__':
    search([[1, 1]])

    for log in LOGS_TO_GOAL:
        print(f"{len(log)=}, {log}")

    print(f"{max_depth=}")

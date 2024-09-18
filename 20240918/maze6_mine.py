# Hi-lock: (("8,[[:space:]]*" (0 (quote 1-my-face) prepend)))
# Hi-lock: (("7,[[:space:]]*" (0 (quote 2-my-face) prepend)))
# Hi-lock: (("1,[[:space:]]*" (0 (quote 6-my-face) prepend)))
# Hi-lock: (("9,?[[:space:]]*" (0 (quote 12-my-face) prepend)))

# Hi-lock: (("\\_<depth\\_>" (0 (quote gray-2-my-face) prepend)))
# Hi-lock: (("furthest_point" (0 (quote gray-5-my-face) prepend)))
# Hi-lock: (("\\_<new_furthest_point\\_>" (0 (quote 14-my-face) prepend)))
# Hi-lock: (("\\_<final_point\\_>" (0 (quote 13-my-face) prepend)))
# Hi-lock: (("\\_<new_target\\_>" (0 (quote 12-my-face) prepend)))
# Hi-lock: (("\\_<trace\\_>" (0 (quote 11-my-face) prepend)))
# Hi-lock: (("\\_<short_links\\_>" (0 (quote 10-my-face) prepend)))
# Hi-lock: (("\\_<link\\_>" (0 (quote 9-my-face) prepend)))
# Hi-lock: (("\\_<back_trace\\_>" (0 (quote 8-my-face) prepend)))
# Hi-lock: (("\\_<target\\_>" (0 (quote 7-my-face) prepend)))
# Hi-lock: (("\\_<getting_goal\\_>" (0 (quote 6-my-face) prepend)))
# Hi-lock: (("\\_<links\\_>" (0 (quote 5-my-face) prepend)))
# Hi-lock: (("\\_<next_y\\_>" (0 (quote 4-my-face) prepend)))
# Hi-lock: (("\\_<next_x\\_>" (0 (quote 3-my-face) prepend)))
# Hi-lock: (("\\_<to_be_searched_further\\_>" (0 (quote 2-my-face) prepend)))
# Hi-lock: (("\\_<searched_already\\_>" (0 (quote 1-my-face) prepend)))

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
MOVINGS = [[0, -1], [-1, 0], [0, 1], [1, 0]]

# ################################################################
# 関数
# ################################################################
def back_trace(links, furthest_point):

    for idx, link in enumerate(reversed(links)):
        if link["to"] == furthest_point:
            print(link)

            new_furthest_point = link["from"]
            short_links = links[0:len(links)-(idx+1)]

            # 再帰
            back_trace(short_links, new_furthest_point)

            # ↓ breakしてもしなくても同じ結果になる。
            # ↓ whileブロック内で下記の条件が課されているので。
            # ↓ if   [next_x, next_y] not in searched_already:
            break

    trace.append(furthest_point)

# ################################################################
# 広域変数の宣言 と 初期化
# ################################################################

# ################
# 探索済みの座標
# ################
searched_already = [[1, 1]]

# ################
# さらに探索すべきの座標と探索段階（探索の深さ）
# ################
to_be_searched_further = [[1, 1, 0]]

# ################
# 各移動における前後の座標
# ################
# 例:
#   [ {"from":(x, y), "to":(x+1, y)}, ..., ]
# 注意: 必ずしもゴールに至る移動とは限らない。
#       ゴールに至らない移動も含めて、全ての移動を記録する。
links = []

# ################
# ゴールに至った経路: back_trace() 内で逆順に組み立てる
# ################
trace = []

# ################
# ゴールに至ったかどうかのフラグ
# ################
# サンプルのまま、ゴールに至った後に exit してしまうと、
# 広域変数のメモリが解放されてしまい、
# back_trace() による ゴールに至った経路の組み立てができなくなってしまう。
# そこで while だけを抜けるために、whileの継続条件にこのフラグも課す。
getting_goal=False

max_breadth = 0
max_depth = 0
num_while = 0

# ################################################################
# 本体
# ################################################################
while (len(to_be_searched_further) > 0) and (getting_goal != True):

    num_while+=1

    x, y, depth = to_be_searched_further.pop(0) # キューの先頭を取り出す
    if  max_depth < depth:
        max_depth = depth


    for moving in MOVINGS:

        next_x = x + moving[0]
        next_y = y + moving[1]

        links.append({"from" : (x, y),
                      "to"   : (next_x, next_y),
                      "depth": depth})

        if MAZE[next_x][next_y] == 1:
            print(depth + 1, links)
            getting_goal = True
            break

        elif MAZE[next_x][next_y] != 9:
            if   [next_x, next_y] not in searched_already:
                # 過去に移動していない場所の場合、ログとキューに追加する
                searched_already       .append([next_x, next_y])
                to_be_searched_further .append([next_x, next_y, depth + 1])

                # TODO: 幅の定義が不明
                breadth = len(to_be_searched_further)
                if  max_breadth < breadth:
                    max_breadth = breadth


print("================================================================")

back_trace(links, links[-1]["to"])
print(f"\nThe trace from start to goal is {trace}.")
print(f"{max_depth=}, {max_breadth=}, {num_while=}")

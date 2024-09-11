import numpy as np
import matplotlib
import matplotlib.pyplot as plt

MAZE = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 0, 0, 9, 9, 0, 9, 9],
    [9, 0, 9, 9, 0, 0, 0, 0, 9],
    [9, 0, 0, 0, 0, 9, 9, 9, 9],
    [9, 9, 0, 9, 0, 9, 0, 6, 9],
    [9, 0, 0, 9, 0, 0, 0, 9, 9],
    [9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9]
]

STEPS = [
    (1, 1),     (2, 1),     (3, 1),     (3, 2),     (4, 2),     (5, 2),
    (5, 1),     (6, 1),     (5, 1),     (5, 2),     (4, 2),     (3, 2),
    (3, 3),     (3, 4),     (4, 4),     (5, 4),     (6, 4),     (6, 3),
    (6, 4),     (5, 4),     (5, 5),     (5, 6),     (6, 6),     (6, 7),
    (6, 6),     (5, 6),     (4, 6),     (4, 7) ]

fig, ax = plt.subplots()

heatmap = ax.pcolormesh(MAZE,
                        # vmin=0,
                        # vmax=9,
                        cmap="jet" # 配色のパターン
                        )

# ################################
# 格子を表示することで迷路っぽさを表現する
# ################################

# 格子の位置の設定
ax.set_xticks(np.arange(len(MAZE[0])), minor=False)
ax.set_yticks(np.arange(len(MAZE   )), minor=False)

# 格子の描画
plt.grid()

maze = MAZE

for idx, step in enumerate(STEPS):
    # ################################
    # データの読み込み
    # ################################
    maze[step[0]][step[1]] = 3
    heatmap = ax.pcolormesh(maze,
                            # vmin=0,
                            # vmax=9,
                            cmap="jet" # 配色のパターン
                            )
    previous_step = step
    maze[previous_step[0]][previous_step[1]] = 4
    # ################################
    # 画像ファイルの生成
    # ################################

    # 注意: images ディレクトリが存在しないとエラーになります。
    # pythonプログラムからも作れるはずですが、
    # 今は横着して、あらかじめ手動で作っておきました。
    plt.savefig(f'./images/{idx:02}.png')

# パラパラ漫画の作り方
# 1. imagemagick をインストールする。
# 2. images ディレクトリに移動する。
#     -$cd ./images/
# 3. 以下のコマンドを実行する。
#     -$convert -delay 25 *.png steps.gif

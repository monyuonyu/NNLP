import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# x軸の範囲
x = np.linspace(-10, 10, 400)
y = sigmoid(x)

# 初期プロット
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-', lw=2)
ax.set_xlim(-10, 10)
ax.set_ylim(0, 1)
ax.set_xlabel("x")
ax.set_ylabel("sigmoid(x)")
ax.set_title("Sigmoid Function Animation")

# x値を入力してy値が現れるようにする
plot_x = []
plot_y = []

def update(frame):
    plot_x.append(x[frame])
    plot_y.append(y[frame])
    line.set_data(plot_x, plot_y)
    return line,

# アニメーションの作成
ani = animation.FuncAnimation(fig, update, frames=len(x), interval=10, blit=True)

# GIFとして保存
ani.save("sigmoid_animation.gif", writer="pillow", fps=30)

plt.show()

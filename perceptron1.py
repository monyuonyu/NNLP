# パーセプトロンの原型の実装例（重み付け、学習なし）

# しきい値を設定
shikii = 5

def perceptron(input_value):
    if input_value >= shikii:
        return "OK"
    else:
        return "NG"

# 判定例
print(perceptron(4))  # NG
print(perceptron(6))  # OK

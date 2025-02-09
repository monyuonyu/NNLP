# 重み付きパーセプトロン

# しきい値の設定
threshold = 100  # 合計スコアがこの値以上ならOK

# テストケースの入力（国語: 80, 数学: 50, 英語: 90）
test_case = [80, 50, 90]

# 重みセットの定義
weights_sets = {
    "set1": [0.3, 0.2, 0.6],  # NG (合計スコアがしきい値未満)
    "set2": [0.6, 0.8, 0.2],  # OK (しきい値を超える)
}

# パーセプトロンの判定関数
def perceptron(inputs, weights):
    # 各入力値と重みを掛け合わせてスコアを計算
    score = sum(inputs[i] * weights[i] for i in range(len(inputs)))
    # しきい値と比較して判定を返す
    return score, "OK" if score >= threshold else "NG"

# 結果の表示
print("| 重みセット | 判定 (80,50,90) [score] |")

# 各重みセットで計算
for set_name, weights in weights_sets.items():
    score, result = perceptron(test_case, weights)
    print(f"| {set_name:9} | {result:2} ({score:6.2f})          |")

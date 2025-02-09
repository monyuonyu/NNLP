# しきい値の設定（合計スコアがこの値以上ならOKと判定）
threshold = 100  

# 学習データ（入力値, 正解ラベル）
data = [
    ([80, 50, 90], "OK"),  # 合格
    ([30, 20, 40], "NG"),  # 不合格
    ([50, 60, 70], "OK"),  # 合格
    ([40, 30, 20], "NG")   # 不合格
]

# 初期重みの設定
weights = [0.1, 0.1, 0.1]  # 初期値はすべて0.1
learning_rate = 0.01  # 学習率（どの程度修正するか）

def train_perceptron(data, weights, learning_rate, epochs=1000):
    """
    パーセプトロンの学習関数
    """
    for epoch in range(epochs):  # 指定回数繰り返す
        for inputs, label in data:
            # 1.予測
            score = sum(inputs[i] * weights[i] for i in range(len(inputs)))
            prediction = "OK" if score >= threshold else "NG"  
            
            # 2.誤差の計算
            actual = 1 if label == "OK" else 0
            predicted = 1 if prediction == "OK" else 0
            error = actual - predicted  
            
            # 3.重みの修正
            for i in range(len(weights)):
                weights[i] += learning_rate * error * inputs[i]  
    return weights

# 学習を実行
trained_weights = train_perceptron(data, weights, learning_rate)

# 学習後の結果を出力
print("学習後の重み:", trained_weights)

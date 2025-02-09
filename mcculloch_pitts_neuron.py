# マカロック・ピッツニューロンを電気のスイッチとして実装

def light_switch_neuron(switches):
    """
    3つのスイッチがすべてON（1）になったら電気がつく（1を出力）。
    :param switches: 3つのスイッチの状態（0または1のリスト）
    :return: 1（電気がつく）または0（電気がつかない）
    """
    if switches[0] == 1 and switches[1] == 1 and switches[2] == 1:
        return 1
    else:
        return 0

# すべてのスイッチの状態の組み合わせを生成
switch_combinations = [
    [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
    [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]
]

# 各組み合わせに対する電気の状態を出力
print("スイッチ1 | スイッチ2 | スイッチ3 | 電気の状態")
print("----------------------------------")
for switches in switch_combinations:
    light_on = light_switch_neuron(switches)
    print(f"   {switches[0]}     |    {switches[1]}     |    {switches[2]}     | {'ON' if light_on else 'OFF'}")

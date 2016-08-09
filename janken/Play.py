import random
HANDS = ('グー', 'チョキ', 'パー')


def select_hand():
    """
    コンピュータの手をランダムに決める
    いずれか
    :return:HANDSの中のいずれか。
    """
    HANDS_choice = random.choice(HANDS)

    return HANDS_choice


def judgement(player, computer):
    """
    じゃんけんの勝敗を判定する
    :param player: HANDOSの中のどれか
    :param computer: HANDOSの中のどれか
    :return: プレイヤーが勝ちの場合は１，あいこは０，負けは−１を返す
    """
    if player == 0 and computer == 1:
        return 1

    if player == 1 and computer == 2:
        return 1

    if player == 2 and computer == 0:
        return 1

    if player == 0 and computer == 2:
        return -1

    if player == 1 and computer == 0:
        return -1

    if player == 2 and computer == 1:
        return -1

    else:
        return 0


def save_score(result):
    """
    'score.txt'に戦績を保存。
    win:x lose:y drow:zのディクショナリデータを保存する。
    :param result:
    :return: Nonu
    """
    pass

if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選択してください(数字): '))-1
    computer = select_hand()
    result = judgement(player, computer)
    # コンピュータの手と勝敗の結果を表示
    save_score(result)

    print(computer)

    print(result)
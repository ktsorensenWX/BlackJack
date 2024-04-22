import random
import sys


# ace = 1, 2-10 number cards, 11-13 is jacks/kings/queens
def get_card():
    return random.randint(1, 13)


def score(cards):
    total_cards = []
    total_soft_ace = []

    for i in cards:
        if i > 10:  # Checks for J's, K's and Q's
            total_cards.append(10)
        elif i == 1:  # Checks for an Ace
            if sum(total_cards) > 21 & sum(total_soft_ace) == 1:
                total_cards.append(1)
            elif 20 >= sum(total_cards) >= 11:
                total_cards.append(1)
            else:
                total_cards.append(11)
                total_soft_ace.append(1)
        else:
            total_cards.append(i)

    total = sum(total_cards)
    soft_ace_count = sum(total_soft_ace)

    return total, soft_ace_count


def stand(stand_on_value, stand_on_soft, cards):
    total, soft_ace_count = score(cards)

    if stand_on_soft == 'soft':
        if total >= int(stand_on_value):
            return True
        elif soft_ace_count == 1:
            return False
    elif stand_on_soft == 'hard':
        if int(stand_on_value) <= total:
            return True
        else:
            return False


def main():
    if len(sys.argv) > 4:
        raise ValueError('Too many arguments')
    if 20 <= int(sys.argv[2]) > 0:
        raise ValueError('Only values between 1-20 allowed')

    bust_counter = 0
    for z in range(0, int(sys.argv[1])):
        hand = []
        for i in range(2):
            hand.append(get_card())
        total, _ = score(hand)
        if stand(sys.argv[2], sys.argv[3], hand):
            z += 1
        else:
            while total < int(sys.argv[2]):
                hand.append(get_card())
                stand(int(sys.argv[2]), sys.argv[3], hand)
                total, _ = score(hand)
                if total > 21:
                    z += 1
                    bust_counter += 1
                if 21 > total >= int(sys.argv[2]):
                    z += 1

    hand_is_bust_percentage = round(float(bust_counter / int(sys.argv[1])) * 100, 2)
    print(hand_is_bust_percentage, '%')


if __name__ == '__main__':
    main()

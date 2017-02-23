# Lesson 1 first edition

def poker(hands):
	# return the best hand: poker([hand1,hand2...]) => hand2
	return max(hands,key=hand_rank)

def hand_rank(hand):

	return


def test():
    # To be a good programmer you must be a good tester

    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf,fk,fh]) == sf
    assert poker([fk,fh]) == fk
    assert poker([fh,fh]) == fh
    assert poker([fh]) == fh
    assert poker([sf]+[fh]*99) == sf

    print("Tests pass")

 print(test())
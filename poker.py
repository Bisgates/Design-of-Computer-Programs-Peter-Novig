# Lesson 1 first edition

def poker(hands):
	# return the best hand: poker([hand1,hand2...]) => hand2
	return max(hands,key=hand_rank)

def hand_rank(hand):
	# return a value indicate the ranking of a hand
	ranks = card_ranks(hand)
	if(straight(ranks) and flush(ranks)):
		return (8,max(hand))
	elif(kind(4,ranks)):
		return (7,kind(4,ranks),kind(1,ranks))
	elif(kind(3,ranks) and kind(2,ranks)):
		return (6,kind(3,ranks),kind(2,ranks))
	elif(flush(hand)):
		return (5,ranks)
	elif(straight(ranks)):
		return (4,max(hand))
	elif(kind(3,ranks)):
		return(3,kind(3,ranks),ranks)
	elif(two_pairs(ranks)!=None):
		return(2,two_pairs(ranks),ranks)
	elif(kind(2,ranks)):
		return(1,kind(2,ranks),ranks)
	else:
		return(0,ranks)

def card_ranks(cards):
	# rank the card : [3D 3C 5D 5C 9C] => [9 5 5 3 3]
	ss = '__23456789TJQKA'
	cards = [ss.index(r) for r,s in cards]
	cards.sort(reverse=True)
	return cards

def straight(ranks):
	# Is this hand straight [9C,8D,7H,6S,5D] => 9
	return (ranks[0]-ranks[-1]==4) and len(set(ranks))==5

def flush(hand):
	# Is this a fulsh [D,D,D,D,D] => 1
	h = [s for r,s in hand]
	return len(set(h))==1

def kind(n,ranks):
	# Is there n kinds (2,[10,10,5,3,2]) => 10
	for r in ranks:
		if(ranks.count(r)==n): return r
	return None

def two_pairs(ranks):
	# is any pair there [10,10,8,8,4] => (10,8) / [3,4,5,6,7] => None
	high = kind(2,ranks)
	lower = kind(2,sorted(ranks))
	if(high and high!=lower):
		return (high,lower)
	return None

def test():
    # To be a good programmer you must be a good tester
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "3D 3C 4D 4C 8D".split()
    assert card_ranks(sf) == [10,9,8,7,6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]
    assert straight([9,8,7,6,5]) == True
    assert straight([9,8,7,6,4]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert kind(4,card_ranks(fk)) == 9
    assert kind(3,card_ranks(fk)) == None
    assert kind(2,card_ranks(fk)) == None
    assert kind(1,card_ranks(fk)) == 7
    assert two_pairs(card_ranks(tp)) == (4,3)
    assert two_pairs(card_ranks(sf)) == None
    assert poker([sf,fk,fh]) == sf
    assert poker([fk,fh]) == fk
    assert poker([fh,fh]) == fh
    assert poker([fh]) == fh
    assert poker([sf]+[fh]*99) == sf
    assert hand_rank(sf) == (8,10)
    assert hand_rank(fk) == (7,9,7)
    assert hand_rank(fh) == (6,10,7)
    t5 = "4C 5C 7C 8C 3C".split()
    t4 = "3D 4H 5D 6S 7C".split()
    t3 = "3D 3H 3S 5C 6D".split()
    t2 = "2D 3H 4S 2H 3D".split()
    t1 = "4D 4H 5D 6D 8C".split()
    t0 = "2D 5H 13D 5D 6C".split()
    assert hand_rank(t5) == (5,card_ranks(t5))
    assert hand_rank(t4) == (4,7)
    assert hand_rank(t3) == (3,3,card_ranks(t3))
    assert hand_rank(t2) == (2,(3,2),card_ranks(t2))
    assert hand_rank(t1) == (1,4,card_ranks(t1))
    assert hand_rank(t0) == (0,card_ranks(t0))
    print("Tests pass")

test()
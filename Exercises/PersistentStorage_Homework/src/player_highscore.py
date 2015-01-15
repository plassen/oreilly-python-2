import shelve

def zero_highscore():
    shelf = shelve.open('highscore.shlf')
    shelf.clear()
    shelf.close()

def manage_highscore(player, score):
    shelf = shelve.open('highscore.shlf', writeback = True)
    
    if player in shelf.keys():
        high_score = shelf[player]
        if score > high_score:
            shelf[player] = score
    else:
        shelf[player] = score
    shelf.close()
    
    shelf = shelve.open('highscore.shlf')
    high_score = shelf[player]
    shelf.close()
    
    return high_score

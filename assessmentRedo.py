def winCounter(powerListA, powerListB, powerListC):
    playerList = []
    for i in range(0, len(powerListA)):
        powers = [powerListA[i], powerListB[i], powerListC[i]]
        powers.sort(key=lambda x: -x)
        playerList.append(powers)

    print(playerList)

    

    winnerCounter = 0
    for player in playerList:
        opponentsBeaten = 0
        for opponent in playerList:
            if opponent is not player:
                if player[0] > opponent[1] and player[1] > opponent[2]:
                    opponentsBeaten += 1
                    
        if opponentsBeaten > len(playerList) - 2:
            winnerCounter += 1
    
    return winnerCounter


print(winCounter([8, 10, 9, 11], [2, 6, 7, 12], [4, 16, 3, 1]))

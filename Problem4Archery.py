#Problem 4

import random

score = 0
score_card = []
arrows = 0

while arrows <= 9:
    points = random.randint(0,10)
    score_card.append(points)
    if points == 0:
        arrows == arrows
    elif points == 10:
        score += 20
        arrows += 1
    else:
        score += points
        arrows += 1
    
    
    print(score)
    print(score_card)
    
    
    

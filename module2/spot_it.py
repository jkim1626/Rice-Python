import comp140_module2 as spotit

def incident(point, line, mod):
    if ((point[0] * line[0]) % mod + 
        (point[1] * line[1]) % mod + 
        (point[2] * line[2]) % mod) % mod == 0:
        return True
    
    return False

def equivalent(point1, point2, mod):
    coordx = ((point1[1] * point2[2]) % mod) - ((point1[2] * point2[1]) % mod) == 0
    coordy = ((point1[2] * point2[0]) % mod) - ((point1[0] * point2[2]) % mod) == 0
    coordz = ((point1[0] * point2[1]) % mod) - ((point1[1] * point2[0]) % mod) == 0
    
    return coordx and coordy and coordz
    
def generate_all_points(mod):
    points = [(mod - 1,mod - 1,mod - 1)]
    for num0 in range(mod):
        for num1 in range(mod):
            for num2 in range(mod):
                new_point = (num0,num1,num2)
                for point in points:
                    unique = True
                    if equivalent(new_point,point,mod):
                        unique = False
                        break
                if unique:
                    points.append(new_point)
   
    return points

def create_cards(list_points, list_lines, mod):
    deck = []
    for index_line in range(len(list_lines)):
        card = []
        for index_point in range(len(list_points)):
            if incident(list_points[index_point],list_lines[index_line],mod):
                card.append(index_point)
        deck.append(card)
    
    return deck

def run():
    modulus = 7
    points = generate_all_points(modulus)
    lines = points[:]
    deck = create_cards(points, lines, modulus)
    spotit.start(deck)

run()

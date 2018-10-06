import random

def files_and_strings():
    characters = "Diane Alicia Peter Eli Will Grace Zach Jason Kalinda Jackie Veronika Owen Cary Elsbeth Lucca"
    judges = "Abernathy Dunaway Cuesta Hovick Parks Winter Baxter Kuhn Wicks Chase Lessner James Sutman Dunn Lowrey"
    clients = "Sweeney Bishop Gross Roja Edelstein Dellinger Flores Grant Savarese Ashbaugh Gardner Dipple Hellinger Boies Locke Florrick"

    with open('cha.txt', 'w', encoding='utf-8') as f:
        f.write(characters)
    with open('jud.txt', 'w', encoding='utf-8') as f:
        f.write(judges)
    with open('cli.txt', 'w', encoding='utf-8') as f:
        f.write(clients)
    return

def register():
    ke = []
    va = []
    large = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    small = ('abcdefghijklmnopqrstuvwxyz')
    for x in large: ke.append(x)
    for y in small: va.append(y)
    dicti = dict(zip(ke, va))
    return (dicti)

def preparation_of_game():
    print("Hey! You have to protect the characters from The Good Wife.\nIf you need help with the characters please press 1, otherwise press 2)")
#    helping = input()
    print("\nYou can choose who you want them to be.")
    print('1 - characters, 2 - judges, 3 - clients')
    a = input()
    if a == '1':
        with open('cha.txt', encoding='utf-8') as f:
            characters = f.read()
#            if helping == 1:
#                print(characters)
        u = (characters.split())[random.randint(0, 14)]

    if a == '2':
        with open('jud.txt', encoding='utf-8') as f:
            judges = f.read()
            print(judges)
        u = (judges.split())[random.randint(0, 14)]
     
    if a == '3':
        with open('cli.txt',  encoding='utf-8') as f:
            clients = f.read()
            print(clients)
        u = (clients.split())[random.randint(0, 14)]
    b = []   
    for x in dicti:
        if x == (u[0]):
            b.append(dicti[x])
            b.append(u[1:len(u)])
            b = ('').join(b)
    c = []
    print('\nI am prepared to execute one of these good people. Can you save them? You will see a metaphorical image of a gun firing')
    print('Give me a letter!')
    for x in range (len(b)):
        c.append('_')
    print((' ').join(c))
    return(b, c, u)

def graphics():
    ba = ""
    ca = ""
    da = ""
    ea = ""
    fa = ""
    ga = ""
    ha = ""
    ia = ""
    ja = ""
    ka = ""
    la = ""
    ma = ""
    na = ""
    oa = ""
    pa = ""
    qa = ""
    ra = ""
    sa = ""
    ta = ""
    ua = ""
    arr = [ba,ca,da,ea,fa,ga,ha,ia,ja,ka,la,ma,na,oa,pa,qa,ra,sa,ta,ua]
    return(arr)
def popytki(y):
    if 30-y == 1:
        print('\nYou have', 30-y, 'попытка left')
    if 30-y == 2 or 30-y == 3 or 30-y == 4:
        print('\nYou have', 30-y, 'попытки left')
    else:
        print('\nYou have', 30-y, 'попыток left')
    return

def game():
    for y in range (30):
        if arr[19]== '*':
            print("You lost.")
            break
        popytki(y)
        y = y-1
        h = input()
        if h not in dicti.keys() and h not in dicti.values():
            print('watch it!')
            h = input()
        if h not in b:
            print(' |', arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13], arr[14], arr[15], arr[16], arr[17], arr[18], arr[19], '|' )
        arr[y+1] = '*'
        for w in range (len (b)):
            if b[w] == h:
                c[w] = h
                print((' ').join(c))
        if '_' not in c:
            print('Good! You saved')
            break
    print(u, '!')
    print('Wanna start over? Press 1 for YES and 2 for NO')
    return

files_and_strings()
dicti = register()
b, c, u = preparation_of_game()
arr = graphics()
game()

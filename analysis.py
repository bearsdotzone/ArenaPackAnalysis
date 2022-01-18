from locale import Error
import re, sys, argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('-i','--inputfile', default='input.txt', help="Indicate an input file, defaults to input.txt in pwd.")
parser.add_argument('-c', action='store_true', default=False, help="Show card frequency analysis, used for multiple decklists in one file.")
args = parser.parse_args()

f = None
if os.path.exists(args.inputfile):
    f = open(args.inputfile, "r")
else:
    raise FileNotFoundError(args.inputfile)

cards = dict()
sets = dict()
for x in f:
    if re.search("\d+ ", x) is None:
        continue

    # Search for set code
    temp = re.search("[\(\[].*[\)\]]", x)
    if  temp is not None:
        cardname = re.search("[^\d\s]", x)

        name = x[cardname.span()[0]:temp.span()[0]-1]

        if name in cards.keys():
            cards[name]+=1
        else:
            cards[name]=1

        temp = temp.group()[1:-1]
        if temp in sets.keys():
            sets[temp]+=1
        else:
            sets[temp]=1
    else:
        cardname = re.search("[^\d\s]", x)
        name = x[cardname.span()[0]:]

        if name in cards.keys():
            cards[name]+=1
        else:
            cards[name]=1

if(len(cards.items()) == 0):
    raise Error("No cards detected.")

if(len(sets.values()) != 0):
    for x in range(int(max(sets.values())), 0, -1):
        z = []
        for k,v in sets.items():
            if v is x:
                z += [k]

        if len(z) != 0:
            print(x, z)

if(args.c):
    print("Cards")
    for x in range(int(max(cards.values())), 0, -1):
        print(x)
        for k,v in cards.items():
            if v is x:
                print(k.strip())
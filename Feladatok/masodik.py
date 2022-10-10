p1 = input("player 1: (r, s, p)")
p2 = input("player 2: (r, s, p)")

while p1 == p2:
    p1 = input("player 1: (r, s, p)")
    p2 = input("player 2: (r, s, p)")
    print("Again!")

if p1 == "r" and p2 == "s":
    print("the first player is the winner")
elif  p1 == "s" and p2 == "r":
    print("the second player is the winner")

if p1 == "s" and p2 == "p":
    print("the first player is the winner")
elif  p1 == "p" and p2 == "s":
    print("the second player is the winner")

if p1 == "p" and p2 == "r":
    print("the first player is the winner")
elif  p1 == "r" and p2 == "p":
    print("the second player is the winner")
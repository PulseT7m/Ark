text="cheat spawnactor  \"Blueprint\'/Game/Genesis2/Structures/LoadoutMannequin/Structure_LoadoutDummy_Hotbar.Structure_LoadoutDummy_Hotbar\'\""
def hcc():
    lay=int(input("How many layers would you like there to be? "))
    xx=int(input("How many mannequins should be in each layer? "))
    rows=int(input("How many rows of mannequins should there be per layer? "))
    g=int(xx/rows)
    a,b,c=0,0,275
    for i in range(lay):
        for j in range(rows):
            a=0
            print(f"{text} 0 0 -{c}")
            for x in range(g):#wenn b 0 unterscheidung und dann b plus 140 
                print(f"{text} {a} {b} -{c}|")
                print(f"{text} {a} -{b} -{c}|")
                a=a+200
            b=b+140
        c=c+275
        
        
def vcc():
    lay=int(input("How many layers would you like there to be? "))
    xx=int(input("How many mannequins should be in each layer? "))
    rows=int(input("How many rows of mannequins should there be per layer? "))
    g=int(xx/rows)
    a,b,c=0,0,-140
    for i in range(lay):
        c=c+140
        for j in range(rows):
            a=0
            for x in range(g):
                print(f"{text} {a} {c} {b}|")
                a=a+200
            b=b+275

cc=int(input("What kind of custom cave code would you like to generate?(1=dropdowns;2=normal cave entrances) "))
if cc == 1:
    hcc()
elif cc == 2:
    vcc()
else:
    print("Error 404: Try again")

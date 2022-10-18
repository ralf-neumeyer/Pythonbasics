import random

namen = ['ralf' , 'dieter' , 'klaus' , 'hans']

def schmeichel():
    adjektiv = ['traurig' , 'freudig' , 'betrunken' , 'herzlich']
    norm = [ 'mensch' , 'hecht' , 'freund' , 'klumpel' , 'wannabe Programieren' ]
    out = "Du bist der" + " " + (random.choice(adjektiv)) + " " + (random.choice(norm)) + " !!!"
    return out

rueck = schmeichel()
print (rueck)
for name in namen :
    rueck = schmeichel()
    print (name + " " + schmeichel())







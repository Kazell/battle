import random
import time



#######        id - 1st position
#######        medals - 2nd position
#######        money - 3rd position
#######        attack - 4th position

def Gamer(id):
    g=[]
    name=any
    power=random.randint(1,1000)
    medals=1000
    money=0
    attack=0
    g.extend([power,id,medals,money,attack])
    return g


def choose():
    a=open('pull.txt').readlines()
    c=[]
    for i in list(a):
        c.append(i[:-1])
    k=random.choices(c, k=200)
    m=[]
    for i in k:
        l=Gamer(i)
        m.append(l)
        m.sort()
    return m

f=choose()
Game1=f[:50]
Game2=f[50:100]
Game3=f[100:150]
Game4=f[150:]



def agressors1():
    p=[]
    for k in Game1:
        if random.randint(0,1)==1:
            p.append(k)
    return p


def agressors2():
    p=[]
    for k in Game2:
        if random.randint(0,1)==1:
            p.append(k)
    return p

def agressors3():
    p=[]
    for k in Game3:
        if random.randint(0,1)==1:
            p.append(k)
    return p

def agressors4():
    p=[]
    for k in Game4:
        if random.randint(0,1)==1:
            p.append(k)
    return p


#print(agressors1())

#print(random.choices(Game1,k=50)) 


battle=[]

def victim1(agressor1):
    v=[]
    Game1_1=random.choices(Game1,k=50)
    for i in Game1_1:
        if i[1]!=agressor1[1]:
            for k in battle:
                if k[0]==agressor1[1]:
                    if i[1]!=k[1]:
                        v.append(k[1])
            else:
                v.append(i)
    return v




def victim2(agressor2):
    v=[]
    Game2_1=random.choices(Game2,k=50)
    for i in Game2_1:
        if i[1]!=agressor2[1]:
            for k in battle:
                if k[0]==agressor2[1]:
                    if i[1]!=k[1]:
                        v.append(k[1])
            else:
                v.append(i)
    return v

def victim3(agressor3):
    v=[]
    Game3_1=random.choices(Game3,k=50)
    for i in Game3_1:
        if i[1]!=agressor3[1]:
            for k in battle:
                if k[0]==agressor3[1]:
                    if i[1]!=k[1]:
                        v.append(k[1])
            else:
                v.append(i)
    return v


def victim4(agressor4):
    v=[]
    Game4_1=random.choices(Game4,k=50)
    for i in Game4_1:
        if i[1]!=agressor4[1]:
            for k in battle:
                if k[0]==agressor4[1]:
                    if i[1]!=k[1]:
                        v.append(k[1])
            else:
                v.append(i)
    return v
     


def GET_player(id):
    for i in f:
        if i[1]==id:
            print('id'+' => '+str(i[1])+'\n'
                'power'+' => '+str(i[0])+'\n'
                'medals'+' => '+str(i[2])+'\n'
                  'money'+' => '+str(i[3])+'\n'
                  'attack'+' => '+str(i[4]))



def POST_attack(from_player_id, to_player_id):
    r=random.randint(-10,10)
    from_player_id[2]+=r
    from_player_id[4]+=1
    battle.append([from_player_id[1], to_player_id[1]])
    to_player_id[2]-=r    
    #print('foo')
    return from_player_id, to_player_id

def POST_tournament():    
    for j in range(23):
        v2_1=[]
        v2_2=[]
        v2_3=[]
        v2_4=[]
        t1=time.time()
        a1=agressors1()        
        a2=[]
        for a in a1:
            if a not in a2:
                if a not in v2_1:
                   a2.append(a)
            b=victim1(a)
            for l in b:
                if l not in a2:
                     if l not in v2_1:
                          v2_1.append(l)                                ##### if you want to see pairs of fighters, erase all #
            #print(a)
            #print(l)
            POST_attack(a, l)
            #print('foof')
        a1_2=agressors2()        
        a2_2=[]
        for a in a1_2:
            if a not in a2_2:
                if a not in v2_2:
                   a2_2.append(a)
            b=victim2(a)
            for l in b:
                if l not in a2_2:
                     if l not in v2_2:
                          v2_2.append(l)
            #print(a)
            #print(l)
            POST_attack(a, l)
            #print('foof')
        a1_3=agressors3()        
        a2_3=[]
        for a in a1_3:
            if a not in a2_3:
                if a not in v2_3:
                   a2_3.append(a)
            b=victim3(a)
            for l in b:
                if l not in a2_3:
                     if l not in v2_3:
                          v2_3.append(l)
            #print(a)
            #print(l)
            POST_attack(a, l)
            #print('foof')
        a1_4=agressors4()        
        a2_4=[]
        for a in a1_4:
            if a not in a2_4:
                if a not in v2_4:
                   a2_4.append(a)
            b=victim4(a)
            for l in b:
                if l not in a2_4:
                     if l not in v2_4:
                          v2_4.append(l)
            #print(a)
            #print(l)
            POST_attack(a, l)
            #print('foof')
        t2=time.time()
        t=t2-t1
        time.sleep(5-t)                                                  ##### if you don't want to wait 120 sec, add # before time.sleep(5-t)
    loosers1=[]
    loosers2=[]
    loosers3=[]
    loosers4=[]
    v2_1=[]
    v2_2=[]
    v2_3=[]
    v2_4=[]
    for y in Game1:
        #print(y[4])
        if y[4]==0:
            loosers1.append(y)
    loo=[]
    for z in loosers1:
        for k in Game1:
            if k not in loosers1:
                if k not in loo:
                    loo.append(k)
        #print(z)
        #print(k)
        POST_attack(z, k)
        #print('at least')
    if loosers1==[]:
        a1=agressors1()        
        a2=[]
        for a in a1:
            if a not in a2:
                if a not in v2_1:
                   a2.append(a)
            b=victim1(a)
            for l in b:
                if l not in a2:
                     if l not in v2_1:
                          v2_1.append(l)
            #print(a)
            #print(l)
            POST_attack(a, l)
            #print('foof')
    for y in Game2:
        #print(y[4])
        if y[4]==0:
            loosers2.append(y)
    loo=[]
    for z in loosers2:
        for k in Game2:
            if k not in loosers2:
                if k not in loo:
                    loo.append(k)
        #print(z)
        #print(k)
        POST_attack(z, k)
        #print('at least')
    if loosers2==[]:
        a1_2=agressors2()        
        a2_2=[]
        for a in a1_2:
            if a not in a2_2:
                if a not in v2_2:
                   a2_2.append(a)
            b=victim2(a)
            for l in b:
                if l not in a2_2:
                     if l not in v2_2:
                          v2_2.append(l)
            #print(a)
            #print(l)
            POST_attack(a, l)
            #print('foof')
    for y in Game3:
        #print(y[4])
        if y[4]==0:
            loosers3.append(y)
    loo=[]
    for z in loosers3:
        for k in Game3:
            if k not in loosers3:
                if k not in loo:
                    loo.append(k)
        #print(z)
        #print(k)
        POST_attack(z, k)
        #print('at least')
    if loosers3==[]:
        a1_3=agressors3()        
        a2_3=[]
        for a in a1_3:
            if a not in a2_3:
                if a not in v2_3:
                   a2_3.append(a)
            b=victim3(a)
            for l in b:
                if l not in a2_3:
                     if l not in v2_3:
                          v2_3.append(l)
            #print(a)
            #print(l)
            POST_attack(a, l)
            #print('foof')
    for y in Game4:
        #print(y[4])
        if y[4]==0:
            loosers4.append(y)
    loo=[]
    for z in loosers4:
        for k in Game4:
            if k not in loosers4:
                if k not in loo:
                    loo.append(k)
        #print(z)
        #print(k)
        POST_attack(z, k)
        #print('at least')
    if loosers4==[]:
        a1_4=agressors4()        
        a2_4=[]
        for a in a1_4:
            if a not in a2_4:
                if a not in v2_4:
                   a2_4.append(a)
            b=victim4(a)
            for l in b:
                if l not in a2_4:
                     if l not in v2_4:
                          v2_4.append(l)
            #print(a)
            #print(l)
            POST_attack(a, l)
            #print('foof')
    yes=[]                                                         #getting list sorted by medals
    for g in Game1:
        yes.append(g[2])
        yes0=list(set(yes))
        yes0.sort()
    yes1=yes0[len(yes0)-1]
    yes2=yes0[len(yes0)-2]
    yes3=yes0[len(yes0)-3]
    for g1 in Game1:
        if g1[2]==yes1:
            g1[3]+=300
        elif g1[2]==yes2:
            g1[3]+=200
        elif g1[2]==yes3:
            g1[3]+=100
    yes=[]
    for g in Game2:
        yes.append(g[2])
        yes0=list(set(yes))
        yes0.sort()
    yes1=yes0[len(yes0)-1]
    yes2=yes0[len(yes0)-2]
    yes3=yes0[len(yes0)-3]
    for g1 in Game2:
        if g1[2]==yes1:
            g1[3]+=300
        elif g1[2]==yes2:
            g1[3]+=200
        elif g1[2]==yes3:
            g1[3]+=100
    yes=[]
    for g in Game3:
        yes.append(g[2])
        yes0=list(set(yes))
        yes0.sort()
    yes1=yes0[len(yes0)-1]
    yes2=yes0[len(yes0)-2]
    yes3=yes0[len(yes0)-3]
    for g1 in Game3:
        if g1[2]==yes1:
            g1[3]+=300
        elif g1[2]==yes2:
            g1[3]+=200
        elif g1[2]==yes3:
            g1[3]+=100
    yes=[]
    for g in Game4:
        yes.append(g[2])
        yes0=list(set(yes))
        yes0.sort()
    yes1=yes0[len(yes0)-1]
    yes2=yes0[len(yes0)-2]
    yes3=yes0[len(yes0)-3]
    for g1 in Game4:
        if g1[2]==yes1:
            g1[3]+=300
        elif g1[2]==yes2:
            g1[3]+=200
        elif g1[2]==yes3:
            g1[3]+=100
    return Game1, Game2, Game3, Game4
                    
POST_tournament()

#for k in f:                                                              #####if you want to see characteristicsof all 200 players, 'erase' #
#    print(GET_player (k[1]))


def GET_tornament():
    print('Winners in Group1')
    for i in Game1:        
        if i[3]==300:
            print('1st place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +300')
    for i in Game1:
        if i[3]==200:
            print('2nd place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +200')
    for i in Game1:
        if i[3]==100:
            print('3rd place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +100')
    print('\nWinners in Group2')
    for i in Game2:        
        if i[3]==300:
            print('1st place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +300')
    for i in Game2:
        if i[3]==200:
            print('2nd place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +200')
    for i in Game2:
        if i[3]==100:
            print('3rd place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +100')
    print('\nWinners in Group3')
    for i in Game3:        
        if i[3]==300:
            print('1st place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +300')
    for i in Game3:
        if i[3]==200:
            print('2nd place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +200')
    for i in Game3:
        if i[3]==100:
            print('3rd place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +100')
    print('\nWinners in Group4')
    for i in Game4:        
        if i[3]==300:
            print('1st place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +300')
    for i in Game4:
        if i[3]==200:
            print('2nd place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +200')
    for i in Game4:
        if i[3]==100:
            print('3rd place: \n'+
                  'id'+' -----> '+i[1]+'\n'+
                  'money'+' -----> +100')


GET_tornament()

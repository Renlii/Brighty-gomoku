import random
def SK(all_black,all_white,all_other):
    """This is calculate that which cordinate have the greatest value to both /
    himself and opponent"""
    real_zone_1=[]
    real_zone_2=[]
    real_zone_3=[]
    global p
    #FIRST I want to defin the zone value since the more center you are, the
    #more value you are.  Therefore....
    
    #Zone 1 __ the gratest value of the zone. 
    zone_1=[]
    zone_1_val=0.3
    for i in all_other:
        if 125<=int(i[0])<=1100 and 125<=int(i[1])<=825:
            zone_1.append(i)

    #zone 2
    zone_2=[]
    zone_2_val=0.2
    for i in all_other:
        if 0<=int(i[0])<=125 and 125<=int(i[1])<=825:
            zone_2.append(i)
        if 1100<=int(i[0])<=1225 and 125<=int(i[1])<=825:
            zone_2.append(i)
        if 125<=int(i[0])<=1100 and 0<=int(i[1])<=125:
            zone_2.append(i)
        if 125<=int(i[0])<=1100 and 825<=int(i[1])<=950:
            zone_2.append(i)

    #zone 3
    zone_3=[]
    zone_3_val=0.1
    for i in all_other:
        if 0<=int(i[0])<=125 and 0<=int(i[1])<=125:
            zone_3.append(i)
        if 0<=int(i[0])<=125 and 825<=int(i[1])<=950:
            zone_3.append(i)
        if 1100<=int(i[0])<=1225 and 0<=int(i[1])<=125:
            zone_3.append(i)
        if 1100<=int(i[0])<=1225 and 825<=int(i[1])<=950:
            zone_3.append(i)

    if all_black==[] and all_white==[]:
        p=0 #First hand Black
        #all_black.append([25*25,19*25])
        return[25*25,19*25]

    if all_black!=[] and all_white==[]:
        p=1 #Second hand White
        all_white.append([all_white[0][0]-25,all_white[0][1]+25])
        return[all_white[0][0]-25,all_white[0][1]+25]
    

    #Calculate value start!!!!
    val=0
    value_list=[] #[[坐标]，val]
    if p == 0: #First hand Black
        for i in all_black:
            x=i[0]
            y=i[1]
            #右下↘️
            if [x+25 ,y+25] in all_other:
                val=1
                value_list.append([[x+25,y+25],val])
                print('右下 if',val)
            else:
                val=1
                for a in range(1,4):
                    if [x+25*a,y+25*a] in all_black:
                        val+=1
                    else:
                        value_list.append([[x+25*a,y+25*a],val])
                        print('右下',val)
                        break
                
            #左上↖️
            if [x-25,y-25] in all_other:
                val=1
                value_list.append([[x-25,y-25],val])
                print('左上 if')
            else:
                val=1
                for a in range(1,4):
                    if [[x-25*a,y-25*a], val] in all_black:
                        val+=1
                    else:
                        value_list.append([[x-25*a,y-25*a],val])
                        print('左上')
                        break
                    
            #右上↗️        
            if [x+25,y-25] in all_other:
                val=1
                value_list.append([[x+25,y-25],val])
                print('右上 if')
            else:
                val=1
                for a in range(1,4):
                    if [x+25*a,y-25*a] in all_black:
                        val+=1
                    else:
                        value_list.append([[x+25*a,y-25*a],val])
                        print('右上')
                        break

            #左下↙️
            if [x-25,y+25] in all_other:
                if [x-25,y+25] in all_white:
                    print('WDNMD')
                val=1
                value_list.append([[x-25,y+25],val])
            else:
                val=1
                for a in range(1,4):
                    if [x-25*a,y+25*a] in all_black:
                        val+=1
                    else:
                        value_list.append([[x-25*a,y+25*a],val])
                        print('左下')
                        break

            #右➡️
            if [x+25,y] in all_other:
                val=1
                value_list.append([[x+25,y],val])
                print('右 if')
            else:
                val=1
                for a in range(1,4):
                    if [x+25*a,y] in all_black:
                        val+=1
                    else:
                        value_list.append([[x+25*a,y],val])
                        print('右')
                        break

            #左⬅️              
            if [i[0]-25,i[1]] in all_other:
                val=1
                value_list.append([[i[0]-25,i[1]],val])
                print('左 if')
            else:
                val=1
                for a in range(1,4):
                    if [i[0]-25*a,i[1]] in all_black:
                        val+=1
                    else:
                        value_list.append([[i[0]-25*a,i[1]],val])
                        print('左')
                        break

            #下⬇️                   
            if [i[0],i[1]+25] in all_other:
                if [i[0],i[1]+25] in all_white:
                    print('WDNMDAAAAAA')
                val=1
                value_list.append([[i[0],i[1]+25],val])
            else:
                val=1
                for a in range(1,4):
                    if [i[0],i[1]+25*a] in all_black:
                        val+=1
                    else:
                        value_list.append([[i[0],i[1]+25*a],val])
                        print('下')
                        break
                    
            #上⬆️
            if [i[0],i[1]-25] in all_other:
                val=1
                value_list.append([[i[0],i[1]-25],val])
            else:
                val=1
                for a in range(1,4):
                    if [i[0],i[1]-25*a] in all_black:
                        val+=1
                    else:
                        value_list.append([[i[0],i[1]-25*a],val])
                        print('上')
                        break



    all_val=[]
    lv=len(value_list)
    value_list=value_list[:lv//2]
    print(value_list)

    
    sum_value=[]
    for a in value_list:
        for b in value_list:
            if a[0] == b[0]:
                sum_1 = int(a[1])+int(b[1])
                sum_value.append([a[0],sum_1])




    

    print(sum_value)
    for i in sum_value:
        all_val.append(i[1])
    print(all_val)
    numb=-1
    all_max=[]
    for v in all_val:
        numb+=1
        if v == max(all_val):
            max_val_list = value_list[numb][0] #最大值的xy坐标
            if value_list[numb][0] in all_other:
                all_max.append(value_list[numb])
    print(all_max,'all_max is this shit')
            
    print(max(all_val),'max val')
    for u in all_max:
        if u[0] in zone_1:
            real_zone_1.append(u[0])
        if u[0] in zone_2:
            real_zone_2.append(u[0])
        if u[0] in zone_3:
            real_zone_3.append(u[0])
    if real_zone_1 != []:
        print('real_1')
        return real_zone_1[0]
    elif real_zone_2 != []:
        print('Its zone 2')
        return real_zone_2[0]
    elif real_zone_3 != []:
        print('Its zone 3')
        return real_zone_3[0]
    else:
        return "mistake"



    











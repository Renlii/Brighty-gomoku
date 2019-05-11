import random
def SK(all_black,all_white,all_other):
    """This is the function that calculate cordinates's value for both side players"""
    real_zone_1=[]
    real_zone_2=[]
    real_zone_3=[]
    global p
    #FIRST defining the zone value since the more center you are, the
    #more value you will have.
    
    #Zone 1: the gratest value zone
    zone_1=[]
    zone_1_val=0.3
    for i in all_other:
        if 125<=int(i[0])<=1100 and 125<=int(i[1])<=825:
            zone_1.append(i)

    #zone 2: second greatest value zone
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

    #zone 3: smallest value zone
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


  

    #Calculation of the values
    val=0
    value_list=[] #[[coordinate]，val]
    if p == 0: #First hand Black
        for i in all_black:
            x=i[0]
            y=i[1]
            #right down↘️
            if [x+25 ,y+25] in all_other:
                val=1
                value_list.append([[x+25,y+25],val])
                #print('右下 if',value_list)
                #print('Right D if',val)
            else:
                val=1
                for a in range(1,4):
                    if [x+25*a,y+25*a] in all_black:
                        val+=1
                    elif [x+25*a,y+25*a] in all_other:
                        value_list.append([[x+25*a,y+25*a],val])
                        #print('Right D',val)
                        #print('右下',value_list)
                    elif [x+25*a,y+25*a] in all_white:
                        break
                
            #left up↖️
            if [x-25,y-25] in all_other:
                val=1
                value_list.append([[x-25,y-25],val])
                #print('Left U if')
            else:
                val=1
                for a in range(1,4):
                    if [x-25*a,y-25*a] in all_black:
                        val+=1
                    elif [x-25*a,y-25*a] in all_other:
                        value_list.append([[x-25*a,y-25*a],val])
                        #print('Left U')
                    elif [x-25*a,y-25*a] in all_white:
                        break
                    
            #right up↗️        
            if [x+25,y-25] in all_other:
                val=1
                value_list.append([[x+25,y-25],val])
                #print('RU if')
            else:
                val=1
                for a in range(1,4):
                    if [x+25*a,y-25*a] in all_black:
                        val+=1
                    elif [x+25*a,y-25*a] in all_other:
                        value_list.append([[x+25*a,y-25*a],val])
                        #print('右上')
                    elif [x+25*a,y-25*a] in all_white:
                        break

            #left down↙️
            if [x-25,y+25] in all_other:
                val=1
                value_list.append([[x-25,y+25],val])
                #print('左下 if')                
            else:
                val=1
                for a in range(1,4):
                    if [x-25*a,y+25*a] in all_black:
                        val+=1
                    elif [x-25*a,y+25*a] in all_other:
                        value_list.append([[x-25*a,y+25*a],val])
                        #print('左下')
                    elif [x-25*a,y+25*a] in all_white:
                        break

            #right➡️
            if [x+25,y] in all_other:
                val=1
                value_list.append([[x+25,y],val])
                #print('右',value_list)
                #print('右 if')
            else:
                val=1
                for a in range(1,4):
                    if [x+25*a,y] in all_black:
                        val+=1
                    elif [x+25*a,y] in all_other:
                        value_list.append([[x+25*a,y],val])
                        #print('右')
                    elif [x+25*a,y] in all_white:
                        break

            #left⬅️              
            if [i[0]-25,i[1]] in all_other:
                val=1
                value_list.append([[i[0]-25,i[1]],val])
                #print('左', value_list)
                #print('左 if')
            else:
                val=1
                for a in range(1,4):
                    if [i[0]-25*a,i[1]] in all_black:
                        val+=1
                    elif [i[0]-25*a,i[1]] in all_other:
                        value_list.append([[i[0]-25*a,i[1]],val])
                        #print('左')
                    elif [i[0]-25*a,i[1]] in all_white:
                        break

            #down⬇️                   
            if [i[0],i[1]+25] in all_other:
                val=1
                value_list.append([[i[0],i[1]+25],val])
                #print('下', value_list)
                #print('下 if')
            else:
                val=1
                for a in range(1,4):
                    if [i[0],i[1]+25*a] in all_black:
                        val+=1
                    elif [i[0],i[1]+25*a] in all_other:
                        value_list.append([[i[0],i[1]+25*a],val])
                        #print('下')
                    elif [i[0],i[1]+25*a] in all_white:
                        break
                    
            #up⬆️
            if [i[0],i[1]-25] in all_other:
                val=1
                value_list.append([[i[0],i[1]-25],val])
                #print('上',value_list)
                #print('上 if')
            else:
                val=1
                for a in range(1,4):
                    if [i[0],i[1]-25*a] in all_black:
                        val+=1
                    elif [i[0],i[1]-25*a] in all_other:
                        value_list.append([[i[0],i[1]-25*a],val])
                        #print('上')
                    elif [i[0],i[1]-25*a] in all_white:
                        break



    all_val=[]
    #print(value_list,'这是value_list')

    
    sum_value=[]
    coord=[]
    for a in value_list:
        if a[0] not in coord:
            coord.append(a[0])
    #print(coord)
    for b in coord:
        he=[]
        for c in value_list:
            if b == c[0]:
                he.append(c[1])
        #print(he,'这是和')
        sum_value.append([b,sum(he)])



    #print(sum_value,'同样坐标下val相加')
    for i in sum_value:
        all_val.append(i[1])
    #print(all_val,'所有的相加之后的val')
    numb=-1
    all_max=[]
    for v in all_val:
        numb+=1
        if v == max(all_val):
            max_val_list = value_list[numb][0] #max (x,y)
            if value_list[numb][0] in all_other:
                all_max.append(value_list[numb])
  
            
    #print(max(all_val),'max val')
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



    



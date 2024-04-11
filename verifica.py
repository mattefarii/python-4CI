#punto 1
dict={        "AA123BB":[("Giugno",(9,4,5,7),1293),("Luglio",(14,3,5,12),3231),("Agosto",(19,14,15,17),4020),("Settembre",(6,8,5,7),3928)],
              "AB345CD":[("Giugno",(20,24,15,7),1391),("Luglio",(9,14,5,17),1234),("Agosto",(20,24,15,17),4932,("Settembre",(10,14,5,7),2872))],
              "CD456FF":[("Giugno",(10,14,5,7),2872),("Luglio",(19,4,15,7),3273),("Agosto",(20,14,6,6),3211,("Settembre",(10,14,5,7),2827))],
}

#punto 2
dict["ZZ999CN"]=[("FM",(10,10,10,10),8000)]

#punto 3
for chiave,valore in dict.items():
    for mese in valore:
        dict[valore]=[("Ottobre",(5,5,5,5),2000)]

   
#punto 4
for chiave,valori in dict.items():
    if (chiave=="AA123BB"):
        for tupla in valori:
            if(tupla[0]=="Settembre"):
                print(tupla)

#punto 5
for chiave,valori in dict.items():
    if (chiave=="CD456FF"):
        for tupla in valori:
            if(tupla[0]=="Luglio"):
                print(tupla)

#punto 6
for chiave,valori in dict.items():
    if (chiave=="AA123BB"):
        for tupla in valori:
            if(tupla[0]=="Luglio"):
                print(tupla[1][0])
                print(tupla[1][1])
                print(tupla[1][2])
                print(tupla[1][3])

#punto 7
for chiave,valori in dict.items():
    max=0
    for tupla in valori:
        if(tupla[0]=="Luglio"):
            if(tupla[1][1]>max):
                max=tupla[1][1]
            elif (tupla[2][1]<max):
                max=tupla[2][1]
            elif (tupla[3][1]<max):
                max=tupla[3][1]
                print(max)


#punto 8
for chiave,valori in dict.items():
    sommaKm=0
    if (chiave=="AA123BB"):
        for tupla in valori:
            if(tupla[2]>sommaKm):
                sommaKm+=tupla[2]
    elif(chiave=="AB345CD"):
        for tupla in valori:
            if(tupla[2]>sommaKm):
                sommaKm+=tupla[2]
    elif(chiave=="CD456FF"):
        for tupla in valori:
            if(tupla[2]>sommaKm):
                sommaKm+=tupla[2]
print(sommaKm)

#punto 9
for chiave,valori in dict.items():
    kmMax=0
    if (chiave=="CD456FF"):
         for tupla in valori:
             if(tupla[2]>kmMax):
                 kmMax=tupla[2]
                 print(kmMax)

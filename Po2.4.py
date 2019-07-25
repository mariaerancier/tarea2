lista = ['aza', 'xyz', 'bac', '535','ebe']
c = 0
for a in lista:
    if len(a)>2 and a[0]==a[len(a)-1]:
        c=c+1
print("La cantidad es: "+str(c))

def pizza():
    list1=['1.SweetCorn Pizza','2. Cheese Pizza','3.Capsicum Pizza','4.Onion Pizza','5.Macroni & Cheese Pizza','6.Pepperoni Pizza','7.Margherita Pizza','8.Hawaiin Pizza']
    for x in list1:
        print(x)
        
def toppings():
    l3=['1. Bacon','2. Olives','3. Ham','4. Mushrooms','5. Pineapple','6. Salami','7. Anchovies']
    for z in l3:
        print(z)
quant=1
t1=1
list5=[]
list6=[]
print('Welcome To Pizzeria Hut')
pizza()
p=int(input('\n Select Your Pizza= '))
print('\nNote: All Pizzas Come With Tomato Base')
if p==1:
        list5.append('SweetCorn Pizza')
elif p==2:
        list5.append('Cheese Pizza')
elif p==3:
        list5.append('Capsicum Pizza')
elif p==4:
        list5.append('Onion Pizza')
elif p==5:
        list5.append('Macroni & Cheese Pizza')
elif p==6:
        list5.append('Margherita Pizza')
elif p==7:
	    list5.append('Hawaiin Pizza')	
for b in list5:
    	print('\n ',b,'Is Selected')
def size():
    
    print('\nSelect Size Of Pizza...')
    l2=['1. Regular(Rs 100)','2. Medium(Rs 130)','3. Large(Rs 180)']
    for y in l2:
        print(y)
size()
s=int(input('Choose Your Pizza Size= '))
if s==1:
        pr=100
        list6.append('Regular(Rs 100)')
elif s==2:
        list6.append('Medium(Rs 130)')
        pr=130
elif s==3:
        list6.append('Large(Rs 180)')
        pr=180
print('\n ',list6,'Is Selected')
m=input('\nDo You Want To Order More Pizza (Y/N): ')
if m=='Y':
    quant=quant+1
    pizza()
    p=int(input('\n Select Your Pizza: '))
    if p==1:
        list5.append('SweetCorn Pizza')
    elif p==2:
        list5.append('Cheese Pizza')
    elif p==3:
        list5.append('Capsicum Pizza')
    elif p==4:
        list5.append('Onion Pizza')
    elif p==5:
        list5.append('Macroni & Cheese Pizza')
    elif p==6:
        list5.append('Margherita Pizza')
    elif p==7:
    	list5.append('Hawaiin Pizza')
    for b in list5:
    	print('\n ',b,'Is Selected')
    size()
    s=int(input('Choose Your Pizza Size='))
    if s==1:
        pr=pr+100
        list6.append('Regular(Rs 100)')
    elif s==2:
        list6.append('Medium(Rs 130)')
        pr=pr+130
    elif s==3:
        list6.append('Large(Rs 180)')
        pr=pr+180
    print('\n ',list6,'Is Selected')
    print('\nWhich Topping Do You Want To Choose')
    print('\nNote: Cheese is By Default Topping\n')
    toppings()    
    list4=[]
    topp=int(input('How Many Toppings Do You Want To Choose(Max 4)='))
    b=1
    while b<=topp:
        t=int(input('\nWhich Topping Do You Want To Choose='))
        b=b+1
        if t==1:
        	list4.append('Bacon')
        elif t==2:
        	list4.append('Olives')
        elif t==3:
        	list4.append('Ham')
        elif t==4:
        	list4.append('Mushrooms')
        elif t==5:
        	list4.append('Pineapple')
        elif t==6:
        	list4.append('Salami')
        elif t==7:
        	list4.append('Anchovies')

        print('\nChoose Delivery Option')
        d=input('\nTake Away(T) Or Home Delivery(H)= ')
        if d=='T':
         nm=input('\nEnter Your Name= ')
         ph=int(input('\nEnter Your Mobile Number= '))
         print('\nQuantity= ',quant)
         pbill=quant*pr
         print('\nPrice= ',pbill)
         tbill=topp*10
         print('\nToppings Bill= ',tbill)
         nbill=pbill+tbill
         print('\nNet Bill= ',nbill)
        elif d=='H':
        	nm=input('\nEnter Your Name= ')
        	ph=int(input('\nEnter Your Mobile Number='))
        	address=input('\nAddress= ')
        	print('\nQuantity= ',quant)
        	pbill=quant*pr
        	print('\nPrice= ',pbill)
        	tbill=topp*10
        	print('\nToppings Bill=',tbill)
        	nbill=pbill+tbill
        	print('\nNet Bill= ',nbill)
        	if nbill<150:
        	 	dchrg=20
        	else:
        	 	dchrg=0
        	net=nbill+dchrg
        	print('\nNet Bill=',net)
         
elif m=='N':
    quant=quant+0
print('\nWhich Topping Do You Want To Choose')
print('\nNote: Cheese is By Default Topping\n')
toppings()
l4=[]
topp=int(input('How Many Toppings Do You Want To Choose(Max 4): '))
a=1
while a<=topp:
        t=int(input('\nWhich Topping Do You Want To Choose: '))
        a=a+1
        if t==1:
        	l4.append('Bacon')
        elif t==2:
        	l4.append('Olives')
        elif t==3:
        	l4.append('Ham')
        elif t==4:
        	l4.append('Mushrooms')
        elif t==5:
        	l4.append('Pineapple')
        elif t==6:
        	l4.append('Salami')
        elif t==7:
        	l4.append('Anchovies')
        
print('\nChoose Delivery Option')
d=input('\nTake Away(T) Or Home Delivery(H): ')
if d=='T':
 	       nm=input('\nEnter Your Name= ')
 	       ph=int(input('\nEnter Your Mobile Number='))
 	       print('\nPrinting Bill......')
 	       print('\nQuantity= ',quant)
 	       pbill=quant*pr
 	       print('\nPrice=',pbill)
 	       tbill=topp*10
 	       print('Toppings Bill: ',tbill)
 	       nbill=pbill+tbill
 	       print('\nNet Bill: ',nbill)
elif d=='H':
	nm=input('\nEnter Your Name: ')
	ph=int(input('\nEnter Your Mobile Number: '))
	adress=input('\nAddress: ')
	print('\nQuantity: ',quant)
	pbill=quant*pr
	print('\nPrice: ',pbill)
	tbill=topp*10
	print('\nToppings Bill: ',tbill)
	nbill=pbill+tbill
	print('\nBill: ',nbill)
	if nbill<150:
		dchrg=20
	else:
		dchrg=0
	net=nbill+dchrg
	print('\nNet Bill: ',net)
    
def encontrar_valor(list2):
	list2=[]
	for i in list1:
		if i not in list2 :
			list2.append(i)
	list2.sort()
	print(list2)


list1=[1,2,3,2,6,7,8,8,9,7,5]	
encontrar_valor(list1)	


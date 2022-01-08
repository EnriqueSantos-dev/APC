def v (text):
	dic={}
	o_a=text.count("a")
	dic['a']=o_a
	o_e=text.count("e")
	dic['e']=o_e
	o_i=text.count("i")
	dic['i']=o_i
	o_o=text.count("o")
	dic['o']=o_o
	o_u=text.count("u")
	dic['u']=o_u
	print(dic)


text=input("digite seu texto:")
text=text.lower()
v(text)


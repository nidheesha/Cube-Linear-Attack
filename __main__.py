from parser import Parser
from cube_attack import RandomCubeAttack
from trivium_cube_attack import TriviumCubeAttack

def main():

    args = Parser().args
    #print(args)

    if args.mode=="random":

        ca = RandomCubeAttack(degree=args.degree,equation = args.equation)
        sps = ca.execute_offline_attack()
        equations = ca.execute_online_attack(sps)
        print(ca.possible_maxterms)

        print("\n\n\n")
#find the superpoly keys
        superpoly_terms = {}
        for maxterm in sps.keys():
            for k in sps[maxterm].keys(): 
                if (sps[maxterm][k] == 1):
                    superpoly_terms[k]=1

        keys = []            
        for k in superpoly_terms.keys():
        	keys.append(k)

        print("found keys ==="+" ".join(keys))	
        #print(" ".join(keys))	
        n_terms = len(superpoly_terms)
        assign_strings = []
        #print(n_terms)

#generating the assign terms
        for i in range(2**n_terms):
        	assign_string = format(i,'b')
        	while len(assign_string) != n_terms:
        		assign_string = '0' + assign_string
    		assign_strings.append(assign_string)
    		#print(assign_string," ".join(assign_strings),"\n")
        backup = args.equation.split(" ")


        
# assigning the assign terms and calling the randomfunc
        for value in assign_strings:
        	current_assignment = {} 
        	for i,j in enumerate(value):
        		#print(i,j,"\n")
        		current_assignment[keys[i-1]] = j
    			#print(keys[i-1],j)
        	poly_terms = args.equation.split(" ")
        	
        	for k in current_assignment.keys():
        		remove_terms = []
        		if(current_assignment[k]=='0'): 
        			print("found the "+ k + " as 0 so removing the terms")
        			for t in poly_terms:
        				if(t.find(k)!= -1):
        					#print("in zero",t.find(k),k,t)
        					#t.__contains__(k)):
        					#poly_terms.remove(t)
        					remove_terms.append(t)
        					#print(" ".join(poly_terms),"\n"," ".join(remove_terms))
        			for t in remove_terms:
        				poly_terms.remove(t)
        		else:
        			#print("found the "+ k + " as 1 so replacing the terms")
        			#print("before replace"+" ".join(poly_terms))
        			poly_terms= [poly_term.replace(k, '') for poly_term in poly_terms]
        			#print("after replace"+" ".join(poly_terms))

        			# for t in poly_terms:
        				# if(t.find(k)!= -1):
        					#print("in one",t.find(k),k,t)
        					#t.__contains__(k)):
        					# t.replace(k,"")
        					# index = poly_terms.index(t)
        					# print(t,k)
        					# print(index)
        					# poly_terms[index].replace(k,"")

        					#print(" ".join(poly_terms))
#finding the nonlinear terms
        	nonlinear_mon = []
        	for t in poly_terms:
        		if t.count('x') >1:
        			nonlinear_mon.append(t)

        	counting_x = []
        	counting_v = []
        	while len(counting_x)< args.nx or  len(counting_v)<args.nv:
        		if(len(counting_x)< args.nx and  len(counting_v)<args.nv):
        			max_freq_term = algo2(nonlinear_mon)
        		elif(len(counting_x)< args.nx):
        			max_freq_term = algo2(nonlinear_mon,'x')
        		elif(len(counting_v)< args.nv):
        			max_freq_term = algo2(nonlinear_mon,'v')

        		if(max_freq_term.find('x')!=-1):
        			counting_x.append(max_freq_term)
        		else:
        			counting_v.append(max_freq_term)

        		#print ("removing....", max_freq_term," from ", " ".join(nonlinear_mon))
        		#print ("removing....", max_freq_term," from ", " ".join(poly_terms))
        		nonlinear_mon = remove_max_freq_term(nonlinear_mon,max_freq_term)
        		poly_terms = remove_max_freq_term(poly_terms,max_freq_term)

        		#print ("after removing....", max_freq_term," from ", " ".join(nonlinear_mon))
        		#print ("after removing....", max_freq_term," from ", " ".join(poly_terms))

        	equations = ""
        	#print(" ".join(backup))
        	equations= " ".join(poly_terms)
        	#print(equations)
        	ca1 = RandomCubeAttack(degree=args.degree,equation = equations)
	        sps1 = ca1.execute_offline_attack()
	        equations1 = ca1.execute_online_attack(sps1)
	        print(ca1.possible_maxterms)
        	print("\n\n\n")

        
        #print("in random")

    elif args.mode=="trivium":
    	print("in trivium mode")
        f = TriviumCubeAttack(args.n_rounds)
       # sps = f.execute_offline_attack()
       # equations = f.execute_online_attack(sps)

        #print(ca.possible_maxterms)

        print(f.test_maxterm("v1", 288))
        print("in trivium")

def algo2(nonlinear_mon,find = ''):
	counting = {}
	for t in nonlinear_mon:
		split = t.split("v");
		#print(" ".join(split))
		if split[0] == "":
			split.pop(0)
		# if(split[0][0] == 'x')
		for s in split:
			if(s.find('x') == -1):
				if ('v'+s) in counting:
					#print("incrementing v",s)
					counting['v'+s]+=1
				else:
					#print("initialising v",s)
					counting['v'+s]=1
			else:
				split2=s.split('x')
				#print(" ".join(split2))
				if(split2[0] != ''):
					if ('v'+split2[0]) in counting:
						#print("incrementing v",split2[0])
						counting['v'+split2[0]]+=1
					else:
						#print("initialising v",split2[0])
						counting['v'+split2[0]] = 1 
					split2.pop(0)
				elif (split2[0]== ""):
					split2.pop(0)
				for t in split2:
					if('x'+t) in counting:
						#print("incrementing x",t)
						counting['x'+t]+=1
					else:
						#print("initialising x",t)
						counting['x'+t]=1


	highest = max(counting.values())
	counting =  {k:v for k, v in counting.items() if v == highest}
	for t in counting:
		print(t)
	if(len(counting)>=2):
		for t in counting.keys():
			for k in nonlinear_mon:
				if k.count(t) == 2 :
					counting[t]+= 1
	print("counting after counting second degree")
	#for t in counting:
		#print(t,counting[t])
	
	if(find == ''):
		return max(counting, key = counting.get)
	elif find == 'x':
		counting_x = {}
		for t in counting:
			if(t.find('x') != -1):
				counting_x[t] = counting[t]
		return max(counting_x, key = counting_x.get)
	elif find == 'v':
		counting_v = {}
		for t in counting:
			if(t.find('v') != -1):
				counting_v[t] = counting[t]
		return max(counting_v, key = counting_v.get)


def remove_max_freq_term(nonlinear_mon,max_freq_term):
	remove_terms=[]
	for t in nonlinear_mon:
		if(t.find(max_freq_term)!=-1):
			remove_terms.append(t)
	for t in remove_terms:
		nonlinear_mon.remove(t)

	return nonlinear_mon


main()
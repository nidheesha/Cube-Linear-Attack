import numpy as np
import re




#print(np.random.choice(2,2**6))
#print(np.random.randint(0,2,2**6))
#print(format(2,'b'))
#print("seisysyttt".replace("sy",""))

t = ["v1x2","x1x2"]

for k in t:
	k=k.replace('x','z')

print(" ".join(t))

words = ['how', 'much', 'is[br]', 'the', 'fish[br]cuy', 'no', 'really']
words = [w.replace('[br]', '<br />') for w in words]
print(" ".join(words))

# k = t[1].split("v")
# #k = re.split("v|x",t[1])
# print("  ".join(k))
# print(k)

# if(t[0].__contains__('c')):
# 	print("yes")


# for i in range(2**2):
# 	print("k")


# nonlinear_mon = ['v1v2x2','x1x1','v1v2']
# counting = {}
# for t in nonlinear_mon:
# 	split = t.split("v");
# 	print(" ".join(split))
# 	if split[0] == "":
# 		split.pop(0)
# 	# if(split[0][0] == 'x')
# 	for s in split:
# 		if(s.find('x') == -1):
# 			if ('v'+s) in counting:
# 				counting['v'+s]+=1
# 			else:
# 				counting['v'+s]=1
# 		else:
# 			split2=s.split('x')
# 			print(" ".join(split2))
# 			if(split2[0] != ''):
# 				if ('v'+split2[0]) in counting:
# 					counting['v'+split2[0]]+=1
# 				else:
# 					counting['v'+split2[0]] = 1 
# 				split2.pop(0)
# 			elif (split2[0]== ""):
# 				split2.pop(0)
# 			for t in split2:
# 				if('x'+t) in counting:
# 					counting['x'+t]+=1
# 				else:
# 					counting['x'+t]=1
    			
# for t in counting.keys():
# 	print(t,counting[t])

# # highest = max(counting.values())
# # print([k for k, v in counting.items() if v == highest])
# if(len(counting)>=2):
# 	for t in counting.keys():
# 		for k in nonlinear_mon:
# 			if k.count(t) == 2 :
# 				counting[t]+=1

# print(max(zip(counting.values(),counting.keys())))
# print(max(counting,key = counting.get))


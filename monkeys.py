# import enchant
import random
import string
from numpy.random import choice
import enchant
import re

d = enchant.Dict("en_US")
print(d.check("rollaaa"))
print(d.check("hello"))

# list_of_candidates = [1,2,3,4,5]
# number_of_items_to_pick = 3
# probability_distribution = [.1,.1,.1,.1,.6]
# draw = choice(list_of_candidates, number_of_items_to_pick, p=probability_distribution)

alpha_list = ["E","T","A","O","I","N","S","R","H","D","L","U","C","M","F","Y","W","G","P","B","V","K","X","Q","J","Z"]
alpha_list = [x.lower() for x in alpha_list]
alpha_num = 5000
alpha_perc = [12.02,9.10,8.12,7.68,7.31,6.95,6.28,6.02,5.92,4.32,3.98,2.88,2.71,2.61,2.30,2.11,2.09,2.03,1.82,1.49,1.11,0.69,0.17,0.11,0.10,0.07,]
alpha_dist = [x / 100 for x in alpha_perc]

s = choice(alpha_list,alpha_num,alpha_dist)
s = (string.join(s,""))
print(s)
slength = 4
def chunkstring(string, length = slength, offset = 0):
    return (string[offset+i:length+i+offset] for i in range(0, len(string), length))


cs = chunkstring(s)
# print(list(cs))
# cs = chunkstring(s,5,1)
# print(list(cs))

realwords = []

for j in range(0,slength):
	for i in list(cs):
		print(i + " ")
		print(d.check(i))
		if d.check(i) == True:
			realwords.append(i)
print(realwords)

realwords.append("the")
print(realwords)

for i in range(0,alpha_num-10):
	for j in range(10,2,-1):
		wrd = s[i:i+j]
		if d.check(wrd) == True:
			realwords.append(wrd)
			break;


print(realwords)
print(d.check("bl"))

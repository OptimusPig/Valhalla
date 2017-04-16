import itertools

list=[123,325,543,642,123,64577]

for i in list:
	for num in itertools.permutations(str(i),len(str(i))):
		
		if(int(''.join(num))%8):
			print "No"
		else:
			print "Yes"
# for num in itertools.permutations('1234',4):
# 		print ''.join(num)
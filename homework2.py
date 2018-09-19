#homework 2 
#michael Knapp 
#3-6-2018
#knapp296@live.missouristate.edu
import math
import operator
import csv


	
'''def cvsTrain():
		trData = []
		with open("MNIST_train.csv", "r") as file:
				fs = csv.reader(file)
				first_row = True
				for line in fs:
					if first_row:
						first_row = False
						continue
					line = list(map(int, line))
					trData.append((line[0], line[1:]))
				
		return trData'''


def cvsRead(filename):
		Data = []
		with open(filename, "r") as file:
				fs = csv.reader(file)
				first_row = True
				for line in fs:
					if first_row:
						first_row = False
						continue
					line = list(map(int, line))
					Data.append((line[0] , line[1:]))
					
			
		return Data

		
def knnTrainingData(trainingData, test, k):
		neighbors=[]
		t_class = test[0]
		t_attr = test[1]
		for data in trainingData:
			distance = 0
			d_class = data[0]
			d_attr = data[1]
			
			for index in range(len(t_attr)):
				distance += (t_attr[index] - d_attr[index]) ** 2
			
			distance = math.sqrt(distance)
			if len(neighbors) < k: 
				neighbors.append((distance, d_class))
			else:
				i = max(neighbors)
				if i[0] >= distance:	
					neighbors.remove(i)
					neighbors.append((distance, d_class))
						
			
		return voting(neighbors)    
		
def voting(neighbors):
	counts = {}
	for i in neighbors:
		if (i[1] not in counts):
			counts.update({i[1]: 0})
		
		counts[i[1]] += 1 /i[0]
		
	best = max(counts, key=counts.get)
		
	
	return best		
		
def main():
	print ("*******************")
	k = 7
	
	trainingData = cvsRead("MNIST_train.csv")
	testData = cvsRead("MNIST_test.csv")
	Y=0;
	print("The Value of K is:", k)
	for test in testData:
		n = knnTrainingData(trainingData, test, k)
		m = test[0]
		print("desired class:"  , m , "Computed Class:", n)
		if( m != n): 
			Y+=1
	total = len(testData)
			
	print("Accurcy rate is:", ((total- Y) /total)*100 ,"%")
	
	print ("Number of missclassified test samples", Y)
	print ("total numbers of test samples", total)
	
	
main()
	

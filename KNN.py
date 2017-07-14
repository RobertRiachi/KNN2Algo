from scipy.spatial import distance
import random

def edist(x,y):
	return distance.euclidean(x,y)

class KNN():
	def fit(self, X_train, Y_train):
		self.X_train = X_train
		self.Y_train = y_train
		
	def predict(self, X_test):
		predicts = []
		len = len(X_test)
		
		for i in range(0, len):
			classify = self.nearest(i)
			predicts.append(classify)
		return predicts	
	
	def choice(self, bestindex, secondbestindex):
	  x = [self.Y_train[bestindex],self.Y_train[secondbestindex]]
	  return random.choice(x)
		
	def closest(self, data):
		bestdistance = None
		bestindex = None
		secondbestdist = None
		secondbestindex = None
		len = len(self.X_train)
		
		for i in range(0, len):
			d = edist(self.X_train[i], data)
			if d < bestdistance:
				secondbestdist = bestdistance
				secondbestindex = bestindex
				bestdistance = d
				bestindex = i
			elif d < secondbestdist:
				secondbestdist = d
				secondbestindex = i
		return choice(bestindex, secondbestindex)
		
	print("Love, -Robert")

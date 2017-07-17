from scipy.spatial import distance
from collections import Counter

def edist(x,y):
	return distance.euclidean(x,y)
	
def Most_Common(lst):
	data = Counter(lst)
	return data.most_common(1)[0][0]

class KNN():
	def fit(self, X_train, Y_train):
		self.X_train = X_train
		self.Y_train = y_train
		
	def predict(self, X_test, k):
		predicts = []
		len = len(X_test)
		
		for i in range(len):
			classify = self.nearest(i, k)
			predicts.append(classify)
		return predicts	
	
	def choice(self, distsarr, k):
		labels = [x[1] for x in distsarr]
		topklabels = labels[:k]

		return Most_Common(topklabels)
	
	
	def nearest(self, data, k):
		distarray = []
		for i in range(len):
			distarray.append([edist(self.X_train[i], data), self.Y_train[i]])
		
		sorteddists = sorted(distarray, key=lambda x: x[0])
	
		return choice(self, sorteddists, k)
				
print("Love, -Robert")

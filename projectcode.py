#Declaring file and importing data
link = 'Fertilizer_prediction.csv'
import pandas as pd
data0 = pd.read_csv(link, sep=',', engine='python')
data = pd.DataFrame(data0)
sfdata = data.values
print('DATA HEAD',data.head())

#Initializing X and Y
X = data.iloc[:,:8]
Y = data.iloc[:,-1]

#Inserting model and splitting dataset
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
 
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y,test_size = 0.2,random_state = 1)

#Making fertilizer dictionary
ferdic = {1:'DAP', 2:'14-35-14', 3:'17-17-17', 4:'10-26-26', 5:'28-28', 6:'20-20', 7:'Urea'}
 import pickle
 
pkl_filename = 'pickle_model.pkl'
# Load from file
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)
    
# Calculate the accuracy score and predict target values
score = pickle_model.score(Xtest  , Ytest)
print("Test score: {0:.2f} %".format(100 * score))
Ypredict = pickle_model.predict(X)

#Manual checking
x2 = [[27,53,39,5,4,38,0,0]]
print(int(pickle_model.predict(x2)))

res = int(pickle_model.predict(x2))
print('\nFertilizer Required :', ferdic[res])
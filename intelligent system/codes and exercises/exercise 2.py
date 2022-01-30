''' MOHAMED MOUBARAK MOHAMED MISBAHOU MKOUBOI (1820705) '''
#import sklearn
import sklearn

# import decision_tree classifier from scikit
from sklearn import tree

# Convert Features in Int, 1 = 2 seats, 0 = 4 or 5 seats
features = [[150, 1], [250, 1], [660, 0], [1300, 0]]

# Convert Labels into Int, 1 = Motorbike, 0 = Motorcycle
labels = [1, 1, 0, 0]

# Create the Classifier - This is now an empty box of rules
classifier = tree.DecisionTreeClassifier()

# We need an Algorithm to train it - scikit comes with fit
classifier = classifier.fit(features, labels)

#predict a fruit
classifier.predict([[8,0]])

def whatmoto(feat1, feat2):
    motoname = ""
    moto = classifier.predict([[feat1,feat2]])
    if moto == 1:
        motoname = "Motorbike"
    else:
        motoname = "Motorcar"
    return motoname

#predict a moto
print(classifier.predict([[8,1]]) , whatmoto(157, 1))

print(classifier.predict([[8,0]]) , whatmoto(1000, 0))
# Load libraries
import pandas

# from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

from sklearn import model_selection
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB      # Accuracy: 0.740240 (+/- 0.005949)
from sklearn.naive_bayes import BernoulliNB     # Accuracy: 0.811730 (+/- 0.004672)
from sklearn.naive_bayes import ComplementNB    # Accuracy: 0.700330 (+/- 0.014145)
from sklearn.naive_bayes import CategoricalNB   # UNKNOWN (NOT RECOMMENED)

import joblib



# import dataset
dataset = pandas.read_csv("ipdos_cleaned_ipdos.csv")
print("(num_of_rows, num_of_columns) = " + str(dataset.shape) + '\n')
# print(dataset.shape)

# # head
# print(dataset.head(20))

# descriptions
# print(dataset.describe())

# # class distribution
# print(dataset.groupby('label').size())

# split dataset
array = dataset.values
# print("rows of metadata: \n" + str(array))
X = array[:,0:26]
Y = array[:,26]
test_size = 0.3
random_state = 42
# Split dataset into training set and test set
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=test_size, random_state=random_state)
X_train_set, X_test, Y_train_set, Y_test = model_selection.train_test_split(X_train, Y_train, test_size=test_size, random_state=random_state)

# # Test options and evaluation metric
scoring = 'accuracy'

# Evaluating algorithm model

models = []
models.append(('LR', LogisticRegression(max_iter=1000)))
models.append(('NB', BernoulliNB()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))



# evaluate each model in turn
results = []
names = []
for name, model in models:
        kfold = model_selection.KFold(n_splits=5, shuffle=True, random_state=random_state)
        cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        message = "%s Accuracy: %f (+/- %f)" % (name, cv_results.mean(), cv_results.std())
        print(message)

# # #Compare Algorithms
# fig = plt.figure()
# fig.suptitle('Algorithm Comparison')
# ax = fig.add_subplot(111)
# plt.boxplot(results)
# ax.set_xticklabels(names)
# plt.show()


################ SAVE FILE ################
# ### Make predictions on validation dataset
cart = DecisionTreeClassifier()         # Create Decision Tree classifer object
cart.fit(X_train_set, Y_train_set)      # Train Decision Tree Classifer

# #saving the model using joblib 
# filename = 'finalized_DT_model.sav'
# joblib.dump(cart, filename)
# # load the model from disk
# loaded_model = joblib.load(filename)
# result = loaded_model.score(X_test, Y_test)
# print ("\nCART results on 'validation_size%' test set: " + str(result))

#Predict the response for test dataset
predictions_rfc = cart.predict(X_test)
print("\nCART accuracy test: " + str(accuracy_score(Y_test, predictions_rfc)))
# print(accuracy_score(Y_test, predictions_rfc))
print(str(confusion_matrix(Y_test, predictions_rfc)) + "\n")
print(classification_report(Y_test, predictions_rfc))


# Make predictions on test dataset
# print("\nCART results on final 30% validation \n")
# print("\nCART results on final test_size% validation \n")

##########################################
# newcart = DecisionTreeClassifier()
# newcart.fit(X_train_set, Y_train_set)
# newpredictions_rfc = newcart.predict(X_validation)
# print("\nCART accuracy validation based on 'test_size%': " + str(accuracy_score(Y_validation, newpredictions_rfc)))
# # print(accuracy_score(Y_validation, newpredictions_rfc))
# print(str(confusion_matrix(Y_validation, newpredictions_rfc)) + "\n")
# print(classification_report(Y_validation, newpredictions_rfc))
# df = dataset.reset_index(drop = False)

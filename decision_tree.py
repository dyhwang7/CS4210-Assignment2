# -------------------------------------------------------------------------
# AUTHOR: Daeyoung Hwang
# FILENAME: decision_tree.py
# SPECIFICATION: training using 3 csv training sets and then testing on the test csv to find best model
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    # transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here

    age = {'Young': 1, 'Prepresbyopic': 2, 'Presbyopic': 3}
    spectacle = {'Myope': 1, 'Hypermetrope': 2}
    astigmatism = {'Yes': 1, 'No': 2}
    tear = {'Normal': 1, 'Reduced': 2}
    lenses_ground_truth = {'Yes': 1, 'No': 2}

    for row in dbTraining:
        X.append([age[row[0]], spectacle[row[1]], astigmatism[row[2]], tear[row[3]]])

    # X =

    # transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here
    # Y =

    for row in dbTraining:
        Y.append(lenses_ground_truth[row[4]])

    lowest_accuracy = 1
    # loop your training and test tasks 10 times here
    for i in range(10):

        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        dbTest = []

        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for j, row in enumerate(reader):
                if j > 0:  # skipping the header
                    dbTest.append(row)

        TP = TN = FP = FN = 0

        for data in dbTest:
            # transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
            # class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            # --> add your Python code here
            class_predicted = clf.predict([[age[data[0]], spectacle[data[1]], astigmatism[data[2]], tear[data[3]]]])[0]
            # print(class_predicted)
            # print(data[4])

            # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            # --> add your Python code here
            if class_predicted == lenses_ground_truth[data[4]]:
                if class_predicted == 1:
                    TP += 1
                else:
                    TN += 1
            else:
                if class_predicted == 1:
                    FP += 1
                else:
                    FN += 1

            # find the lowest accuracy of this model during the 10 runs (training and test set)
            # --> add your Python code here

        accuracy = (TP + TN) / (TP + TN + FP + FN)
        if accuracy < lowest_accuracy:
            lowest_accuracy = accuracy

# print the lowest accuracy of this model during the 10 runs (training and test set) and save it.
# your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
# --> add your Python code here

    print('lowest accuracy for set {} is {}'.format(ds, lowest_accuracy))
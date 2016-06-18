#

# TODO: Import the three supervised learning models from sklearn
from sklearn.svm import SVC
from sklearn import tree
from sklearn import linear_model

# TODO: Initialize the three models
clf_A = linear_model.LinearRegression()
clf_B = tree.DecisionTreeClassifier()
clf_C = SVC()

def dataSplitter(trainPoints, X_all, y_all):
    # TODO: Set the number of training points
    num_train = trainPoints

    # Set the number of testing points
    num_test = X_all.shape[0] - num_train
    testPercentage= float(format(num_test/(num_train+num_test), '.2f'))

    # TODO: Shuffle and split the dataset into the number of training and testing points above
    X_train = []
    y_train=[]
    X_test=[]
    y_test=[]
    rs = cross_validation.ShuffleSplit(n_students, n_iter=1,test_size=testPercentage, random_state=0)
    for train, test in rs:
        for val in train:
            X_train.append(X_all.loc[val])
            y_train.append(y_all.loc[val])

        for val in test:
            X_test.append(X_all.loc[val])
            y_test.append(y_all.loc[val])
    # Return the training and testing data subsets
    X_train = array(X_train)
    y_train = array(y_train)
    X_test = array(X_test)
    y_test = array(y_test)
    return X_train, X_test, y_train, y_test
    
# TODO: Set up the training set sizes
X_train_100,X_test_100,y_train_100,y_test_100 = dataSplitter(100,X_all,y_all)


X_train_200,X_test_200,y_train_200,y_test_200 = dataSplitter(200,X_all,y_all)


X_train_300,X_test_300,y_train_300,y_test_300 = dataSplitter(300,X_all,y_all)


# TODO: Execute the 'train_predict' function for each classifier and each training set size
# train_predict(clf, X_train, y_train, X_test, y_test)

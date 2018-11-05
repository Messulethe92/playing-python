from sklearn import tree

# The features of fruit. [weight, rough(1) or smooth(0)]
features = [[140, 1],[130, 1],[150, 0],[170, 0]]
# The labels of the fruit in the feature list. Orange(1) or Apple(0) 
labels = [1, 1, 0, 0]

# The classifier that we're using. A simple decision tree.
clf = tree.DecisionTreeClassifier()
iterations = 3

while True:
    iterations += 1
    # (Re)Training the classifier with the fruit and their labels.
    clf = clf.fit(features, labels)


    iWeight = input('What does the fruit weigh? ')

    while not iWeight.isnumeric() or int(iWeight) <= 0:
        iWeight = input('What does the fruit weigh [only whole numbers bigger than 0]? ')
        
    isRough = input('Is the fruit Rough (1) or Smooth(0)? ')

    while not isRough.isnumeric() or (int(isRough) != 0 and int(isRough) != 1):
        isRough = input('Is the fruit Rough (1) or Smooth(0) [please input a 0 or 1]? ')

    # Predicting a new fruit
    prediction = clf.predict([[iWeight, isRough]])

    if int(prediction) == 1:
        print('         Fruit is an Orange! ' + str(prediction))
    else:
        print('         Fruit is an Apple! ' + str(prediction))

    predictionCorrect = input('Is this a correct (1) or incorrect(0) guess? ')
    while not predictionCorrect.isnumeric() or (int(predictionCorrect) != 0 and int(predictionCorrect) != 1):
        predictionCorrect = input('Is this a correct (1) or incorrect(0) guess [please input a 0 or 1]? ')

    features.append([iWeight, isRough])
    # If the prediction was correct, then predicted value, else the opposite of the predicted value
    if int(predictionCorrect) == 1: # Right prediction
        labels.append(int(prediction))
    else: # Wrong prediction
        labels.append(0 if int(prediction) == 1 else 1)

    print(features[iterations])
    print(labels[iterations])



# First neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# Load the dataset
dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=',')

# Split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

# Define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)

# Evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

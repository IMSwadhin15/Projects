from keras.models import load_model
import numpy as np

# Load X_test and y_test
X_test = np.load('X_test.npy')
y_test = np.load('y_test.npy')

# Verify the shapes
# print(X_test.shape)
# print(y_test.shape)


# Load the model from the H5 file
model1 = load_model('model1.h5')
# model2 = load_model('model2.h5')

# Verify the model structure by printing the summary
model1.summary()
# model2.summary()


# Evaluate model1
test_loss1, test_accuracy1 = model1.evaluate(X_test, y_test)
print(f"Test Accuracy for model1 (ReLU): {test_accuracy1:.4f}")

# # # Evaluate model2
# test_loss2, test_accuracy2 = model2.evaluate(X_test, y_test)
# print(f"Test Accuracy for model2 (Tanh): {test_accuracy2:.4f}")

# # Evaluate model3
# test_loss3, test_accuracy3 = model3.evaluate(X_test, y_test)
# print(f"Test Accuracy for model3 (Sigmoid): {test_accuracy3:.4f}")
from function import *
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import TensorBoard
import pandas as pd

label_map = {label:num for num, label in enumerate(actions)}
# print(label_map)
sequences, labels = [], []
for action in actions:
    for sequence in range(no_sequences):
        window = []
        for frame_num in range(sequence_length):
            try:
                res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)),allow_pickle=True)
                if res.shape != (63,):
                    print(f"Shape of {action}/{sequence}/{frame_num}: {res.shape}")
                    continue
                window.append(res)
            except Exception as e:
                print(f"Error loading file: 'Image/{action}/{sequence}/{frame_num}.npy' - {e}")
        if len(window) != sequence_length:
            print(f"Incomplete window for {action}/{sequence}: {len(window)} frames")
            continue
        sequences.append(window)
        labels.append(label_map[action])

X = np.array(sequences)
y = to_categorical(labels).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)
import numpy as np

# Save X_test and y_test
np.save('X_test.npy', X_test)
np.save('y_test.npy', y_test)


log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)

# # RELU
# model1 = Sequential()
# model1.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,63)))
# model1.add(LSTM(128, return_sequences=True, activation='relu'))
# model1.add(LSTM(64, return_sequences=False, activation='relu'))
# model1.add(Dense(64, activation='relu'))
# model1.add(Dense(32, activation='relu'))
# model1.add(Dense(actions.shape[0], activation='softmax'))
# res = [.7, 0.2, 0.1]

# model1.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
# history = model1.fit(X_train, y_train, epochs=200, validation_data=(X_test, y_test),callbacks=[tb_callback])
# import pandas as pd

# # Extract data from history
# history_dict = history.history
# epochs = list(range(1, len(history_dict['categorical_accuracy']) + 1))

# # Create a DataFrame
# data = {
#     'Epoch': epochs,
#     'Train Accuracy': history_dict.get('categorical_accuracy', []),
#     'Validation Accuracy': history_dict.get('val_categorical_accuracy', [])
    
# }
# df = pd.DataFrame(data)

# # Save to CSV
# df.to_csv('epoch_data1.csv',index=False)
# model1.summary()

# model1_json = model1.to_json()
# with open("model1.json", "w") as json_file:
#     json_file.write(model1_json)
# model1.save('model1.h5')

#---------------------------------------------------------------------------

# # TANH
# model2 = Sequential()
# model2.add(LSTM(64, return_sequences=True, activation='tanh', input_shape=(30,63)))
# model2.add(LSTM(128, return_sequences=True, activation='tanh'))
# model2.add(LSTM(64, return_sequences=False, activation='tanh'))
# model2.add(Dense(64, activation='tanh'))
# model2.add(Dense(32, activation='tanh'))
# model2.add(Dense(actions.shape[0], activation='softmax'))
# res = [.7, 0.2, 0.1]

# model2.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
# history = model2.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test), callbacks=[tb_callback])
# import pandas as pd

# # Extract data from history
# history_dict = history.history
# epochs = list(range(1, len(history_dict['categorical_accuracy']) + 1))

# # Create a DataFrame
# data = {
#     'Epoch': epochs,
#     'Train Accuracy': history_dict.get('categorical_accuracy', []),
#     'Validation Accuracy': history_dict.get('val_categorical_accuracy', [])
    
# }
# df = pd.DataFrame(data)

# # Save to CSV
# df.to_csv('epoch_data2.csv',index=False)
# model2.summary()

# model2_json = model2.to_json()
# with open("model2.json", "w") as json_file:
#     json_file.write(model2_json)
# model2.save('model2.h5')

#---------------------------------------------------------------------------

# # SIGMOID
# model3 = Sequential()
# model3.add(LSTM(64, return_sequences=True, activation='sigmoid', input_shape=(30,63)))
# model3.add(LSTM(128, return_sequences=True, activation='sigmoid'))
# model3.add(LSTM(64, return_sequences=False, activation='sigmoid'))
# model3.add(Dense(64, activation='sigmoid'))
# model3.add(Dense(32, activation='sigmoid'))
# model3.add(Dense(actions.shape[0], activation='softmax'))
# res = [.7, 0.2, 0.1]

# model3.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
# history = model3.fit(X_train, y_train, epochs=200,validation_data=(X_test, y_test), callbacks=[tb_callback])
# import pandas as pd

# # Extract data from history
# history_dict = history.history
# epochs = list(range(1, len(history_dict['categorical_accuracy']) + 1))

# # Create a DataFrame
# data = {
#     'Epoch': epochs,
#     'Train Accuracy': history_dict.get('categorical_accuracy', []),
    
#     'Validation Accuracy': history_dict.get('val_categorical_accuracy', [])
# }
# df = pd.DataFrame(data)

# # Save to CSV
# df.to_csv('epoch_data3.csv',index=False)
# model3.summary()

# model3_json = model3.to_json()
# with open("model3.json", "w") as json_file:
#     json_file.write(model3_json)
# model3.save('model3.h5')

#--------------------------------------------------------------------------

# CNN

from skimage.transform import resize

# Reshape each sample to a size compatible with (50, 50, 3)
num_samples_train = X_train.shape[0]
X_train_resized = np.zeros((num_samples_train, 50, 50, 3))

for i in range(num_samples_train):
    # Reshape to closest square shape that preserves the total number of elements (e.g., 45x42)
    reshaped_sample = np.reshape(X_train[i], (45, 42))
    
    # Resize to (50, 50) and replicate across 3 color channels
    reshaped_sample = resize(reshaped_sample, (50, 50), mode='constant', anti_aliasing=True)
    reshaped_sample = np.stack([reshaped_sample] * 3, axis=-1)  # Add 3 channels
    
    X_train_resized[i] = reshaped_sample

# Repeat for X_test
num_samples_test = X_test.shape[0]
X_test_resized = np.zeros((num_samples_test, 50, 50, 3))

for i in range(num_samples_test):
    reshaped_sample = np.reshape(X_test[i], (45, 42))
    reshaped_sample = resize(reshaped_sample, (50, 50), mode='constant', anti_aliasing=True)
    reshaped_sample = np.stack([reshaped_sample] * 3, axis=-1)
    
    X_test_resized[i] = reshaped_sample

# Normalize pixel values (optional)
X_train_resized /= 255.0
X_test_resized /= 255.0

#----------------------------------------------------------------------
# CNN 1

# from keras.layers import Conv2D, MaxPooling2D, Flatten

# model4 = Sequential()
# model4.add(Conv2D(32, (3, 3), padding="same", input_shape=(50, 50, 3), activation="relu"))
# model4.add(MaxPooling2D(pool_size=(3, 3)))
# model4.add(Conv2D(90, (3, 3), padding="same", activation="relu"))
# model4.add(MaxPooling2D(pool_size=(2, 2)))
# model4.add(Conv2D(90, (3, 3), padding="same", activation="relu"))
# model4.add(MaxPooling2D(pool_size=(2, 2)))
# model4.add(Flatten())
# model4.add(Dense(60, activation="relu"))
# model4.add(Dense(40, activation="relu"))
# model4.add(Dense(actions.shape[0], activation="softmax"))

# # Compile the CNN model
# model4.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

# # Train the CNN model
# history = model4.fit(X_train_resized, y_train, epochs=100, validation_data=(X_test_resized, y_test), callbacks=[tb_callback])

# # Extract data from history and save it to CSV
# history_dict = history.history
# epochs = list(range(1, len(history_dict['categorical_accuracy']) + 1))

# data = {
#     'Epoch': epochs,
#     'Train Accuracy': history_dict.get('categorical_accuracy', []),
#     'Validation Accuracy': history_dict.get('val_categorical_accuracy', [])
# }

# df = pd.DataFrame(data)

# # Save to CSV
# df.to_csv('epoch_data4.csv', index=False)
# model4.summary()

# # Save model architecture and weights
# model4_json = model4.to_json()
# with open("model4.json", "w") as json_file:
#     json_file.write(model4_json)
# model4.save('model4.h5')

#------------------------------------------------------------------------

# VARIATION OF CNN
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten

model5 = Sequential()

# First convolutional layer with increased filter size and kernel size
model5.add(Conv2D(64, (5, 5), padding="same", input_shape=(50, 50, 3), activation="relu"))
model5.add(MaxPooling2D(pool_size=(3, 3)))
model5.add(Dropout(0.2))  # Adding dropout to reduce overfitting

# Second convolutional layer with more filters
model5.add(Conv2D(128, (3, 3), padding="same", activation="relu"))
model5.add(MaxPooling2D(pool_size=(2, 2)))
model5.add(Dropout(0.3))

# Third convolutional layer with a different kernel size
model5.add(Conv2D(128, (3, 3), padding="same", activation="relu"))
model5.add(MaxPooling2D(pool_size=(2, 2)))
model5.add(Dropout(0.4))

# Fourth convolutional layer to increase depth
model5.add(Conv2D(256, (3, 3), padding="same", activation="relu"))
model5.add(MaxPooling2D(pool_size=(2, 2)))
model5.add(Dropout(0.5))

# Flatten and dense layers for classification
model5.add(Flatten())
model5.add(Dense(120, activation="relu"))  # Increased number of units
model5.add(Dropout(0.5))  # Dropout to prevent overfitting
model5.add(Dense(60, activation="relu"))
model5.add(Dense(40, activation="relu"))
model5.add(Dense(actions.shape[0], activation="softmax"))

# Compile the CNN model
model5.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

# Train the CNN model
history = model5.fit(X_train_resized, y_train, epochs=100, validation_data=(X_test_resized, y_test), callbacks=[tb_callback])

# Extract data from history and save it to CSV
history_dict = history.history
epochs = list(range(1, len(history_dict['categorical_accuracy']) + 1))

data = {
    'Epoch': epochs,
    'Train Accuracy': history_dict.get('categorical_accuracy', []),
    'Validation Accuracy': history_dict.get('val_categorical_accuracy', [])
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('epoch_data5.csv', index=False)
model5.summary()

# Save model architecture and weights
model5_json = model5.to_json()
with open("model5.json", "w") as json_file:
    json_file.write(model5_json)
model5.save('model5.h5')
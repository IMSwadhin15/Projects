from skimage.transform import resize

# # Sample input (assuming X_train is in shape (num_samples, 30, 63))
# num_samples = X_train.shape[0]

# # Initialize an empty array for storing the transformed data
# X_train_resized = np.zeros((num_samples, 50, 50, 3))

# # Transform each sample
# for i in range(num_samples):
#     # Flatten or reshape (30, 63) into a 2D format, e.g., (50, 50)
#     # You may need a custom mapping depending on what (30, 63) represents
#     reshaped_sample = np.reshape(X_train[i], (50, 50))  # Example reshape, adapt as needed
    
#     # Expand dimensions to include 3 color channels
#     reshaped_sample = np.stack([reshaped_sample] * 3, axis=-1)
    
#     # Optionally resize to ensure (50, 50, 3) shape
#     reshaped_sample = resize(reshaped_sample, (50, 50, 3), mode='constant', anti_aliasing=True)
    
#     # Store in the array
#     X_train_resized[i] = reshaped_sample

# # Repeat for X_test
# num_samples_test = X_test.shape[0]
# X_test_resized = np.zeros((num_samples_test, 50, 50, 3))
# for i in range(num_samples_test):
#     reshaped_sample = np.reshape(X_test[i], (50, 50))
#     reshaped_sample = np.stack([reshaped_sample] * 3, axis=-1)
#     reshaped_sample = resize(reshaped_sample, (50, 50, 3), mode='constant', anti_aliasing=True)
#     X_test_resized[i] = reshaped_sample

# # Now X_train_resized and X_test_resized are ready for CNN input

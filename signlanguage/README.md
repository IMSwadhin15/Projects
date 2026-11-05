# Odia Sign Language Recognition

This project builds a hand-sign recognition system for selected Odia sign classes using MediaPipe hand landmarks and a deep learning classifier. The workflow is designed to collect hand movement sequences, transform them into keypoint representations, train a classifier, and then recognize signs live from a webcam.

## 1. Brief project workflow

1. Capture frames from the webcam using OpenCV.
2. Crop the hand region and detect hand landmarks with MediaPipe Hands.
3. Flatten each detected hand into a 63-dimensional feature vector (21 landmarks × 3 coordinates: x, y, z).
4. Form a sequence of 30 frames for each sign sample.
5. Save the sequence under the corresponding class folder in the dataset folder.
6. Train a deep learning model on the extracted keypoint sequences.
7. Use the trained model in the live application to predict the ongoing sign.

The important scripts are:

- `collectdata.py` — captures and saves sign images/sequences.
- `data.py` — creates dataset folders and extracts landmark keypoints.
- `trainmodel.py` — builds and trains the model.
- `app.py` — loads the trained model and performs real-time prediction from webcam input.

## 2. Models used

The project explores several deep learning setups, but the final training pipeline in `trainmodel.py` uses a CNN-based classifier built on the reshaped hand-keypoint sequences.

### Landmark extractor
- MediaPipe Hands
  - Detects 21 hand landmarks per frame
  - Used for robust hand tracking and keypoint extraction

### Final classifier (implemented in the project)
A CNN architecture with the following structure:

- Conv2D(64, 5×5, activation="relu")
- MaxPooling2D(3×3)
- Conv2D(128, 3×3, activation="relu")
- MaxPooling2D(2×2)
- Conv2D(128, 3×3, activation="relu")
- MaxPooling2D(2×2)
- Conv2D(256, 3×3, activation="relu")
- MaxPooling2D(2×2)
- Flatten
- Dense(120, activation="relu")
- Dense(60, activation="relu")
- Dense(40, activation="relu")
- Dense(9, activation="softmax")

The training script also includes LSTM experiments with ReLU, tanh, and sigmoid activations, but the active final configuration is the CNN model.

## 3. Dataset details

The project uses a hand-keypoint dataset generated from video/frame sequences. Each sample is represented as a sequence of 30 frames, and each frame is encoded as a 63-dimensional keypoint vector.

### Dataset configuration
- Number of classes: 9
- Sequences per class: 30
- Frames per sequence: 30
- Keypoints per frame: 63
- Total action sequences: 270

This is derived from:

- `actions = np.array(['a', 'aa', 'i', 'u', 'ru', 'e', 'ai', 'o', 'ou'])`
- `no_sequences = 30`
- `sequence_length = 30`

So the project is designed around 9 sign categories, each with 30 sequences.

## 4. Class distribution

The dataset distribution is balanced across the configured classes.

| Class | Sequences |
| --- | ---: |
| a | 30 |
| aa | 30 |
| i | 30 |
| u | 30 |
| ru | 30 |
| e | 30 |
| ai | 30 |
| o | 30 |
| ou | 30 |

Total samples: 270 sequences

Note: The dataset is balanced by design, and each class contributes equally to the training data.

## 5. Train / test / validation split

The training script uses:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)
```

This means:

- Train split: approximately 95%
- Test split: approximately 5%
- Validation split: not explicitly created as a separate dataset in the script

Because `validation_data=(X_test, y_test)` is passed to `model.fit(...)`, the test set is also used as the validation set during training. Therefore, the current repository uses a 95:5 train:test configuration, with no dedicated validation subset.

Approximate counts based on 270 sequences:

- Training samples: about 256–257
- Test/validation samples: about 13–14

## 6. Performance metrics

The project trains with the following metrics:

- Loss: `categorical_crossentropy`
- Accuracy: `categorical_accuracy`

The code logs training and validation metrics to TensorBoard using:

```python
log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)
```

Logs are stored under:

- `signlanguage/Logs/train`
- `signlanguage/Logs/validation`

The repository contains the TensorBoard event files for training/validation logging, but the final numerical accuracy/loss values are not stored as a committed CSV/summary file in this project snapshot. In other words, the project tracks the performance metrics during training, but the exact final metric values are expected to be read from TensorBoard logs generated at runtime.

## 7. How the system works in practice

The real-time application (`app.py`) does the following:

1. Reads frames from the webcam.
2. Crops the region of interest.
3. Extracts hand keypoints with MediaPipe.
4. Keeps the last 30 frames in a sequence.
5. Predicts the label with the trained model.
6. Displays the predicted class on the camera feed.

This makes the project suitable for live sign recognition prototype use.

## 8. Notes

- The raw dataset is not included in this repository snapshot; it is created during data collection by the script.
- The code is structured as a proof-of-concept sign recognition pipeline and can be extended with a larger dataset and better architecture tuning.
- For more reliable benchmarking, a dedicated validation set and a fixed train/test split should be added to the pipeline.

## 9. Potential next improvements

- Increase the number of classes and sample count
- Use a proper validation split separate from the test set
- Save a final trained model file (`.h5`) and confusion matrix
- Report final accuracy, precision, recall, F1-score, and per-class metrics
- Use a larger and more diverse dataset for real-world robustness


## Using Trnsfer learning to classify images of cats and dogs using a pre-trained model ResNet50 from Keras.
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, BatchNormalization, Dropout, GlobalAveragePooling2D
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input


IMG_SIZE = (224, 224)


# Data Augmentation

data_augmentation = keras.Sequential([
    keras.layers.RandomFlip("horizontal"),
    keras.layers.RandomRotation(0.1),
    keras.layers.RandomZoom(0.1),
    keras.layers.RandomTranslation(0.1, 0.1),
    keras.layers.RandomContrast(0.1)
])


# Pretrained ResNet50

backbone = ResNet50(
    include_top=False,
    weights='imagenet',
    input_shape=(224, 224, 3)
)


# Freeze ResNet50

backbone.trainable = False


# Create Model

model = Sequential()

model.add(data_augmentation)

model.add(keras.layers.Lambda(
    lambda x: preprocess_input(x)
))

model.add(backbone)

model.add(GlobalAveragePooling2D())

model.add(BatchNormalization())

model.add(Dense(units=256, activation='relu'))

model.add(Dropout(0.4))

model.add(Dense(units=1, activation='sigmoid'))

model.build((None, 224, 224, 3)) ## None is used for batch size, 224, 224 is the image size and 3 is the number of channels (RGB)

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.0001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()
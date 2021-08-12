import tensorflow as tf

base_model = tf.keras.applications.MobileNetV2(input_shape=(224,224,3), include_top=False, weights='imagenet') #Load MobileNetV2 with imagenet weights
base_model.trainable = False #Freeze convolutional base of network
preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()

inputs = tf.keras.Input(shape=(224, 224, 3))
x = preprocess_input(inputs) #used to scale the input images to the range [-1, 1] which is needed for MobileNetV2
x = base_model(x, training=False)
x = global_average_layer(x)
outputs = tf.linalg.normalize(x, ord = 'euclidean', axis = 1)
model = tf.keras.Model(inputs, outputs)

print(model.summary())

print('saving model')
tf.keras.models.save_model(model, 'model/my_second_tx_model.h5')
print('model_saved')
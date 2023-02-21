
# load and evaluate a saved model
from numpy import loadtxt
from tensorflow.keras.models import load_model

# load model
model = load_model("C:\\Users\\yasha\\Downloads\\vgg16_isl_128.h5")

# summarize model.
model.summary()

predictions = model.predict("D:\\Projects\\ISL using yolov8\\training_data\\archive\\Indian\\2\\2.jpg")

print (predictions)
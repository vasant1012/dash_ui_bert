DEVICE = "cpu"
MAX_LEN = 70
TRAIN_BATCH_SIZE = 16
VALID_BATCH_SIZE = 8
EPOCHS = 10
BASE_MODEL_PATH = r'./base model'
PATH = r'./trained model/'
MODEL_PATH = PATH + "model.bin" # path to bert model
META_PATH = PATH + "meta.bin"
TRAINING_FILE = "./data/input_data.csv" # path to training data
learning_rate = 5.654550891094924e-05
drop_out1 = 0.12520394654248432
drop_out2 = 0.5235516163179119
drop_out3 = 0.013428688116647505

print("Config Import Successfull")

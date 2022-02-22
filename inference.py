import numpy as np
import requests

from tensorflow import keras

def get_mfccs(filename):
    # Load the file to send
    files = {'audio': open(filename, 'rb')}
    # Send the HTTP request and get the reply
    reply = requests.post("https://librosa-utils.herokuapp.com/mfcc_batch", files=files)
    # Extract the text from the reply and decode the JSON into a list
    pitch_track = reply.json()
    print(np.shape(pitch_track['mfccs']))
    return np.array(pitch_track['mfccs'])

def inference(filename, model_path='gtzan10_lstm_0.7179_l_1.12.h5'):
    model = keras.models.load_model(model_path)
    mapping = ['blues',
                'classical',
                'country',
                'disco',
                'hiphop',
                'jazz',
                'metal',
                'pop',
                'reggae',
                'rock']
    mfcc = get_mfccs(filename)
    pred = model.predict(mfcc)
    genre = [mapping[i] for i in np.argmax(pred, axis=1)]

    counter_ = {}
    for i in genre:
        counter_[genre.count(i)] = i
    m = max(counter_)
    return f"Genre: {counter_[m]}, Confidence: {max(counter_)/pred.shape[0]}"

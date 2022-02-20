import math, librosa
import numpy as np

from tensorflow import keras

SAMPLE_RATE = 22050
def extract_mfcc_batch(file_path, n_mfcc=13, n_fft=1024, hop_length=512, length_segment=10):
    """
    Extract and return an mfcc batch
    MFCC - Mel Frequency Cepstrum Coefficients
    """
    mfcc_batch = []
    num_samples_per_segment = 220500 #length_segment * SAMPLE_RATE
    expected_num_mfcc_vectors_per_segment = math.ceil(num_samples_per_segment / hop_length)
   
    signal, sr = librosa.load(file_path, sr=SAMPLE_RATE)

    duration = librosa.get_duration(y=signal, sr=sr) #30 seconds
    num_segments = int(duration/length_segment) #3
    # process segments, extracting mfccs and storing data
    for s in range(num_segments+1):
        start_sample = num_samples_per_segment * s
        finish_sample = start_sample + num_samples_per_segment
        try:
            mfcc = librosa.feature.mfcc(signal[start_sample:finish_sample],
                                    sr=SAMPLE_RATE,
                                    n_fft=n_fft,
                                    n_mfcc=n_mfcc,
                                    hop_length=hop_length
                                    )
            #(13, 431)
            mfcc = mfcc.T # A transpose
            # store mfcc for segment if it has the expected length
            if len(mfcc) == 431:
                mfcc_batch.append(mfcc.tolist())
        except:
            continue
    return mfcc_batch

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
    mfcc = extract_mfcc_batch(filename)
    pred = model.predict(mfcc)
    genre = [mapping[i] for i in np.argmax(pred, axis=1)]

    counter_ = {}
    for i in genre:
        counter_[genre.count(i)] = i
    m = max(counter_)
    return f"Genre: {counter_[m]}, Confidence: {max(counter_)/pred.shape[0]}"

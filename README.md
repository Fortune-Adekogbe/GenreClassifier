---
title: GenreClassifier
emoji: 🎶
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
license: afl-3.0
---

This Genre Classifier is built using the [GTZAN dataset](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification?select=Data) which consists of 10 genres. These genres are:
- Blues
- Classical
- Country
- Disco
- Hiphop
- Jazz
- Metal
- Pop
- Reggae
- Rock

Data for each genre includes 100 30-seconds long tracks which were then used to build a LSTM model 
using Keras (tensorflow backend).

With more data, this model could have a more robust performance but for now, 
it does well on GTZAN-like data.

To use this model, navigate to [the app](https://huggingface.co/spaces/Enutrof/GenreClassifier) on huggingface spaces and upload a track.

To view the API documentation and use it, click [this link](https://hf.space/gradioiframe/Enutrof/GenreClassifier/api).

Check out the configuration reference at https://huggingface.co/docs/hub/spaces#reference

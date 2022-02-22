import subprocess, platform

if platform.system() == 'Linux':
    subprocess.call(['apt-get install', 'libsndfile1'])
    subprocess.call(['apt-get install', 'ffmpeg'])

import gradio as gr
from inference import *

iface = gr.Interface(fn=inference, 
                    inputs=gr.inputs.Audio(source="upload", type="filepath"), 
                    outputs="text")
iface.launch(share=True)
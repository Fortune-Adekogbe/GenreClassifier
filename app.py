import subprocess, platform

if platform.system() == 'Linux':
    subprocess.run(['apt-get', 'install', 'libsndfile1'])
    subprocess.run(['apt-get', 'install', 'ffmpeg'])

import gradio as gr
from inference import *

iface = gr.Interface(fn=inference, 
                    inputs=gr.inputs.Audio(source="upload", type="filepath"), 
                    outputs="text")
iface.launch(share=True)
import subprocess, platform

if platform.system() == 'Linux':
    subprocess.run(['sudo', 'apt-get', 'install', 'libsndfile1'], check=True)
    subprocess.run(['sudo', 'apt-get', 'install', 'ffmpeg'], check=True)

import gradio as gr
from inference import *

iface = gr.Interface(fn=inference, 
                    inputs=gr.inputs.Audio(source="upload", type="filepath"), 
                    outputs="text")
iface.launch(share=True)
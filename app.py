import subprocess, platform
import gradio as gr
from inference import *

if platform.system() == 'Linux':
    subprocess.call(['sudo', 'apt-get install', 'libsndfile1'])
    subprocess.call(['sudo', 'apt-get install', 'ffmpeg'])

iface = gr.Interface(fn=inference, 
                    inputs=gr.inputs.Audio(source="upload", type="filepath"), 
                    outputs="text")
iface.launch(share=True)
import gradio as gr
from inference import *

def greet(name):
    return "Hello " + name + "!"

iface = gr.Interface(fn=inference, 
                    inputs=gr.inputs.Audio(source="upload", type="filepath"), 
                    outputs="text")
iface.launch()
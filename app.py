import gradio as gr
from inference import *

def greet(name):
    return "Hello " + name + "!"

iface = gr.Interface(fn=inference, inputs="audio", outputs="text")
iface.launch()
import gradio as gr
from inference import *

iface = gr.Interface(fn=inference, 
                    inputs='audio', #gr.inputs.Audio(source="upload", type="filepath"), 
                    outputs="text")
iface.launch(share=True)
import gradio as gr
from utils import load_case
from courtroom import run_trial
import io
import sys

def simulate_case(case_no):
    case = load_case(case_no)
    if not case:
        return "❌ Case not found."

    # Capture print output from run_trial
    buffer = io.StringIO()
    sys.stdout = buffer
    run_trial(case)
    sys.stdout = sys.__stdout__

    return buffer.getvalue()

iface = gr.Interface(
    fn=simulate_case,
    inputs=gr.Textbox(label="Enter Case Number"),
    outputs=gr.Textbox(label="Simulation Result", lines=20),
    title="⚖️ AGENTS OF JUSTICE ⚖️",
    description="Enter a case number to simulate a courtroom trial."
)

if __name__ == "__main__":
    iface.launch(share=True)

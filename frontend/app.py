import gradio as gr
import requests
from dotenv import load_dotenv
import os

load_dotenv()
SERVICE_IP = os.getenv('SERVICE_IP')
STATUS_ENDPOINT = os.getenv('STATUS_ENDPOINT')
SUPPORTEDLANG_ENDPOINT = os.getenv('SUPPORTEDLANG_ENDPOINT')
DETECT_ENDPOINT = os.getenv('DETECT_ENDPOINT')
TRANSLATE_ENDPOINT = os.getenv('TRANSLATE_ENDPOINT')

def status_check():
    try:
        response = requests.get(SERVICE_IP + STATUS_ENDPOINT)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False


def get_online_status():
    if status_check():
        return "Online"
    else:
        return "Offline"

def detect_text(x):
    if status_check():
        if len(x) < 6:
            return { status_output: "Online", detect_text_output: "Try with a longer word/sentence."}
        try:
            payload = { "prompt": x }
            response = requests.post(SERVICE_IP + DETECT_ENDPOINT, json = payload)
            response.raise_for_status()
            result = response.json()
            return { status_output: "Online", detect_text_output: result['response'] + " (" + result['confidence'] + ")"}
        except requests.exceptions.RequestException:
            return { status_output: "Online", detect_text_output: "Error Detecting Language."}
    else:
        return { status_output: "Offline", detect_text_output: ""}

def copy_text(detectInput, detectOutput):
    if "%" in detectOutput: 
        return detectInput
    else:
        return ""

def generate_lang_list():
    if status_check():
        try:
            response = requests.get(SERVICE_IP + SUPPORTEDLANG_ENDPOINT)
            response.raise_for_status()
            result = response.json()
            return result['supported_lang']
        except requests.exceptions.RequestException:
            return []
    else:
        return []

def regnerate_dropdown():
    new_options = generate_lang_list()
    return gr.Dropdown(choices=new_options)

def translate_text(x, lang):
    if status_check():
        if len(x) < 6:
            return { status_output: "Online", translate_text_output: "Try with a longer word/sentence."}
        try:
            payload = { "prompt": x, "originalLang": lang }
            response = requests.post(SERVICE_IP + TRANSLATE_ENDPOINT, json = payload)
            response.raise_for_status()
            result = response.json()
            return { status_output: "Online", translate_text_output: result['response']}
        except requests.exceptions.RequestException:
            return { status_output: "Online", translate_text_output: "Error Translating Input."}
    else:
        return { status_output: "Offline", translate_text_output: ""}

status = get_online_status()
lang_dropdown_list = generate_lang_list()
with gr.Blocks() as demo:
    gr.Markdown("Translation Demo App")
    status_output = gr.Textbox(label="Service Status", value=status)
    status_button = gr.Button(value="Check Service Status")
    with gr.Tab("Detect"):
        detect_text_input = gr.Textbox(label="Input")
        gr.Examples(["Hello, how are you?", "Halo apa kabarmu?", "Hallo, wie geht es dir?", "Bonjour comment allez-vous?", "Ciao, come stai?", "こんにちは お元気ですか？", "早上好,你好吗？", "早安,你好嗎？"], detect_text_input)
        detect_text_output = gr.Textbox(label="Detected Language")
        detect_text_button = gr.Button("Detect Language")
    with gr.Tab("Translate"):
        translate_text_input = gr.Textbox(label="Input")
        translate_lang_dropdown = gr.Dropdown(choices=lang_dropdown_list, label="Original Language")
        regenerate_lang_list_button = gr.Button(value="Regenerate List")
        translate_text_output = gr.Textbox(label="English")
        translate_text_button = gr.Button("Translate To English")

    status_button.click(get_online_status, outputs=status_output)
    detect_text_button.click(detect_text, inputs=detect_text_input, outputs=[status_output, detect_text_output])
    regenerate_lang_list_button.click(regnerate_dropdown, outputs=translate_lang_dropdown)
    translate_text_button.click(translate_text, inputs=[translate_text_input,translate_lang_dropdown], outputs=[status_output, translate_text_output])
    detect_text_output.change(copy_text, inputs=[detect_text_input, detect_text_output], outputs=translate_text_input)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)

import whisper
import os

model = whisper.load_model("base")

def _process_file(file_path):
    result = model.transcribe(file_path)
    return result

def _get_text(transcribe_obj):
    return transcribe_obj.text

def transcribe(file_path):
    processed_file = _process_file(file_path)
    text = _get_text(processed_file)
    return text

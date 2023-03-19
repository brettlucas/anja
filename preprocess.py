import os

ACCEPTED_FILE_TYPES = ["m4A", "mp3", 'mp4', "mpeg", 
                        "mpga", "wav", "webm"]

WARNING_MB_LIMIT = 100

def check_if_audio_file_exists(file_path):
    return os.path.isfile(file_path)

def check_if_file_is_audio(file_path, 
                           file_types=ACCEPTED_FILE_TYPES):
    input_file_type = file_path.lower().split(".")[-1] 
    is_audio = input_file_type in file_types
    return is_audio

def get_file_size_MB(file_path):
    size_in_bytes = os.stat(file_path).st_size
    size_in_MB = size_in_bytes / 1_000_000
    return size_in_MB

def check_if_file_under_size_limit(file_path, 
                            upper_limit=WARNING_MB_LIMIT):
    size_in_MB = get_file_size_MB(file_path)
    if size_in_MB > upper_limit:
        return False
    return True

def preprocess_file(file_path): #TODO give option for follow-on
    does_file_exist = check_if_audio_file_exists(file_path)
    if not does_file_exist:
        print(f"No file found at {file_path}.")
        return False
    
    is_file_audio = check_if_file_is_audio(file_path)
    if not is_file_audio:
        file_types_string = ", ".join(ACCEPTED_FILE_TYPES)
        print(f"File at {file_path} is not an accepted audio file.") 
        print(f"Please use {file_types_string}.")
        return False  

    is_ok_size = check_if_file_under_size_limit(file_path)
    if not is_ok_size:
        mb = str(get_file_size_MB(file_path))
        print("File is {mb} MB and exceeds your maximum size limit.")
        return False
    
    return True

    

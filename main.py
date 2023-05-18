import random
import string
import os.path
from gtts import gTTS
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is active"}

@app.get('/text_to_voice/{text}')
def text_to_voice(text: str):

    characters = string.ascii_letters + string.digits + string.punctuation
    file_name = get_random_string(8) + '.mp3'

    audio = gTTS(text, lang="en")
    audio.save('result/' + file_name)
    return {
        'result': 'text is voiced',
        'download_url': 'http://127.0.0.1:8000/download_voice/'+file_name
    }
    # return {'result': 'text is no voiced'}

@app.get('/download_voice/{file_name}')
def download_voice(file_name: str):
    file_dir = 'result/' + file_name
    if(os.path.exists(file_dir)):
        return FileResponse(file_dir, filename='yourfile.mp3')

    return {'status': 'file not found'}





def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
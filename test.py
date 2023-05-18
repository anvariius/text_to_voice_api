import pyttsx3
from PyPDF2 import PdfFileReader
from fastapi import FastAPI
from fastapi.responses import FileResponse

# app = FastAPI()
#
# @app.get('/text_to_audio/{text}/male')
# def text_male_voice(text: str):
#     textToVoice(text, 'Yuri', w=True)
#     return FileResponse("result/test.mp3", filename='yourfile.mp3')
#
# @app.get('/text_to_audio/{text}/female')
# def text_male_voice(text: str):
#     textToVoice(text, 'Milena', w=True)
#     return FileResponse("result/test.mp3", filename='yourfile.mp3')

def userInteraction():
    x = ''
    while(x != 'pdf' and x != 'текст'):
        x = input('Вам необходимо озвучить текст или pdf? ')
        print(x)

    if(x == 'pdf'):
        path = input('Введите путь до pdf файла: ')
        text = pdfToText(path)
    else:
        text = input('Введите текст, который необходимо озвучить: ')

    t = ''
    # while (t != 'Yuri' and t != 'Milena'):
    #     t = input('Введите голос озвучки (Yuri/Milena) ')

    r = 1000
    while(r > 100 or r < -100):
        r = int(input('Введите скорость озвучки (от -100 до 100, 0 обычная) '))

    v = 1
    while (v > 0.9 or v < -0.9):
        v = float(input('Введите громкость озвучки (от -0.9 до 0.9, 0 обычная) '))

    w = ''
    while(w != 'Да' and w != 'Нет'):
        w = input('Нужно ли записать аудио? (Да/Нет) ')

    if(w == 'Да'): w = True
    else: w = False

    textToVoice(text, t, r, v, w)



def pdfToText(url):
    pdf_document = url
    result = ''
    with open(pdf_document, "rb") as filehandle:
        pdf = PdfFileReader(filehandle)
        pages = pdf.getNumPages()
        for i in range(pages):
            page = pdf.getPage(i)
            result += page.extractText()
        return result


def textToVoice(text, t = 'Yuri', r = 0, v = 0, w = False):
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + r)

    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + v)
    #
    # voices = engine.getProperty('voices')
    # for voice in voices:
    #     if(voice.name == t):
    #         engine.setProperty('voice', voice.id)
    #         break


    if(w == False):
        print('Озвучка текста:\n ' + text)
        engine.say(text)
        print('Успешно озвучено')
    else:
        print('Запись текста в аудио:\n ' + text)
        engine.save_to_file(text, 'result.mp3')
        print('Успешно записано')

    engine.runAndWait()

#print(pdfToText("text/text.pdf"))
#textToVoice(pdfToText("text/text.pdf"), 'Yuri', w = True)
userInteraction()
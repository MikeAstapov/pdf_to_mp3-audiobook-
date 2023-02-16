from gtts import gTTS
from pathlib import Path
import pdfplumber


def pdf_to_mp3(file_path='sample', language='en'): # При смене языка в pdf не забудьте изменить параметр language
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print('[INFO] PROCESSING...')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        with open('text1.txt', 'w') as file:
            file.write(text)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f"{file_name}.mp3")
        return print(f"[INFO]  Convert to {file_name}.mp3 complete.")


        # return "File exists!"
    else:
        return "File not exists.Check file path!"


def main():
    pdf_to_mp3(r'D:\python_projects\pdf_to_mp3\pdf_to_mp3-audiobook-\sample.pdf')


if __name__ == '__main__':
    main()
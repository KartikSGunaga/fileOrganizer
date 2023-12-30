import os
from gtts import gTTS

class convertTextToSpeech:
    def __init__(self, text, lang, pace):
        self.text = text
        self.language = lang
        self.pace = pace

    def transcribeAndSave(self):
        speechFile = gTTS(text=self.text, lang=self.language, slow = self.pace)
        fileName = input("\nEnter the filename of the speech mp3 file: ")
        speechFile.save(f"{fileName}.mp3")

        return fileName

    def playFile(self, fileName):
        os.system(f"mpg321 {fileName}")


def main():
    print("\nWelcome to the speech generator!")

    filename = input("Enter the filename: ")
    with open(filename) as file:
        textToRead = file.read()

    language = input("Enter the language: ")
    flag = True

    while flag:
        try:
            pace = int(input("Press 1 for slow pace; 0 for high pace: "))
            if pace in [0, 1]:
                flag = False
                break
        except ValueError:
            print("Please enter 1 or 0.")


    convert = convertTextToSpeech(textToRead, language, pace)
    fileName = convert.transcribeAndSave()

    while True:
        try:
            pace = int(input("Press 1 to read the text; 2 to exit: "))
            if pace in [0, 1]:
                break
        except ValueError:
            print("Please enter 1 or 2.")

    if pace == 1:
        convert.playFile(filename)


if __name__ == '__main__':
    main()

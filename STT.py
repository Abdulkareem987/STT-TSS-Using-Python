import speech_recognition as speech

r = speech.Recognizer()
with speech.Microphone() as mic:
    print("Start your speech")
    r.adjust_for_ambient_noise(mic, duration=0.2)
    audio = r.listen(mic)

# Credentials for IBM watson speech to text service

IBM_USERNAME = "apikey"
IBM_PASSWORD = "enter your api key"

result = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language="en-US", show_all=False)

try:
    print("What you said was: " + result)
except speech.UnknownValueError:
    print("Speech was not understood")
except speech.RequestError as e:
    print("Request fail; {0}".format(e))

with open('result.txt', mode='w') as file:
    file.write("Recognized text: ")
    file.write(result)
print("Exporting to text is done!")

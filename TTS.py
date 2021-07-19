from ibm_cloud_sdk_core import authenticators
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.websocket import audio_source


#Credentials for IBM watson text to speech service
apikey = 'enter your api key'
url = 'enter your service url'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

#Open result.txt file, or replace if you'd like to open a different txt file
with open ('result.txt', 'r') as f:
    text = f.readlines()

#The next two lines are for remvocing spaces from a txt file
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)

with open ('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_KevinV3Voice').get_result()
    audio_file.write(res.content)

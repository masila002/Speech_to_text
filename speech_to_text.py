import speech_recognition as sr
import pyttsx3

#initialize the recognizer
r = sr.Recognizer()

def record_text():
    while(1):
        try:
            #use the microphone
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                #listen to input 
                audio2 = r.listen(source2)

                #using google to recognize audio
                MyText = r.recognize_google(audio2)

                return MyText      #return this text if it does work and end the fuction

        except sr.RequestError as e:
            print("could not request results: {0}", format(e))    #if the word could not be recognized output error and repeat the loop
            
        except sr.UnknownValueError:
            print("Unknown error occurred")
                  
    return

def output_text(text):
    f = open("output.txt", "a")      #open text file, a is for appending the text
    f.write(text)                    #write the text from the audio
    f.write("\n")                    #write to a new line after every sentence
    f.close()

    return

while(1):
    text = record_text()
    output_text(text)

    print("Wrote text")



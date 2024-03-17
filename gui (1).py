import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from PIL import Image

# Function to handle button click
def on_button_click():
    user_query = entry.get()
    query_processor(user_query)
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',130)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
    

# Function to process the user's query
def query_processor(query):
    # Implement the query processing logic here based on the user's query
    # You can call your existing functions like takeCommand() and perform actions based on the query
    

    # cx
    messagebox.showinfo("User Query", f"User Query: {query}")

# Create the main application window
root = tk.Tk()
root.title("STUDENT AI NAVI HELPER")

# Create a label
label = tk.Label(root, text="Ask your question:")
label.pack(pady=10)

# Create an entry widget to get user input
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create a button to process the user's query
button = tk.Button(root, text="Ask", command=on_button_click)
button.pack(pady=10)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("student ai navi helper.... I i will guide you regarding anything please enter question")
    
    
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        if ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'library' in query:
            print('Head west and go straight...for 450 meters, Turn left and move farward for 90 meters,then turn Right and move farward for 20 meters....,and turn left and tavel for 40 meters .....Thereyou can find  central library  Building')
            speak('Proceed in a westerly direction and maintain a straight path for a distance of 450 meters. Upon reaching this point, execute a left turn and advance for 90 meters. Subsequently, initiate a right turn and advance for a further 20 meters. Then, execute another left turn and travel for 40 meters. At the conclusion of this distance, you will arrive at the location of the central library Building.')
            im = Image.open("images/library.jpg")
            im.show()
        
        elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') in query and ('aeronautical block') in query:
            print('Head west and travel for 1 kilometer turn right You can find eleventh block also called as aeronautical block')
            speak('Head west and travel for 1 kilometer turn right You can find eleventh block also called as aeronautical block')
            im = Image.open("images/eleventh block.jpg")
            im.show()
        elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') in query and ('block 11') in query:
            print('Head west and travel for 1 kilometer turn right You can find eleventh block also called as aeronautical block')
            speak('Head west and travel for 1 kilometer turn right You can find eleventh block also called as aeronautical block')
            im = Image.open("images/eleventh block.jpg")
            im.show()
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and('admission block') in query:
            print('Head west and continue on the road for 800, there you can see barcades,turn right and move farword for 50 meters ,there you can find admission block on right side')
            speak('Head west and continue on the road for 800, there you can see barcades,turn right and move farword for 50 meters ,there you can find admission block on right side')
            im = Image.open("images/admission.jpg")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and('administrative block') in query:
            print('Head west and continue on the road for 800, there you can see barcades,turn right and move farword for 50 meters ,there you can find admission block on right side')
            speak('Head west and continue on the road for 800, there you can see barcades,turn right and move farword for 50 meters ,there you can find admission block on right side')
            im = Image.open("images/admission.jpg")
            im.show()
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai') and('block 5') in query:
            print('Head west and continue on road for 850 meters and turn right and move farword for 90 meters there you can find Department of Mechanical engineering block')
            speak('Head west and continue on road for 850 meters and turn right and move farword for 90 meters there you can find Department of Mechanical engineering block')
            im = Image.open("images/mechanical.jpg")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai') and('mechanical block') in query:
            print('Head west and continue on road for 850 meters and turn right and move farword for 90 meters there you can find Department of Mechanical engineering block')
            speak('Head west and continue on road for 850 meters and turn right and move farword for 90 meters there you can find Department of Mechanical engineering block')
            im = Image.open("images/mechanical.jpg")
            im.show()
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and ('computer block') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 40 meters..... there computer block is on left side')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 40 meters..... there computer block is on left side')
            im = Image.open("images/computer.jpg")
            im.show()
            
        elif ('route 'or 'navigate' or 'way'or 'daari'or'patai')and ('computer science block') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 40 meters..... there computerscience block is on right side')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 40 meters..... there computerscience block is on right side')
            im = Image.open("images/computer.jpg")
            im.show()
            
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and ('abdul kalam block') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Dr.A.P.J.abdul kalam block is on right side')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Dr.A.P.J.abdul kalam  block is on right side')
            im = Image.open("images/kalam.jpg")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and ('block 8') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Dr.A.P.J.abdul kalam block is on right side')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Dr.A.P.J.abdul kalam  block is on right side')
            im = Image.open("images/kalam.jpg")
            im.show()
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and ('polytechnic block') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 500 meters..... there Arulmigu kalagalingam Polytecnic collage  is on front')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 500 meters..... there Arulmigu kalagalingam Polytecnic collage  is on front')
            im = Image.open("images/polytechic.jpg")
            im.show()
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and ('biotechnology block') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 400 meters..... there  biotechnology block  is on right')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 400 meters..... there  biotechnology block  is on right')
            im = Image.open("images/biotech.jpg")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and ('block 7') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 400 meters..... there  biotechnology block  is on right')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 400 meters..... there  biotechnology block  is on right')
            im = Image.open("images/biotech.jpg")
            im.show()
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and('civil block') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Civil engineering block is on left side')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Civil engineering block is on left side')
            im = Image.open("images/tenth.jpg")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and('block 10') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Civil engineering block is on left side')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Civil engineering block is on left side')
            im = Image.open("images/tenth.jpg")
            im.show()
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and('mh1') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Civil engineering  is on left side')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Civil engineering  is on left side')
            im = Image.open("images/nelson.jpg")
            im.show()
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and('nelson mandela hostel') in query:
            print('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Civil engineering  is on left side')
            speak('Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Civil engineering  is on left side')
            im = Image.open("images/nelson.jpg")
            im.show()
            
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and('pharmacy block') in query:
            print('Head west and continue on the road for 1100 meters... turn right and travel for 90 meters..... and turn left move farword for 20 meters..... there Arulmigu kalasalingam collage of pharmacy  ')
            speak('Head west and continue on the road for 1100 meters... turn right and travel for 90 meters..... and turn left move farword for 20 meters..... there Arulmigu kalasalingam collage of pharmacy  ')
            im = Image.open("images/pharmacy.jpg")
            im.show()
            
        
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and('mh2') in query:
            print('head west and go straight  for 1000 meters and there you can find the Bhagath singh hostel on the left side')
            speak('head west and go straight  for 1000 meters and there you can find the Bhagath singh hostel on the left side')
            im = Image.open("")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and('bhagat singh hostel') in query:
            print('head west and go straight  for 1000 meters and there you can find the Bhagath singh hostel on the left side')
            speak('head west and go straight  for 1000 meters and there you can find the Bhagath singh hostel on the left side')
            im = Image.open("")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and('mh3'or 'bhagath singh hostel') in query:
            print('head west and go straight  for 1100 meters and there you can find the DR.sarevypally radha krishnan  hostel on the left side')
            speak('head west and go straight  for 1100 meters and there you can find the DR.sarevypally radha krishnan  hostel on the left side')
            im = Image.open("images/radha krishnan.jpg")
            im.show()
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'sodexo' in query:
            print('head west and go straight  for 750 meters and there you can find the sodexo food and you....canteen on the left side')
            speak('head west and go straight  for 750 meters and there you can find the sodexo food and you....canteen on the left side')
            im = Image.open("images/sodexo.jpg")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'COE office' in query:
            print('head west and go straight  for 800 meters and there you can find the control of examination office on the right side')
            speak('head west and go straight  for 800 meters and there you can find the control of examination office on the right side')
            im = Image.open("images/COE.jpg")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'auditorium' in query:
            print('head west and go straight  for 700 meters and there you can find the control of KS krishnan auditorium on the right side')
            speak('head west and go straight  for 700 meters and there you can find the control of KS krishnan auditorium on the right side')
            im = Image.open("images/Auditorium.jpg")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'tifac core building' in query:
            print('head west and go straight  for 700 meters and there you can find the Tifac Core Building on the left side')
            speak('head west and go straight  for 700 meters and there you can find the  Tifac Core Building on the left side')
            im = Image.open("images/Tifac.jpg")
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'block 1' in query:
            print('head west and go straight  for 700 meters and there you can find the Tifac Core Building on the left side')
            speak('head west and go straight  for 700 meters and there you can find the  Tifac Core Building on the left side')
            im = Image.open("images/Tifac.jpg")
            im.show()
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'guest house' in query:
            print('head west and go straight  for 170 meters....  turn left and travel for 40 meters then turn right 230 meters and there you can find the Guest House on the right side')
            speak('head west and go straight  for 170 meters....  turn left and travel for 40 meters then turn right 230 meters and there you can find the Guest House on the right side')
            im = Image.open("images/Guest house.jpg")
            im.show()
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'computer science' and 'hod cabin'in query:
            print('It is in the eigth block sixth floor room number 8612')
            speak('It is in the eigth block sixth floor room number eight six one two')
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'computer science' and 'dean cabin'in query:
            print('It is in the eigth block sixth floor room number 8512')
            speak('It is in the eigth block sixth floor room number eight five one two')
            
        elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'computer science' and 'course coordinator cabin'in query:
            print('It is in the eigth block sixth floor room number 8611')
            speak('It is in the eigth block sixth floor room number eight six one one')
        else:
            print('Sorry...!')
            print("Can't understand your command")
            speak("Sorry,Can't understand your command")

# Run the GUI application
root.mainloop()

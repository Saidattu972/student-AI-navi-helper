import tkinter as tk
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr
from PIL import Image

def takeCommand():
    
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
        print("Say that again, please...")
        return "None"
    return query

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    entry.delete(0, 'end')  
    query = takeCommand().lower()
    entry.insert(0, query)  
    query_processor(query) 

def on_button_click():
    user_query = entry.get()
    query_processor(user_query)

def query_processor(query):
    
    if ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('library') in query:
        response = "Proceed in a westerly direction and maintain a straight path for a distance of 450 meters. " \
                    "Upon reaching this point, execute a left turn and advance for 90 meters. " \
                    "Subsequently, initiate a right turn and advance for a further 20 meters. " \
                    "Then, execute another left turn and travel for 40 meters. " \
                    "At the conclusion of this distance, you will arrive at the location of the central library Building."
        speak(response)
        messagebox.showinfo("Library Location", response)
        # Display the library image
        image = Image.open("c:/Users/user/Downloads/maxresdefault (1).jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('block 11') in query:
        response = 'Head west and travel for 1 kilometer turn right You can find eleventh block also called as aeronautical block'
        speak(response)
        messagebox.showinfo("block 11", response)
        # Display the library image
        image = Image.open("")
        image.show()
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('aeronautical') in query:
        response = 'Head west and travel for 1 kilometer turn right You can find eleventh block also called as aeronautical block'
        speak(response)
        messagebox.showinfo("aeronautical block", response)
        # Display the library image
        image = Image.open("C:/Users/user/Downloads/projectiiitdm/images/WhatsApp Image 2024-03-17 at 8.42.12 AM.jpeg")
        image.show()
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('iiitdm') in query:
        response = 'Head west and continue on the road for 800, there you can see barcades,turn right and move farword for 50 meters ,there you can find admission block on right side'
        speak(response)
        messagebox.showinfo("iiitdm entrance gate", response)
        # Display the library image
        image = Image.open("C:/Users/user/Downloads/projectiiitdm/images/WhatsApp Image 2024-03-17 at 8.42.13 AM (2).jpeg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('administrative') in query:
        response = 'Head west and continue on the road for 800, there you can see barcades,turn right and move farword for 50 meters ,there you can find admission block on right side'
        speak(response)
        messagebox.showinfo("administrative block", response)
        # Display the library image
        image = Image.open("C:/Users/user/Downloads/projectiiitdm/images/WhatsApp Image 2024-03-17 at 8.42.13 AM.jpeg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('mechanical') in query:
        response = 'Head west and continue on road for 850 meters and turn right and move farword for 90 meters there you can find Department of Mechanical engineering block'
        speak(response)
        messagebox.showinfo("Mechanical engineering block", response)
        # Display the library image
        image = Image.open("C:/Users/user/Downloads/projectiiitdm/images/WhatsApp Image 2024-03-17 at 8.42.12 AM (2).jpeg")
        image.show()
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('ashoka hostel') in query:
        response = 'Head west and continue on road for 850 meters and turn right and move farword for 90 meters there you can find Department of Mechanical engineering block'
        speak(response)
        messagebox.showinfo("ashoka hostel", response)
        # Display the library image
        image = Image.open("C:/Users/user/Downloads/projectiiitdm/images/WhatsApp Image 2024-03-17 at 8.42.12 AM (2).jpeg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('awastha hostel') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 40 meters..... there computer block is on left side'
        speak(response)
        messagebox.showinfo("awastha hostel", response)
        # Display the library image
        image = Image.open("C:/Users/user/Downloads/projectiiitdm/images/WhatsApp Image 2024-03-17 at 8.42.12 AM (1).jpeg")
        image.show()
        
        
    elif('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and ('college view') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Dr.A.P.J.abdul kalam block is on right side'
        speak(response)
        messagebox.showinfo("college view", response)
        # Display the library image
        image = Image.open("C:/Users/user/Downloads/projectiiitdm/images/WhatsApp Image 2024-03-17 at 8.42.12 AM (1).jpeg")
        image.show()
    elif('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and ('block 9') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Dr.A.P.J.abdul kalam block is on right side'
        speak(response)
        messagebox.showinfo("abdul kalam block", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/kalam.jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('polytechnic') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 500 meters..... there Arulmigu kalagalingam Polytecnic collage  is on front'
        speak(response)
        messagebox.showinfo("aeronautical block", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/eleventh.jpg")
        image.show()
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('computer science') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 40 meters..... there computerscience block is on right side'
        speak(response)
        messagebox.showinfo("computer science block", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/ramanujan.jpg")
        image.show()
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('ramanujan') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 40 meters..... there computerscience block is on right side'
        speak(response)
        messagebox.showinfo("computer science block", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/ramanujan.jpg")
        image.show()
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('block 8') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 40 meters..... there computerscience block is on right side'
        speak(response)
        messagebox.showinfo("computer science block", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/ramanujan.jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('sodexo') in query:
        response = 'head west and go straight  for 750 meters and there you can find the sodexo food and you....canteen on the left side'
        speak(response)
        messagebox.showinfo("sodexo", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/sodexo.jpg")
        image.show()
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('canteen') in query:
        response = 'head west and go straight  for 750 meters and there you can find the sodexo food and you....canteen on the left side near by you can find nalabagam canteen also'
        speak(response)
        messagebox.showinfo("sodexo", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/sodexo.jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')and ('biotechnology') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 400 meters..... there  biotechnology block  is on right'
        speak(response)
        messagebox.showinfo("biotech block", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/biotech.jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('biotech block') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 400 meters..... there  biotechnology block  is on right'
        speak(response)
        messagebox.showinfo("biotech block", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/biotech.jpg")
        image.show()
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('block 7') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 400 meters..... there  biotechnology block  is on right'
        speak(response)
        messagebox.showinfo("biotech block", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/biotech.jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('auditorium') in query:
        response = 'head west and go straight  for 800 meters and there you can find the control of examination office on the right side'
        speak(response)
        messagebox.showinfo("auditorium", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/Auditorium.jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('coe office') in query:
        response ='head west and go straight  for 800 meters and there you can find the control of examination office on the right side'
        speak(response)
        messagebox.showinfo("COE", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/COE.jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('guest house') in query:
        response = 'head west and go straight  for 170 meters....  turn left and travel for 40 meters then turn right 230 meters and there you can find the Guest House on the right side'
        speak(response)
        messagebox.showinfo("Guest House", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/Guest house.jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')  and ('nelson mandela hostel') in query:
        response = 'head west and go straight  for 1000 meters and there you can find the nelson mandela on the left side'
        speak(response)
        messagebox.showinfo("MH-1", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/nelson.jpg")
        image.show()
    
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('mh1') in query:
        response = 'head west and go straight  for 1000 meters and there you can find the Nelson mandela  on the left side'
        speak(response)
        messagebox.showinfo("MH-1", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/nelson.jpg")
        image.show()

    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('radha krishnan hostel') in query:
        response ='head west and go straight  for 1100 meters and there you can find the DR.sarevypally radha krishnan  hostel on the left side'
        speak(response)
        messagebox.showinfo("MH-3/ Radha krishnan hostel", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/radha krishnan.jpg")
        image.show() 
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('mh3') in query:
        response ='head west and go straight  for 1100 meters and there you can find the DR.sarevypally radha krishnan  hostel on the left side'
        speak(response)
        messagebox.showinfo("MH-3/ Radha krishnan hostel", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/radha krishnan.jpg")
        image.show()     
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('civil') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Civil engineering block is on left side'
        speak(response)
        messagebox.showinfo("civil block / 10th block", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/tenth.jpg")
        image.show()
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai')and ('block 10') in query:
        response = 'Head west and continue on the road for 800 meters... turn right and travel for 160 meters..... and turn left move farword for 150 meters..... there Civil engineering block is on left side'
        speak(response)
        messagebox.showinfo("civil block / 10th block", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/tenth.jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('medical') in query:
        response = 'head west and go straight  for 700 meters and there you can find the Tifac Core Building on the left side'
        speak(response)
        messagebox.showinfo("Medical block or Tifac core", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/Tifac.jpg")
        image.show()
        
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('tifac core') in query:
        response = 'head west and go straight  for 700 meters and there you can find the Tifac Core Building on the left side'
        speak(response)
        messagebox.showinfo("Medical block or Tifac core", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/Tifac.jpg")
        image.show()
    elif ('where'or 'route' or 'navigate' or 'way' or 'daari' or 'patai') and ('pharmacy') in query:
        response = 'Head west and continue on the road for 1100 meters... turn right and travel for 90 meters..... and turn left move farword for 20 meters..... there Arulmigu kalasalingam collage of pharmacy  '
        speak(response)
        messagebox.showinfo("Pharmacy", response)
        # Display the library image
        image = Image.open("C:/Users/Pavan Chand/Downloads/kareeka/images/pharmacy.jpg")
        image.show()
    elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and 'hod cabin'in query:
        response = 'It is in the eigth block sixth floor room number 8612'
        speak(response)
        messagebox.showinfo("hod cabin", response)
    elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and 'cse dean cabin'in query:
        response = 'It is in the eigth block sixth floor room number 8512'
        speak(response)
        messagebox.showinfo("cse dean cabin", response)
    elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'course coordinator cabin'in query:
        response = 'It is in the eigth block sixth floor room number 8611'
        speak(response)
        messagebox.showinfo("course coordinator cabin", response)

    elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'cse hod room'in query:
        response = 'Dr. N.Suresh kumar sir is avaliable 8th block 6th floor room number 8612'
        speak(response)
        messagebox.showinfo("cse hod room", response)

    elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'aiml stream coordinator'in query:
        response = 'Mr. R. Raja Subramanian sir is avaliable 8th block 6th floor room number 8611 4th cabin'
        speak(response)
        messagebox.showinfo("aiml stream coordinator", response)

    elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and 'mechanical hod room' in query:
        response='Sir is avaliable 5th block first floor room number 5101'
        speak(response)
        messagebox.showinfo("Sir is avaliable fifth block first floor room number five one zero one", response)

    elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'mathematical hod Room'in query:
        response = ' Dr.Kameshwari mam is avaliable 9th block 3rd floor room number 9301'
        speak(response)
        messagebox.showinfo('Dr.Kameshwari mam is avaliable nineth block third floor room number Nine three zero one',response)

    elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai') and'cyber security stream coordinator'in query:
        response = 'Dr N.C Brintha mam is avaliable 8th block 6th floor room number 8611 9th cabin'
        speak(response)
        messagebox.showinfo('Dr N.C Brintha mam is avaliable eighth block sixth floor room number eight six eleven nineth cabin',response)

    elif ('where'or'route 'or 'navigate' or 'way'or 'daari'or'patai')and'iot stream coordinator'in query:
        response = ' Dr C. Bala Subramanian sir is avaliable 8th block 6th floor room number 8611 11th cabin'
        speak(response)
        messagebox.showinfo('Dr C. Bala Subramanian sir is avaliable eighth block sixth floor room number eight six eleven 11th cabin',response)
  
    
    else:
        response = "I'm sorry, I don't have information on that location."
        speak(response)
        messagebox.showinfo("Location Not Found", response)

root = tk.Tk()
root.title("Student AI NAVI HELPER")


root.configure(bg="#e6e6e6")


label1 = tk.Label(root, text="IIITDM KANCHIPURAM", width=120, bg="#e6e6e6", font=("Helvetica", 20))
label = tk.Label(root, text="Ask your question:", width=120, bg="#e6e6e6", font=("Helvetica", 16))
label.pack(pady=20)
label1.pack(pady=20)

entry = tk.Entry(root, width=100, font=("Helvetica", 14))
entry.pack(pady=20)


button = tk.Button(root, text="Ask", command=on_button_click, width=15, bg="#4CAF50", fg="white", font=("Helvetica", 14))
button.pack(pady=10)


listen_button = tk.Button(root, text="Listen", command=listen, width=15, bg="#2196F3", fg="white", font=("Helvetica", 14))
listen_button.pack(pady=10)

root.mainloop()
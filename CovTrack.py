#MODULES USED

import tkinter as tk
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


#COVID Cases Tracker
def covid_tracker():
  
  frame = tk.Frame( root, bd=3, bg='#c20000')
  frame.place( relx=0.1, rely=0.12, relheight=0.08, relwidth=0.8 )

  global search_label
  search_label = tk.Label( frame, bd=5, font = ('Helvetica',15,'bold'), anchor = 'nw', justify = 'center', fg='#00948f', text = "Enter Location")
  search_label.place(relx=0.03, rely=0.11, relheight=0.79, relwidth=0.24)

  global entry
  entry = tk.Entry( frame, bd=3,font = ('Helvetica',14))
  entry.place(relx=0.28, rely=0.11, relheight=0.8, relwidth=0.5 )

  global label
  label = tk.Label( bottom_frame, bd=2, bg = '#fffcfc', font = ('Helvetica',15,'bold'), anchor = 'nw', justify = 'left', fg='#c20000')
  label.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

  label['text'] = "Enter a State or Union Territory of India."

  button = tk.Button( frame, text="Get Data", bd=2, fg='#c20000',font = ('Helvetica',14,'bold'), command = send_data)
  button.place( relx=0.79, rely=0.11, relheight=0.8, relwidth=0.2 )


  menu_button = tk.Button( bottom_frame,bd=3, text = "Menu",font = ('Helvetica',13,'bold'),bg='#c20000', fg='#fffcfc', command = menu)
  menu_button.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.1)



#Sends data to the get_covid_data function.
def send_data():
   
  #Gets the state's name from the entry box 
  city = entry.get()

  if city == "":                                            #If user doesn't input any string
    label['text'] = "Please Enter a Location!!"   
  else:
    label['text'] = get_covid_data(city)             



#Gets the COVID cases from the website.
def get_covid_data(city):
    
  url = "https://news.google.com/covid19/map?hl=en-IN&mid=%2Fm%2F03rk0&gl=IN&ceid=IN%3Aen"
  r = requests.get(url).text
  soup = BeautifulSoup(r, 'html5lib')
  table = soup.find('table',class_='pH8O4c')

  #print(table.prettify())

  locations = []
  numbers = []

  for data in table.find_all('th'):
      locations.append(data.text)

  for data in table.find_all('td'):
      numbers.append(data.text)

  for x in numbers:
      if x == '':
          numbers.remove(x)


  data = {}
  
  for location in range(6,len(locations)):
      data[locations[location]] = []

  for i in range(len(data)):

      data[locations[i+6]] = [numbers[x] for x in range(4*i,4*(i+1))]
  state = city
  state.strip()
  state = state[0].upper() + state[1:]

  return f"""
        
        
      Total number of COVID cases worldwide: {data['Worldwide'][0]}
          
      Total number of COVID cases in India: {data['India'][0]}

      {state}'s COVID Cases Information:

      -> Total number of cases: {data[state][0]}
      -> Cases per million: {data[state][1]}
      -> New cases: {data[state][2]}
      -> Deaths: {data[state][3]}
          """



#Getting the Data of all the Countries
def get_covid_data(country):

  url = "https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen"
  r = requests.get(url).text
  soup = BeautifulSoup(r, 'html5lib')
  table = soup.find('table', class_='pH8O4c')

  locations = []
  numbers = []

  for data in table.find_all('th'):
      locations.append(data.text)

  for data in table.find_all('td'):
      numbers.append(data.text)

  for x in numbers:
      if x == '':
          numbers.remove(x)

  data = {}

  for location in range(6, len(locations)):
      data[locations[location]] = []

  for i in range(len(data)):

      data[locations[i+6]] = [numbers[x] for x in range(4*i, 4*(i+1))]
  state = country
  state.strip()
  state = state[0].upper() + state[1:]

  print(locations)
  print(numbers)

  return f"""
        
        
      Total number of COVID cases worldwide: {data['Worldwide'][0]}
          
      {state}'s COVID Cases Information:
      -> Total number of cases: {data[state][0]}
      -> Cases per million: {data[state][1]}
      -> New cases: {data[state][2]}
      -> Deaths: {data[state][3]}
          """


#Symptoms Checker Function.
def symptoms_checker():
  
  global selections
  selections = [tk.IntVar() for x in range(12)]

  bottom_frame = tk.Frame( root, bg='#ff5454')
  bottom_frame.place(relx=0.1, rely=0.25, relheight=0.65, relwidth=0.8)

  label = tk.Label( bottom_frame, bd=2, bg = '#ff8787', font = ('Helvetica',13,'bold'), anchor = 'nw', justify = 'left', fg='#00827e')
  label.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
  

  #List of Different Symptoms Checkboxes
  
  fever_button = tk.Checkbutton(bottom_frame, selectcolor = "green", onvalue = 1, offvalue = 0, text="Fever", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'), variable = selections[0])
  fever_button.place( relx=0.1, rely=0.1, relheight=0.1, relwidth=0.24 )
  
  cough_button = tk.Checkbutton(bottom_frame, selectcolor = "green",text="Dry Cough", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'),variable = selections[1])
  cough_button.place( relx=0.4, rely=0.1, relheight=0.1, relwidth=0.24 )
  
  tiredness_button = tk.Checkbutton(bottom_frame, selectcolor = "green", text="Tiredness", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'), variable = selections[2])
  tiredness_button.place( relx=0.7, rely=0.1, relheight=0.1, relwidth=0.24 )
  
  aches_button = tk.Checkbutton(bottom_frame, selectcolor = "green", text="Aches & Pain", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'),variable = selections[3])
  aches_button.place( relx=0.1, rely=0.23, relheight=0.1, relwidth=0.24 )
  
  throat_button = tk.Checkbutton(bottom_frame, selectcolor = "green", text="Sore throat", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'),variable = selections[4])
  throat_button.place( relx=0.4, rely=0.23, relheight=0.1, relwidth=0.24 )
 
  diarrhoea_button = tk.Checkbutton(bottom_frame, selectcolor = "green", text="Diarrhoea", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'),variable = selections[5])
  diarrhoea_button.place( relx=0.7, rely=0.23, relheight=0.1, relwidth=0.24 )
  
  conjunctivitis_button = tk.Checkbutton(bottom_frame, selectcolor = "green", text="Conjunctivitis", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'),variable = selections[6])
  conjunctivitis_button.place( relx=0.1, rely=0.36, relheight=0.1, relwidth=0.24 )
 
  headache_button = tk.Checkbutton(bottom_frame, selectcolor = "green", text="Headache", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'),variable = selections[7])
  headache_button.place( relx=0.4, rely=0.36, relheight=0.1, relwidth=0.24 )

  loss_button = tk.Checkbutton(bottom_frame, selectcolor = "green", text="Loss of taste", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'),variable = selections[8])
  loss_button.place( relx=0.7, rely=0.36, relheight=0.1, relwidth=0.24 )

  rashes_button = tk.Checkbutton(bottom_frame, selectcolor = "green", text="Rashes", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'),variable = selections[9])
  rashes_button.place( relx=0.1, rely=0.36, relheight=0.1, relwidth=0.24 )

  chest_button = tk.Checkbutton(bottom_frame, selectcolor = "green", text="Chest Pain", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'),variable = selections[10])
  chest_button.place( relx=0.4, rely=0.49, relheight=0.1, relwidth=0.24 )

  submit_button = tk.Button(bottom_frame, text="Submit", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'), command = calculate_case)
  submit_button.place( relx=0.25, rely=0.7, relheight=0.15, relwidth=0.5 )

 

#This function decides if the user has minimal or serious symptoms.
def calculate_case():

  frame = tk.Frame( root, bd=3, bg='#9e0000')
  frame.place( relx=0.1, rely=0.12, relheight=0.08, relwidth=0.8 )

  search_label = tk.Label( frame, bd=0, font = ('Helvetica',15,'bold'), anchor = 'nw', justify = 'center', fg='#fffcfc', bg='#9e0000', text = "Result")
  search_label.place(relx=0.5, rely=0.11, relheight=0.79, relwidth=0.22)
 
    
  bottom_frame = tk.Frame( root, bg='#ff5454')
  bottom_frame.place(relx=0.1, rely=0.25, relheight=0.65, relwidth=0.8)


  label = tk.Label( bottom_frame, bd=2, bg = '#fffcfc', font = ('Helvetica',12,'bold'), anchor = 'nw', justify = 'left', fg='#c20000')
  label.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

  if(sum([x.get() for x in selections])>=5):
  
    label['text'] = f"""
      YOU HAVE SERIOUS SYMPTOMS:
      -----------------------------------------------------

        -> Call a doctor or hospital right away.

        -> You need medical care as soon as possible.

        -> Call your doctor’s office or hospital before you go in.

        -> This will help them prepare to treat you and protect medical staff 
            and other patients.

        -> Take the COVID 19 Test. If results are positive, follow all the 
            instructions given by the doctor and maintain strict quarantine.

    """
    
    next_button = tk.Button( bottom_frame,bd=3, text = "Next",font = ('Helvetica',13,'bold'),bg='#c20000', fg='#fffcfc', command = toll)
    next_button.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.1)

  else:
    
    label['text'] = f"""
      YOU HAVE MINIMAL SYMPTOMS:
      -----------------------------------------------------

        -> Stay at home and exercise normal precautions.

        -> Maintain social distancing.

        -> Wear a mask when you go out in public.

        -> Cover your mouth and nose with a mask when around others.

        -> Monitor Your Health Daily.

        -> If you start experiencing any of the above symptoms, 
            please contact a doctor.

    """
    menu_button = tk.Button( bottom_frame,bd=3, text = "Menu",font = ('Helvetica',13,'bold'),bg='#c20000', fg='#fffcfc', command = menu)
    menu_button.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.1)
  


#Toll function which executes if the user has serious symptoms.
def toll():
  
  frame = tk.Frame( root, bd=3, bg='#9e0000')
  frame.place( relx=0.1, rely=0.12, relheight=0.08, relwidth=0.8 )

  
  search_label = tk.Label( frame, bd=0, font = ('Helvetica',15,'bold'), anchor = 'nw', justify = 'center', fg='#fffcfc', bg='#9e0000', text = "Toll Free Numbers")
  search_label.place(relx=0.44, rely=0.11, relheight=0.79, relwidth=0.28)
 
    
  bottom_frame = tk.Frame( root, bg='#ff5454')
  bottom_frame.place(relx=0.1, rely=0.25, relheight=0.65, relwidth=0.8)


  label = tk.Label( bottom_frame, bd=2, bg = '#fffcfc', font = ('Helvetica',12,'bold'), anchor = 'nw', justify = 'left', fg='#c20000')
  label.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

  label['text'] = f"""   1. Andhra Pradesh - 0866-2410978
    2.Arunachal Pradesh - 9436055743
    3.Assam - 6913347770                           
    4.Bihar - 104                                   
    5.Chhattisgarh - 077122-35091                   
    6.Goa - 104                                     
    7.Gujarat - 104                                 
    8.Haryana - 8558893911                          
    9.Himachal Pradesh - 104                        
    10.Jharkhand - 104                              
    11.Karnataka - 104                              
    12.Kerala - 0471-2552056                        
    13.Madhya Pradesh - 0755-2527177                
    14.Maharashtra - 020-26127394                   
    15.Manipur - 3852411668                         
    16.Meghalaya - 108                              
    17.Mizoram - 102                                
    18.Nagaland - 7005539653                        
    19.Odisha - 9439994859
    20.Punjab - 104
    21.Rajasthan - 0141-2225624
  """
  next_button2 = tk.Button( bottom_frame,bd=3, text = "Next",font = ('Helvetica',13,'bold'),bg='#c20000', fg='#fffcfc', command = toll2)
  next_button2.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.1)



#Continuation of the first toll function.
def toll2():

  frame = tk.Frame( root, bd=3, bg='#9e0000')
  frame.place( relx=0.1, rely=0.12, relheight=0.08, relwidth=0.8 )

  search_label = tk.Label( frame, bd=0, font = ('Helvetica',15,'bold'), anchor = 'nw', justify = 'center', fg='#fffcfc', bg='#9e0000', text = "Toll Free Numbers")
  search_label.place(relx=0.44, rely=0.11, relheight=0.79, relwidth=0.28)
 
  bottom_frame = tk.Frame( root, bg='#ff5454')
  bottom_frame.place(relx=0.1, rely=0.25, relheight=0.65, relwidth=0.8)

  label = tk.Label( bottom_frame, bd=2, bg = '#fffcfc', font = ('Helvetica',12,'bold'), anchor = 'nw', justify = 'left', fg='#c20000')
  label.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

  label['text'] = f"""
    22.Sikkim - 104
    23.Tamil Nadu - 044-29510500
    24.Telangana - 104
    25.Tripura - 0381-2315879
    26.Uttarakhand - 104
    27.Uttar Pradesh - 18001805145
    28.West Bengal - 3323412600
    29.Andaman and Nicobar Islands - 03192-232102
    30.Chandigarh - 9779558282
    31.Dadra and Nagar Haveli and Daman & Diu - 104
    32.Delhi - 011-22307145
    33.Jammu - 01912520982
        Kashmir - 01942440283
    34.Ladakh - 01982256462
    35.Lakshadweep - 104
    36.Puducherry - 104
  """

  menu_button = tk.Button( bottom_frame,bd=3, text = "Menu",font = ('Helvetica',13,'bold'),bg='#c20000', fg='#fffcfc', command = menu)
  menu_button.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.1)

 



#Precautions Function.   
def precaution():

  frame = tk.Frame( root, bd=3, bg='#9e0000')
  frame.place( relx=0.1, rely=0.12, relheight=0.08, relwidth=0.8)

  search_label = tk.Label( frame, bd=0, font = ('Helvetica',16,'bold'), anchor = 'nw', justify = 'center', fg='#fffcfc', bg='#9e0000', text = "Precautions")
  search_label.place(relx=0.45, rely=0.11, relheight=0.79, relwidth=0.22)
 
   
  bottom_frame = tk.Frame( root, bg='#ff5454')
  bottom_frame.place(relx=0.1, rely=0.25, relheight=0.65, relwidth=0.8)

  label = tk.Label( bottom_frame, bd=2, bg = '#fffcfc', font = ('Helvetica',12,'bold'), anchor = 'nw', justify = 'left', fg='#c20000')
  label.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)


  label['text'] = f"""
    COVID-19 spreads easily from person to person, 
    mainly by the following routes:

    -> Between people who are in close contact with one another 
      (within 6 feet).
    -> Through respiratory droplets produced when an infected person 
      coughs, sneezes, breathes, sings or talks.
    -> Respiratory droplets cause infection when they are inhaled or 
      deposited on mucous membranes, such as those that line the
      inside of the nose and mouth.
    -> People who are infected but do not have symptoms can also 
      spread the virus to others.
    
    SOME PRECAUTIONARY MEASURES :
    -> Wash your hands often.
    -> Avoid close contact.
    -> Cover your mouth and nose with a mask when around others.
    -> Cover coughs and sneezes.
    -> Clean and disinfect.
    -> Monitor Your Health Daily.
  """

  menu_button = tk.Button( bottom_frame,bd=3, text = "Menu",font = ('Helvetica',13,'bold'),bg='#c20000', fg='#fffcfc', command = menu)
  menu_button.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.1)


#Closes the App.
def close_app(): 
  root.destroy()


#ROOT UI SECTION

#Height and Width
HEIGHT=700
WIDTH=800

root = tk.Tk()

root.title("CovTrack")
root.iconbitmap("covid.ico")

canvas = tk.Canvas( height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage( file='red.png')
background_label = tk.Label( root, image=background_image)
background_label.place(relheight=1, relwidth=1)



#Menu Function
def menu():
  
  global heading_label
  heading_label = tk.Label( root, bd=3, text = "CovTrack", bg='#dbd9d9', fg='#c20000', font = ('Helvetica',20,'bold'))
  heading_label.place( relx=0.4, rely=0.02, relheight=0.065, relwidth=0.22)

  global frame
  frame = tk.Frame( root, bd=3, bg='#9e0000')
  frame.place( relx=0.1, rely=0.12, relheight=0.08, relwidth=0.8)

  global search_label
  search_label = tk.Label( frame, bd=0, font = ('Helvetica',15,'bold'), anchor = 'nw', justify = 'center', fg='#fffcfc', bg='#9e0000', text = "MENU")
  search_label.place(relx=0.48, rely=0.11, relheight=0.79, relwidth=0.12)

  global bottom_frame
  bottom_frame = tk.Frame( root, bg='#ff5454')
  bottom_frame.place(relx=0.1, rely=0.25, relheight=0.65, relwidth=0.8)


  global label
  label = tk.Label( bottom_frame, bd=2, bg = '#ff8787', font = ('Helvetica',13,'bold'), anchor = 'nw', justify = 'left', fg='#00827e')
  label.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)


  tracker_button = tk.Button(bottom_frame, text="COVID Cases Tracker", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'), command = covid_tracker)
  tracker_button.place( relx=0.1, rely=0.1, relheight=0.15, relwidth=0.8 )

  symptoms_button = tk.Button(bottom_frame, text="Symptoms Checker", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'), command = symptoms_checker)
  symptoms_button.place( relx=0.1, rely=0.3, relheight=0.15, relwidth=0.8 )

  precaution_button = tk.Button(bottom_frame, text="Precautionary Measures", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'), command = precaution)
  precaution_button.place( relx=0.1, rely=0.5, relheight=0.15, relwidth=0.8 )

  exit_button = tk.Button(bottom_frame, text="Exit", bd=2, bg='#c20000', fg='#fffcfc',font = ('Helvetica',14,'bold'), command = close_app)
  exit_button.place( relx=0.1, rely=0.7, relheight=0.15, relwidth=0.8 )


  root.mainloop()



#Opens the menu function when the program boots up.
menu()  
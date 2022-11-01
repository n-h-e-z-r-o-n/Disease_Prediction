import joblib

common_disease_model = joblib.load('Common_Disease/model-disease-prediction.joblib')  # loading common disease module.
heart_disease_model = joblib.load('Heart_Disease/model-heart_disease.joblib')  # loading heart disease module.

symptoms_list = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting',
                 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat',
                 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite',
                 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
                 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
                 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels',
                 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain',
                 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
                 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation',
                 'dischromic _patches', 'watering_from_eyes',
                 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding',
                 'distention_of_abdomen',
                 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting',
                 'small_dents_in_nails', 'inflammatory_nails',
                 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

from tkinter import *


# =============== functions ==============
def show_frame(frame):
    frame.tkraise()


def changeOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))


root = Tk()
root.title("Disease Prediction (group 3)")
root.geometry('950x800')
# root.maxsize(950, 800)
root.minsize(950, 800)

# ================================ Side_Bar =========================================
side_frame = Frame(root, bg='#016064')
side_frame.pack(ipadx=100, side=LEFT, fill=Y, expand=False)


Button(side_frame, bg='white', text='Heart Disease', font=("Courier New Bold", 10),  borderwidth=0,  anchor='w', command=lambda: show_frame(Heart_disease_page)).place(relwidth=0.9, relx=0.05, rely=0.25)
Button(side_frame, bg='white', text='Common Disease', font=("Courier New Bold", 10), borderwidth=0, anchor='w', command=lambda: show_frame(Common_Disease_page)).place(relwidth=0.9, relx=0.05, rely=0.3)
Button(side_frame, bg='white', text='information', font=("Courier New Bold", 10), borderwidth=0, anchor='w', command=lambda: show_frame(project_information_page)).place(relwidth=0.9, relx=0.05, rely=0.35)

#  ================================ CONTENT FRAME =========================================
content_main_frame = Frame(root, bg='pink')
content_main_frame.pack(ipadx=200, side=LEFT, fill=BOTH, expand=True)

content_frame1 = Frame(content_main_frame, bg='green')
content_frame1.place(x=0, relwidth=0.998, relheight=1)

Heart_disease_page = Frame(content_main_frame, bg='white')
Heart_disease_page.place(x=0, relwidth=0.998, relheight=1)

Common_Disease_page = Frame(content_main_frame, bg='white')
Common_Disease_page.place(x=0, relwidth=0.998, relheight=1)

project_information_page = Frame(content_main_frame, bg='white')
project_information_page.place(x=0, relwidth=0.998, relheight=1)


#  ========================= Heart_disease_page   ===========================================================================================================
symptoms_frame = Frame(Common_Disease_page, bg='white')
symptoms_frame.place(x=10, y=20, relheight=0.7, relwidth=0.98)

print('end1')
itching = IntVar()

numt = []
k = 0
while k < len(symptoms_list):
    numt.append(k)
    numt[k] = IntVar()
    k = k + 1

i = 0
column1 = column2 =column3 = column4 = column5 =0.02
while i < 150:
    if i <= 29:
        b = Checkbutton(symptoms_frame, text=symptoms_list[i], font=("Courier New Bold", 10), variable=numt[i], onvalue=1, offvalue=0, anchor='w', bg='white')
        b.place(relx=0.01, rely=column1, relwidth=0.19, height=16)
        changeOnHover(b, '#82EEFD', 'white')
        column1 = column1 + 0.032
    if 29 < i <= 59:
        b = Checkbutton(symptoms_frame, text=symptoms_list[i], font=("Courier New Bold", 10), variable=numt[i], onvalue=1, offvalue=0, anchor='w', bg='white')
        b.place(relx=0.21, rely=column2, relwidth=0.19, height=16)
        changeOnHover(b, '#82EEFD', 'white')
        column2 = column2 + 0.032
    if 59 < i <= 89:
        b = Checkbutton(symptoms_frame, text=symptoms_list[i], activebackground='blue', font=("Courier New Bold", 10), variable=numt[i], onvalue=1, offvalue=0, anchor='w', bg='white')
        b.place(relx=0.41, rely=column3, relwidth=0.19, height=16)
        changeOnHover(b, '#82EEFD', 'white')
        column3 = column3 + 0.032
    if 89 < i <= 119:
        b = Checkbutton(symptoms_frame, text=symptoms_list[i], font=("Courier New Bold", 10), variable=numt[i], onvalue=1, offvalue=0, anchor='w', bg='white')
        b.place(relx=0.61, rely=column4, relwidth=0.19, height=16)
        changeOnHover(b, '#82EEFD', 'white')
        column4 = column4 + 0.032
    if 119 < i <= 149:
        if i == len(symptoms_list):
            break
        b = Checkbutton(symptoms_frame, text=symptoms_list[i], font=("Courier New Bold", 11), variable=numt[i], onvalue=1, offvalue=0, anchor='w', bg='white')
        b.place(relx=0.81, rely=column5, relwidth=0.19, height=16)
        changeOnHover(b, '#82EEFD', 'white')
        column5 = column5 + 0.032

    i = i + 1


def predict():
    x = []
    k = 0
    while k < len(symptoms_list):
        x.append(numt[k].get())
        k = k + 1

    patient_symptoms = [x]
    predictions = common_disease_model.predict(patient_symptoms)  # Make Preadiction
    print(predictions)
    Label(Common_Disease_page, text=f'{predictions}', font=("Courier New Bold", 13), fg='brown', anchor='w', bg='white').place(relx=0.82, rely=0.75, relwidth=0.34, relheight=0.05)


selected_symptoms_Frame = LabelFrame(Common_Disease_page, text='Patient Sysmptoms', bg='white')
selected_symptoms_Frame.place(x=10, rely=0.74, relwidth=0.67, relheight=0.25)


def sym_display():
    k = 0
    column_1 = column_2 = column_3 = 0.1
    loop = 0

    while k < 132 and loop < 21:
        if numt[k].get() == 1:
            if loop < 7:
                vv = Label(selected_symptoms_Frame, text=symptoms_list[k], bg='white', fg='red', font=("Courier New Bold", 10), anchor='w')
                vv.place(relheight=0.1, relwidth=0.3, relx=0.02, rely=column_1)
                vv.after(1000, vv.destroy)
                column_1 = column_1 + 0.12

            if 14 > loop >= 7:
                bb = Label(selected_symptoms_Frame, text=symptoms_list[k], bg='white', fg='red', font=("Courier New Bold", 10), anchor='w')
                bb.place(relheight=0.1, relwidth=0.3, relx=0.35, rely=column_2)
                bb.after(1000, bb.destroy)
                column_2 = column_2 + 0.12

            if 21 > loop >= 14:
                bc = Label(selected_symptoms_Frame, text=symptoms_list[k], bg='white', fg='red', font=("Courier New Bold", 10), anchor='w')
                bc.place(relheight=0.1, relwidth=0.3, relx=0.68, rely=column_3)
                bc.after(1000, bc.destroy)
                column_3 = column_3 + 0.12

            loop = loop + 1
        k = k + 1
    selected_symptoms_Frame.after(1000, sym_display)


sym_display()

Label(Common_Disease_page, text=f'PROGNOSIS:', font=("Courier New Bold", 12), anchor='w', bg='white').place(relx=0.7, rely=0.75, relwidth=0.132, relheight=0.05)

heart_dioagnosis = Button(Common_Disease_page, text='predict', font=("Courier New Bold", 12), command=lambda: predict(), bg='gray')
heart_dioagnosis.place(relx=0.7, rely=0.85, relwidth=0.3)
changeOnHover(heart_dioagnosis, 'Green', 'gray')
Button(Common_Disease_page, text='refresh', font=("Courier New Bold", 12), command=lambda: sym_display()).place(relx=0.7, rely=0.9, relwidth=0.3)

#  ========================= project_information_page   =================================================================================================================================================================================================
Label(project_information_page, bg='white', text='DISEASE PREDICTION (category Machine Learning)', fg='Brown', font=("Arial Bold", 12)).place(relx=0.05, rely=0.0, relwidth=0.9, relheight=0.03)

Label(project_information_page, bg='white', text='PROJECT MEMBERS', fg='Brown', anchor='w', font=("Courier New Bold", 12)).place(relx=0.05, rely=0.04, relwidth=0.9, relheight=0.03)
Label(project_information_page, bg='white', text='1: P15/136414/2019	  Nangulu Hezron Wekesa  	  hezron.w12@students.uonbi.ac.ke', anchor='w', font=("Courier New Bold", 12)).place(relx=0.05, rely=0.08, relwidth=0.9, relheight=0.03)
Label(project_information_page, bg='white', text='2: P15/139974/2020	  Angela Mawia	              angelmawia01@students.uonbi.ac.ke', anchor='w', font=("Courier New Bold", 12)).place(relx=0.05, rely=0.12, relwidth=0.9, relheight=0.03)
Label(project_information_page, bg='white', text='3: P15/141268/2020	  Purity Jangaya	        purityjangaya@students.uonbi.ac.ke	', anchor='w', font=("Courier New Bold", 12)).place(relx=0.05, rely=0.16, relwidth=0.9, relheight=0.03)
Label(project_information_page, bg='white', text='4: P15/140597/2020	  Kuir Elijah Ajak	        ajakkuir123@students.uonbi.ac.ke', anchor='w', font=("Courier New Bold", 12)).place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.03)


#  ========================= Heart_disease_page   ======================================================================================================================================================================================================
def predict_heart_disease():
    x = []
    k = 0
    while k < 13:
        x.append(Heart_Patient_symptoms[k].get())
        k = k + 1
    try:
        Heart_Disease_patient_symptoms_input = [x]
        predictions = heart_disease_model.predict(Heart_Disease_patient_symptoms_input)  # Make Preadiction
        if predictions == ['0']:
            display = '[negative] No Heart Disease'
        else:
            display = '[positive] No Heart Disease'
        Label(Heart_disease_page, bg='white', text=f'{display}', anchor='w', font=("Courier New Bold", 12)).place(relx=0.61, rely=0.59, relwidth=0.37, relheight=0.05)
    except:
        Label(Heart_disease_page, bg='white', fg='red', text='Please Fill All Entry', font=("Courier New Bold", 12)).place(relx=0.61, rely=0.59, relwidth=0.37, relheight=0.05)


Heart_Patient_symptoms = []
H_S = 0
while H_S < 13:
    Heart_Patient_symptoms.append(H_S)
    Heart_Patient_symptoms[H_S] = StringVar()
    H_S = H_S + 1

Label(Heart_disease_page, bg='white', fg='blue', text='Patient Details', anchor='w', font=("Courier New Bold", 13)).place(relx=0.1, rely=0.05, relwidth=0.4, relheight=0.04)

Label(Heart_disease_page, bg='white', text='age', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.03)
E1 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[0], font=("Courier New Bold", 12))
E1.place(relx=0.61, rely=0.1, relwidth=0.3, relheight=0.03)
changeOnHover(E1, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='sex', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.135, relwidth=0.5, relheight=0.03)
E2 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[1], font=("Courier New Bold", 12))
E2.place(relx=0.61, rely=0.135, relwidth=0.3, relheight=0.03)
changeOnHover(E2, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='chest pain type (4 values)', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.17, relwidth=0.5, relheight=0.03)
E3 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[2], font=("Courier New Bold", 12))
E3.place(relx=0.61, rely=0.17, relwidth=0.3, relheight=0.03)
changeOnHover(E3, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='resting blood pressure', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.205, relwidth=0.5, relheight=0.03)
E4 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[3], font=("Courier New Bold", 12))
E4.place(relx=0.61, rely=0.205, relwidth=0.3, relheight=0.03)
changeOnHover(E4, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='serum cholestoral in mg/dl', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.24, relwidth=0.5, relheight=0.03)
E5 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[4], font=("Courier New Bold", 12))
E5.place(relx=0.61, rely=0.24, relwidth=0.3, relheight=0.03)
changeOnHover(E5, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='fasting blood sugar > 120 mg/dl', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.275, relwidth=0.5, relheight=0.03)
E6 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[5], font=("Courier New Bold", 12))
E6.place(relx=0.61, rely=0.275, relwidth=0.3, relheight=0.03)
changeOnHover(E6, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='resting electrocardiographic results (values 0,1,2)', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.31, relwidth=0.5, relheight=0.03)
E7 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[6], font=("Courier New Bold", 12))
E7.place(relx=0.61, rely=0.31, relwidth=0.3, relheight=0.03)
changeOnHover(E7, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='maximum heart rate achieved', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.345, relwidth=0.5, relheight=0.03)
E8 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[7], font=("Courier New Bold", 12))
E8.place(relx=0.61, rely=0.345, relwidth=0.3, relheight=0.03)
changeOnHover(E8, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='exercise induced angina', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.38, relwidth=0.5, relheight=0.03)
E9 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[8], font=("Courier New Bold", 12))
E9.place(relx=0.61, rely=0.38, relwidth=0.3, relheight=0.03)
changeOnHover(E9, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='oldpeak = ST depression induced by exercise relative to rest', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.415, relwidth=0.5, relheight=0.03)
E10 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[9], font=("Courier New Bold", 12))
E10.place(relx=0.61, rely=0.415, relwidth=0.3, relheight=0.03)
changeOnHover(E10, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='the slope of the peak exercise ST segment', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.45, relwidth=0.5, relheight=0.03)
E11 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[10], font=("Courier New Bold", 12))
E11.place(relx=0.61, rely=0.45, relwidth=0.3, relheight=0.03)
changeOnHover(E11, '#DDBBB4', 'pink')
Label(Heart_disease_page, bg='white', text='number of major vessels (0-3) colored by flourosopy', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.485, relwidth=0.5, relheight=0.03)
E12 = Entry(Heart_disease_page, textvariable=Heart_Patient_symptoms[11], bg='pink', font=("Courier New Bold", 12))
E12.place(relx=0.61, rely=0.485, relwidth=0.3, relheight=0.03)
changeOnHover(E12, '#DDBBB4', 'pink')

Label(Heart_disease_page, bg='white', text='thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', anchor='w', font=("Courier New Bold", 12)).place(relx=0.1, rely=0.52, relwidth=0.5, relheight=0.03)
E13 = Entry(Heart_disease_page, bg='pink', textvariable=Heart_Patient_symptoms[12], font=("Courier New Bold", 12))
E13.place(relx=0.61, rely=0.52, relwidth=0.3, relheight=0.03)
changeOnHover(E13, '#DDBBB4', 'pink')

Label(Heart_disease_page, bg='white', text='Diagnosis', fg='Brown', anchor='e', font=("Courier New Bold", 14)).place(relx=0.1, rely=0.6, relwidth=0.5, relheight=0.03)

heart_D = Button(Heart_disease_page, text='predict', activebackground='#014421', borderwidth=1, activeforeground='white', font=("Courier New Bold", 12), command=lambda: predict_heart_disease(), bg='gray')
heart_D.place(relheight=0.05, relwidth=0.2, rely=0.7, relx=0.61)
changeOnHover(heart_D, 'green', 'pink')

root.mainloop()

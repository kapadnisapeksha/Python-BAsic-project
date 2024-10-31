#Apeksha Kapadnis
class DiseaseExpertSystem:
    def __init__(self):
        self.knowledge_base = {
           'Common Cold': ['runny nose', 'sneezing', 'sore throat', 'cough'],
            'Influenza': ['fever', 'body aches', 'fatigue', 'headache'],
            'Allergies': ['itchy eyes', 'sneezing', 'runny nose'],
            'COVID-19': ['fever', 'cough', 'shortness of breath'],
            'Migraine without Aura': ['throbbing headache', 'nausea', 'sensitivity to light'],
            'Migraine with Aura': ['visual disturbances', 'pins and needles sensation', 'speech difficulties'],
            'Heart Disease': ['chest pain', 'shortness of breath', 'fatigue'],
            'Asthma': ['wheezing', 'coughing', 'shortness of breath'],
            'Diabetes': ['frequent urination', 'increased thirst', 'unexplained weight loss'],
            'Hypertension': ['high blood pressure', 'headache', 'fatigue'],
            'Gastroenteritis': ['nausea', 'vomiting', 'diarrhea'],
            'Pneumonia': ['cough', 'fever', 'difficulty breathing'],
            'Urinary Tract Infection': ['frequent urination', 'burning sensation', 'cloudy urine'],
            'Sinusitis': ['facial pain', 'congestion', 'headache'],
            'Laryngitis': ['hoarseness', 'sore throat', 'difficulty speaking'],
            'Anemia': ['fatigue', 'weakness', 'pale skin'],
            'Appendicitis': ['abdominal pain', 'loss of appetite', 'nausea'],
            'Osteoarthritis': ['joint pain', 'stiffness', 'swelling'],
            'Gastritis': ['stomach pain', 'nausea', 'indigestion'],
            'Depression': ['persistent sadness', 'loss of interest', 'fatigue']
        }

    def predict_disease(self, symptoms):
        predicted_diseases = []
        for disease, disease_symptoms in self.knowledge_base.items():
            if all(symptom in symptoms for symptom in disease_symptoms):
                predicted_diseases.append(disease)

        return predicted_diseases


def run_expert_system():
    print("Welcome to the Disease Expert System!")
    print("Please provide some information:")

    age = input("Enter your age: ")
    gender = input("Enter your gender: ")

    expert_system = DiseaseExpertSystem()
    user_symptoms = input("Enter your symptoms (comma-separated): ").split(',')

    predicted_diseases = expert_system.predict_disease(user_symptoms)

    if 'Heart Disease' in predicted_diseases:
        bp = input("Enter your blood pressure (BP): ")
        sugar = input("Enter your sugar level: ")

        if int(bp) >= 140 or int(sugar) >= 200:
            predicted_diseases.remove('Heart Disease')

    if predicted_diseases:
        print("Predicted diseases:", predicted_diseases)
    else:
        print("No diseases found matching the provided symptoms.")

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'y':
        run_expert_system()
    else:
        print("Thank you for using the Disease Expert System. We hope you find it helpful!")


run_expert_system()

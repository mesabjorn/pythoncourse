#%%

class Patient:
    geboortedatum = ""
    patient_id = ""
    name = ""

    def __init__(self, id, name, geboortedatum):
        self.geboortedatum = geboortedatum
        self.patient_id = id
        self.name = name
        self.medicatie_lijst = []

    def __str__(self):
        return f"{self.patient_id} - {self.name} - {self.geboortedatum}"

    def add_medication(self, med):
        self.medicatie_lijst.append(med)

    def remove_medication(self, med):
        if(med in self.medicatie_lijst):
            ind = self.medicatie_lijst.index(med)
            del self.medicatie_lijst[ind]
        else:            
            print(f"Warning {med} not in patient's list.")

class PatientDatabase:
    PatientList = []

    def add_patient(self, patient):
        self.PatientList.append(patient)

    def __str__(self):
        return "Patient DB"

    def get_patient(self, zoekterm):

        for p in self.PatientList:
            if(p.patient_id==zoekterm):
                return p
    
    def get_patient_by_geboortedatum(self, zoekterm):        
        for p in self.PatientList:
            if(p.geboortedatum==zoekterm):
                return p    

P1 = Patient("000","de Vries","22-11-1988")
P2 = Patient("001","de Jong","01-03-1956")
P3 = Patient("002","Olde Riekerink","27-09-1974")

P1.add_medication("Oxazepam")
P1.add_medication("Aspirine")
P1.add_medication("Labetolol")

P2.add_medication("Aspirine")

P2.remove_medication("Oxazepam")
P1.remove_medication("Oxazepam")

DB = PatientDatabase()
DB.add_patient(P1)
DB.add_patient(P2)
DB.add_patient(P3)

for p in DB.PatientList:
    print(str(p))

result = DB.get_patient("000")
print(str(result))

result = DB.get_patient_by_geboortedatum("01-03-1956")
print(str(result))











# %%

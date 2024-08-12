from datetime import datetime
from typing import Union
class Dosage:
    def __init__(self):
        self.older_dosis = {"Ibuprofen":[],
                            "Paracetamol":[],
                            "Aspirin":[]}
    
    def daily_dosis(self,medikament:str) -> int:
        """Returns the daily dose of a given medication in mg."""
        #todo finde tägliche Dosis von Medikamenten
        if medikament == "Ibuprofen":
            return 1200
        elif medikament == "Paracetamol":
            return 4000
        elif medikament == "Aspirin":
            return 3000
        elif medikament == "Diclofenac":
            return 75
        elif medikament == "Naproxen":
            return 760
        elif medikament == "Novalgin":
            return 4000
        else:
            "Medikament nicht gefunden"
        
    def resource_medication(self,medikament:str) -> str:
        """Returns the resource of a given medication."""
        #todo finde Ressource von Medikamenten
        if medikament == "Ibuprofen":
            return "https://www.gelbeseiten.de/ratgeber/gl/ibuprofen-hoechstdosis-ibuprofen-richtig-dosieren"
        elif medikament == "Paracetamol":
            return "https://www.gelbeseiten.de/ratgeber/gl/paracetamol-wirkung-anwendung-und-dosierung-des-schmerzmittels"
        elif medikament == "Aspirin":
            return "https://www.gelbeseiten.de/ratgeber/gl/schmerzmittel-aspirin-wirkung-anwendung-und-dosierung-von-acetylsalicylsaeure"
        elif medikament == "Diclofenac":
            return "https://www.gelbeseiten.de/ratgeber/gl/diclofenac-wirkung-anwendung-und-dosierung-des-schmerzmittels"
        elif medikament == "Naproxen":
            return "https://www.apotheken-umschau.de/medikamente/beipackzettel/naproxen-al-500-tabletten-4900350.html"
        elif medikament == "Novalgin":
            return "https://www.apotheken-umschau.de/medikamente/beipackzettel/novalgin-filmtabletten-731577.html#dosierung"
        else:
            return "Medikament nicht gefunden"
        

    def caculate_time_difference(self,current_time: datetime.time, old_time: Union[datetime.time, str]) -> float:

        if type(old_time) == str:
            time1 = datetime.strptime(old_time, "%H:%M").replace(year=current_time.year, month=current_time.month, day=current_time.day)
        else:
            time1 = old_time
        # Calculate the difference
        time_difference = current_time - time1
        # Convert the difference to total seconds
        total_seconds = time_difference.total_seconds()

        # Convert seconds to hours (as a float)
        hours_difference = total_seconds / 3600
        # Round the hours difference to 2 decimal places
        return round(hours_difference, 2)

    def caculate_older_dosis(self,medikamnet:str, old_dosis_interface = int) -> int:
        current_time = datetime.now()
        old_dosis_list = self.older_dosis[medikamnet]
        old_dosis = 0 + old_dosis_interface
        if len(old_dosis_list) > 0:
            for count,dose in enumerate(old_dosis_list):
                if self.caculate_time_difference(current_time, dose["time"]) > 24:
                    del old_dosis_list[count]
                else: 
                    old_dosis += dose["dosage"]
        self.older_dosis[medikamnet] = old_dosis_list
        return old_dosis

    def add_old_dosis(self, medikament:str, current_dosis:int, time:str| None =None):
        if time is None:
            time = datetime.now()
        doses = {"time": time,"dosage": current_dosis }
        self.older_dosis[medikament].append(doses)


    def remaining_dosis(self,medikament:str, dosis:int, old_dosis: int = 0, time:str| None =None) -> int:
        """Returns the remaining dose of a given medication in mg."""
        daily_dosis_mg = self.daily_dosis(medikament)
        current_old_dosis = self.caculate_older_dosis(medikament, old_dosis)
        remaining_dosis = daily_dosis_mg - dosis - current_old_dosis
        self.add_old_dosis(medikament=medikament, current_dosis=dosis, time=time)
        return remaining_dosis

import streamlit as st
from daily_dosis import Dosage

def main():
    st.title("Schmerzmittelrechner")

    medication = st.selectbox("Medikament:", ["Ibuprofen", "Paracetamol", "Aspirin"], index = 0)
    current_dose = int(st.number_input("Aktuelle Dosis (in mg)", min_value=0, max_value= 1000, step = 100))
    taken = st.checkbox("Bereits Medikamente eingenommen? ")
    if taken:
        already_taken = int(st.number_input("Bereits eingenommene Menge (in mg)", min_value=0, max_value= 1000, step = 100))
        time_already_taken = st.time_input("Bereits vergangene Zeit (in Stunden und Minuten)", value = None)
    else:
        already_taken = 0
        time_already_taken = None
    if st.button("Berechnen"):
        daily_dose_calculator = Dosage()
        daily_dose = daily_dose_calculator.remaining_dosis( medikament= medication, dosis=
            current_dose, old_dosis= already_taken, time= time_already_taken)
        st.write(f"Die empfohlene Tagesdosis beträgt: {daily_dose} mg")

if __name__ == "__main__":
    main()

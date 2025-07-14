#life_parameters.py

# How long have you lived so far

import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

class AgeCalculator:
    def __init__(self, birthdate):
        self.birthdate = birthdate

    def calculate_life_details(self):
        current_date = datetime.now()
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d")
        
        delta = current_date - birth_date
        
        years = relativedelta(current_date, birth_date).years
        months = relativedelta(current_date, birth_date).months
        weeks = delta.days // 7
        days = delta.days % 7
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        seconds = delta.seconds % 60
        
        return years, months, weeks, days, hours, minutes, seconds

def main():
    st.title("Life Details Calculator")
    
    birthdate = st.text_input("Enter your birthdate (YYYY-MM-DD):")
    
    if birthdate:
        try:
            age_calculator = AgeCalculator(birthdate)
            years, months, weeks, days, hours, minutes, seconds = age_calculator.calculate_life_details()
            
            st.markdown(
                f"""
                <div style='font-size:20px; color:green;'>
                    You have lived for:
                    <ul>
                        <li>{years} years</li>
                        <li>{months} months</li>
                        <li>{weeks} weeks</li>
                        <li>{days} days</li>
                        <li>{hours} hours</li>
                        <li>{minutes} minutes</li>
                        <li>{seconds} seconds</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        except ValueError:
            st.error("Please enter a valid date in the format YYYY-MM-DD.")

if __name__ == "__main__":
    main()

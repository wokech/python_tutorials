#days_lived_web_app.py

# Streamlit version

import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

class AgeCalculator:
    def __init__(self, birthdate):
        self.birthdate = birthdate

    def calculate_days_lived(self):
        current_date = datetime.now()
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d")
        delta = current_date - birth_date
        return delta.days

    def convert_days_to_units(self, days):
        weeks = days / 7
        years = days / 365.25  # considering leap years
        months = days / 30.44  # average days in a month
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        return weeks, years, months, hours, minutes, seconds

def main():
    st.title("Days Lived Calculator")
    
    birthdate = st.text_input("Enter your birthdate (YYYY-MM-DD):")
    
    if birthdate:
        try:
            age_calculator = AgeCalculator(birthdate)
            days_lived = age_calculator.calculate_days_lived()
            weeks, years, months, hours, minutes, seconds = age_calculator.convert_days_to_units(days_lived)
            
            st.markdown(
                f"""
                <div style='font-size:20px; color:green;'>
                    <p>You have lived for:</p>
                    <ul>
                        <li>{days_lived} days</li>
                        <li>{weeks:.2f} weeks</li>
                        <li>{years:.2f} years</li>
                        <li>{months:.2f} months</li>
                        <li>{hours:.2f} hours</li>
                        <li>{minutes:.2f} minutes</li>
                        <li>{seconds:.2f} seconds</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        except ValueError:
            st.error("Please enter a valid date in the format YYYY-MM-DD.")

if __name__ == "__main__":
    main()

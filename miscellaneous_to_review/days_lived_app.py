#days_lived.py

# Import the datetime module from the standard Python library to handle dates and times.
from datetime import datetime

# Define a class named AgeCalculator which will contain methods to calculate the number of days lived based on the birthdate.
class AgeCalculator:
    # Define the __init__ method, which is the constructor for the class. 
    # This method initializes an instance of the class with the provided birthdate.
    def __init__(self, birthdate):
        # Initialize the class with the birthdate attribute
        # Assign the birthdate parameter to the instance variable self.birthdate 
        # so that it can be used in other methods within the class.
        self.birthdate = birthdate

    # Define a method named calculate_days_lived within the AgeCalculator class. 
    # This method will calculate the number of days lived from the birthdate to 
    # the current date.
    def calculate_days_lived(self):
        # Calculate the number of days lived
        # Get the current date and time using datetime.now() 
        # and store it in the variable current_date.
        current_date = datetime.now()
        # Convert the birthdate string into a datetime object using datetime.strptime. 
        # The format "%Y-%m-%d" specifies that the date is in the format "YYYY-MM-DD".
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d")
        # Calculate the difference between the current date and the birthdate, 
        # resulting in a timedelta object which represents the difference in time.
        delta = current_date - birth_date
        # Return the number of days from the timedelta object using the days attribute.
        return delta.days

# Define the main function of the script which will be executed when the script runs.
def main():
    # Get birthdate input from user
    # Prompt the user to enter their birthdate in the format "YYYY-MM-DD" 
    # and store the input in the birthdate variable.

    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    
    # Create an instance of AgeCalculator
    # Create an instance of the AgeCalculator class with the provided birthdate.
    age_calculator = AgeCalculator(birthdate)
    
    # Calculate days lived
    # Call the calculate_days_lived method on the age_calculator instance to 
    # compute the number of days lived and store the result in the days_lived variable.
    days_lived = age_calculator.calculate_days_lived()
    
    # Print the result
    # Print the number of days lived using an f-string to format the output.
    print(f"You have lived for {days_lived} days.")

# Ensure that the main function is called only when the script is run directly 
# (not when it is imported as a module in another script).
# Call the main function to start the program.
if __name__ == "__main__":
    main()

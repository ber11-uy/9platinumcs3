

# FA2 - Hospital Billing System
# Name: Amber Gail C. Uy
# Section: 9-Platinum


class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = 0
        self.set_bill_amount(bill_amount)

    # Getters
    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        if (isinstance(bill_amount, (int, float))
                and not isinstance(bill_amount, bool)
                and bill_amount >= 0):
            self.__bill_amount = bill_amount
        else:
            raise ValueError("The bill amount must be a non-negative number.")

    # Calculates the full bill for regular patients
    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    # Overrides calculate_bill() with a 20% discount
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    # Overrides calculate_bill() with a 15% discount
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


# Create one object for each patient type
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)


# Display billing information
print("Hospital Billing System")
print("-----------------------")

print("\nPatient Name: ", regular_patient.get_name())
print("Original Bill: ₱{:,.2f}".format(regular_patient.get_bill_amount()))
print("Final Bill: ₱{:,.2f}".format(regular_patient.calculate_bill()))
print()

print("Patient Name: ", senior_patient.get_name())
print("Original Bill: ₱{:,.2f}".format(senior_patient.get_bill_amount()))
print("Final Bill: ₱{:,.2f}".format(senior_patient.calculate_bill()))
print()

print("Patient Name: ", philhealth_patient.get_name())
print("Original Bill: ₱{:,.2f}".format(philhealth_patient.get_bill_amount()))
print("Final Bill: ₱{:,.2f}".format(philhealth_patient.calculate_bill()))



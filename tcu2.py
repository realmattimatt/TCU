import random
import sys


class PatientManagement:
    def __init__(self):
        self.patient_id_list = []
        self.patient_message = []
        self.staff_password = "password123"

    def main(self):
        while True:
            choice = input("Enter 'a' to add a patient, 'c' to mark a message as completed, 'm' to message staff, 'p' to view patients, 'r' to remove a patient, 'v' to view patient messages, or 'q' to quit: ").lower()

            if choice == "a":
                patient_id = self.get_patient_id()
                patient_info = self.get_patient_info()

                while patient_id in self.patient_id_list:
                    patient_id = self.get_patient_id()

                self.add_patient(patient_id, patient_info)

                x = (patient_id,) + patient_info
                print("Patient added:", x)

            elif choice == 'c':
                password = input("Enter the staff password: ")
                if password == self.staff_password:
                    message_index = int(input("Enter the index of the message to mark as completed: "))
                    if message_index >= 0 and message_index < len(self.patient_message):
                        self.patient_message[message_index] = (*self.patient_message[message_index][:2], True)
                        print("Message marked as completed.")
                    else:
                        print("Invalid message index.")
                else:
                    print("Incorrect password. Access denied.")

            elif choice == 'm':
                patient_id = int(input("Enter the patient ID to send a message: "))
                if self.validate_patient_id(patient_id):
                    message = input("What is your message to the staff? ")
                    self.send_message(patient_id, message, False)
                    print("Message sent successfully.")
                else:
                    print("Invalid patient ID. Please try again.")

            elif choice == 'p':
                self.display_patients()

            elif choice == 'r':
                patient_id = int(input("Enter the patient ID to remove: "))
                if self.remove_patient(patient_id):
                    print("Patient removed successfully.")
                else:
                    print("Patient not found.")

            elif choice == 'v':
                password = input("Enter the staff password: ")
                if password == self.staff_password:
                    print("Patient Messages:")
                    for i, message in enumerate(self.patient_message):
                        patient_id, msg, status = message
                        print("Index:", i)
                        print("Patient ID:", patient_id)
                        print("Message:", msg)
                        print("Status:", "Completed" if status else "Not Completed")
                        print("--------------------")
                else:
                    print("Incorrect password. Access denied.")

            elif choice == 'q':
                sys.exit("Exiting the program.")

            else:
                print("Invalid choice. Please try again.")


    def get_patient_info(self):
        last_name = input("Last name: ").title()
        first_name = input("First name: ").title()
        while True:
            age_input = input("Age: ")
            if not age_input.isdigit():
                print("Invalid age. Please enter a valid integer.")
                continue

            age = int(age_input)
            if age < 0:
                print("Invalid age. Age must be a positive number.")
            else:
                break

        while True:
            gender = input("Gender at Birth (Male/Female): ").title()
            if gender in ["Male", "Female"]:
                break
            else:
                print("Invalid gender. Please enter either 'Male' or 'Female'.")

        return last_name, first_name, age, gender


    def get_patient_id(self):
        id = random.randrange(1000, 10000)
        return id


    def add_patient(self, patient_id, patient_info):
        self.patient_id_list.append((patient_id, patient_info))


    def remove_patient(self, patient_id):
        for index, (pid, _) in enumerate(self.patient_id_list):
            if pid == patient_id:
                del self.patient_id_list[index]
                return True
        return False


    def send_message(self, patient_id, message, status):
        self.patient_message.append((patient_id, message, status))


    def display_patients(self):
        password = input("Enter the staff password: ")
        if password == self.staff_password:
            print()
            print("Patients:")
            print("------------------------------------------------------------")
            print("| Patient ID | Last Name | First Name | Age | Gender       |")
            print("------------------------------------------------------------")
            for patient in self.patient_id_list:
                patient_id, patient_info = patient
                last_name, first_name, age, gender = patient_info
                print(f"| {patient_id:<10} | {last_name:<9} | {first_name:<10} | {age:<3} | {gender:<12} |")
            print("------------------------------------------------------------")
        else:
            print("Incorrect password. Access denied.")


    def validate_patient_id(self, patient_id):
        return any(pid == patient_id for pid, _ in self.patient_id_list)


if __name__ == "__main__":
    pm = PatientManagement()
    pm.main()

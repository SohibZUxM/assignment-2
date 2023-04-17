class DentalCompany:
    def __init__(self, company): #constructing the class
        #setting attributes
        self.__company = company
        self.__branches = []
        #getting the name
    def get_name(self):
        return self.__company
        #function to add the branch to the list of branches
    def add_branch(self, branch):
        self.__branches.append(branch)
        #getting an attribute
    def get_branches(self):
        return self.__branches

class Branch:
    def __init__(self, address, phoneNumber, manager): #constructing the class
        #setting attributes
        self.__address = address
        self.__phone_number = phoneNumber
        self.__manager = manager
        self.__services = []
        self.__staff = []
        self.__patients = []
    #function to add the service to the list of services
    def add_service(self, service):
        self.__services.append(service)
    #function to add the staff to the list of staff
    def add_staff(self, staff):
        self.__staff.append(staff)
    #function to add the patient to the list of patients
    def add_patient(self, patient):
        self.__patients.append(patient)
    #function to display the services that patient requested for
    def display_services(self):
        print("Services offered:")
        #loopin over the services list and printing them 
        for service in self.__services:
            print(f"- {service.getName()} (${service.getCost()})")
    #showing the staff name and its role
    def display_staff(self):
        print("Staff members:")
        for staff in self.__staff:
            print(f"- {staff.getName()} ({staff.getRole()})")
    #function to show the patient information
    def display_patients(self):
        print("Patients:")
        for patient in self.__patients:
            print(f"- {patient.getName()}")
    # function to show the booked services
    def book_appointment(self, patient, service):
        print(f"{patient.getName()} has booked a {service.getName()} appointment on the branch {self.__address}")
    # function to show the final results of the service with its price including VAT and service names
    def checkout(self, patient):
        total_cost = 0
        #patients name on receipt
        print(f"Receipt for {patient.getName()}:")
        for service in patient.getServiceReceived():
            print(f"- {service.getName()} (${service.getCost()})")
            #adding all the cost of the services
            total_cost += service.getCost()
        #adding the VAT of the cost
        vat = total_cost * 0.05
        #final amount
        total_cost += vat
        print(f"Total: ${total_cost} (including 5% VAT)")

class Service:
    def __init__(self, name, cost): #constructing the class
        #setting attributes
        self.__name = name
        self.__cost = cost
        #getting attributes
    def getName(self):
        return self.__name
    
    def getCost(self):
        return self.__cost
    
class Staff:
    def __init__(self, name, role): #constructing the class
        #setting attributes
        self.__name = name
        self.__role = role
    #getting attributes
    def getName(self):
        return self.__name
    
    def getRole(self):
        return self.__role

class Patient:
    def __init__(self, name): #constructing the class
        #setting attributes
        self.__name = name
        self.__services_received = []
    # adding the service to the service list
    def receive_service(self, service):
        self.__services_received.append(service)
    #getting attributes
    def getName(self):
        return self.__name
    
    def getServiceReceived(self):
        return self.__services_received
    
class Manager(Staff):
    def __init__(self, name,role): #constructing the class
        #inheriting from Staff class
        super().__init__(name, role)
    #the manager can hire and the function adds the hired person to the staff list of the branch
    def manage_staff(self, action, branch, member=None):
        if action == 'hire':
            if member is not None:
                branch.add_staff(member)
            else:
                print("No one was hired")

class Receptionist(Staff):
    def __init__(self, name, role): #constructing the class
        #inheriting from Staff class
        super().__init__(name, role)
    # booking an appointment and showing its information
    def book_appointment(self, patient, service, branch):
        print(f"{self.__name} has booked a {service.getName()} appointment for {patient.getName()} at {branch.__address}")
        #patient has been added to the registration book of the Branch
        branch.add_patient(patient)
    #getting attributes
    def getName(self):
        return self.__name
    
class Appointment:
    def __init__(self, patient, service, dateTime): #constructing the class
        #setting attributes
        self.__patient = patient
        self.__service = service
        self.__dateTime = dateTime

# Test case 1: adding branches
company = DentalCompany('MagicDent')
branch1 = Branch("17 Sad Street", "658982", "Dr. Tom")
branch2 = Branch("32 Outside", "9842312", "Dr. Jerry")
company.add_branch(branch1)
company.add_branch(branch2)
# Test case 2: adding services, staff, and patients to a branch
cleaning = Service("Cleaning", 50)
implants = Service("Implants", 1000)
receptionist = Staff("Sarah", "Receptionist")
dentist = Staff("Dr. Lee", "Dentist")
patient1 = Patient("Max")
patient2 = Patient("Mark")
branch1.add_service(cleaning)
branch1.add_service(implants)
branch1.add_staff(receptionist)
branch1.add_staff(dentist)
branch1.add_patient(patient1)
branch1.add_patient(patient2)

# Test case 3: adding a patient appointment
print(f"Welcome to {company.get_name()}")
branch1.book_appointment(patient1, cleaning)
print(f"Invoice is generated by {receptionist.getName()}")
# Test case 4: displaying receipt and final bill
patient1.receive_service(cleaning)
patient1.receive_service(implants)
branch1.checkout(patient1)

# Citizen class
class Citizen:
    """A citizen who can submit complaints. Stores minimal data only."""

    def __init__(self, citizen_id, alias, area):
        self.citizen_id = citizen_id   
        self.alias = alias             
        self.area = area              

    # Instance method
    def display_info(self):
        print("\n-------- Citizen Information ---------")
        print(f"ID:    {self.citizen_id}")
        print(f"Alias: {self.alias}")
        print(f"Area:  {self.area}")


    def submit_complaint(self, system, category, description):
        complaint = Complaint(
            system.generate_id(),
            self.citizen_id,
            category,
            description,
            self.area,
        )
        system.add_complaint(complaint)
        return complaint


    @classmethod
    def from_string(cls, data):
        citizen_id, alias, area = [part.strip() for part in data.split(",")]
        return cls(citizen_id, alias, area)


# Complaint class
class Complaint:
    categories = (
        "Waste Collection",
        "Road Damage",
        "Water Supply",
        "Street Lighting",
    )
    statuses = ("Pending", "In Progress", "Resolved")

    def __init__(self, complaint_id, citizen_id, category, description,
                 area, status="Pending"):
        if not Complaint.is_valid_category(category):
            raise ValueError(f"Invalid category: {category}")
        if status not in Complaint.statuses:
            raise ValueError(f"Invalid status: {status}")
        if not description.strip():
            raise ValueError("Description cannot be empty.")

        self.complaint_id = complaint_id
        self.citizen_id = citizen_id
        self.category = category
        self.description = description
        self.area = area
        self.status = status

    @staticmethod
    def is_valid_category(category):
        return category in Complaint.categories


    def update_status(self, new_status):
        if new_status not in Complaint.statuses:
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status
        print(f"Complaint {self.complaint_id} status updated to '{new_status}'.")


    def display_complaint(self):
        print("\n--------- Complaint Information ---------")
        print(f"Complaint ID: {self.complaint_id}")
        print(f"Citizen ID:   {self.citizen_id}")
        print(f"Category:     {self.category}")
        print(f"Description:  {self.description}")
        print(f"Area:         {self.area}")
        print(f"Status:       {self.status}")



## Complaint System class
class ComplaintSystem:

    def __init__(self, system_name):
        self.system_name = system_name
        self.complaints = {}    
        self.next_number = 1      

    def generate_id(self):
        complaint_id = f"CMP{self.next_number:03d}"
        self.next_number += 1
        return complaint_id

    def add_complaint(self, complaint):
        if complaint.complaint_id in self.complaints:
            raise ValueError(f"Complaint ID {complaint.complaint_id} already exists.")
        self.complaints[complaint.complaint_id] = complaint
        print(f"Complaint {complaint.complaint_id} added successfully.")

    def find_complaint(self, complaint_id):
        return self.complaints.get(complaint_id)

    def display_complaints(self):
        print(f"\n** {self.system_name}: All Complaints **")
        if len(self.complaints) == 0:
            print("No complaints found.")
        else:
            for complaint in self.complaints.values():
                complaint.display_complaint()

    def count_by_status(self):
        print(f"\n------- Summary ({len(self.complaints)} total) -------")
        for status in Complaint.statuses:
            count = sum(1 for c in self.complaints.values() if c.status == status)
            print(f"{status}: {count}")


# Demonstration
if __name__ == "__main__":

    citizen1 = Citizen("C101", "Saidu", "Kingtom")
    citizen2 = Citizen("C102", "Abu", "7Up")
    citizen3 = Citizen.from_string("C103, Yabom, Kissy")   

    citizen1.display_info()
    citizen2.display_info()
    citizen3.display_info()

    system = ComplaintSystem("Freetown Citizen Complaint System")


    print("\n-------- Submitting Complaints --------")
    c1 = citizen1.submit_complaint(system, "Waste Collection",
                                   "Rubbish has not been collected for two weeks.")
    c2 = citizen2.submit_complaint(system, "Road Damage",
                                   "Large pothole near the junction.")
    c3 = citizen3.submit_complaint(system, "Street Lighting",
                                   "Street light has been off for a week.")

    # 4. Update a status
    print("\n--------- Updating Status ---------")
    c1.update_status("In Progress")
    c2.update_status("Resolved")

    # 5. Find a record by ID
    print("\n---------- Find Complaint ----------")
    found = system.find_complaint("CMP002")
    if found:
        found.display_complaint()
    print("CMP999 found?", system.find_complaint("CMP999") is not None)


    print("\n--------- Static Method Test ---------")
    print("Is 'Road Damage' valid?", Complaint.is_valid_category("Road Damage"))
    print("Is 'Noise' valid?", Complaint.is_valid_category("Noise"))

    # 7. Error handling demonstrations
    print("\n--------- Error Handling Tests ---------")

    try:   # invalid category
        citizen1.submit_complaint(system, "Noise", "Too loud at night.")
    except ValueError as error:
        print(f"Error: {error}")

    try:
        c3.update_status("banana")
    except ValueError as error:
        print(f"Error: {error}")

    try:
        duplicate = Complaint("CMP001", "C102", "Water Supply",
                              "No water since Monday.", "7Up")
        system.add_complaint(duplicate)
    except ValueError as error:
        print(f"Error: {error}")

    try: 
        Complaint("CMP050", "C101", "Water Supply", "   ", "Kingtom")
    except ValueError as error:
        print(f"Error: {error}")

    # 8. Display everything
    system.display_complaints()
    system.count_by_status()
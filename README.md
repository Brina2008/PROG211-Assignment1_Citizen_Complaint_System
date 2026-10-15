# Citizen Complaint System

A Python program built with Object-Oriented Programming (OOP) that helps citizens report problems with public services and helps government officials track each complaint until it is resolved.

**Course:** PROG211 Object-Oriented Programming 1
**Institution:** Limkokwing University of Creative Technology, Sierra Leone
**Assignment:** Real-World Solutions under DPG Standards (Individual Assignment)
**Domain:** Government / Public Service
**Author:** *[Your name and student ID]*

---

## Table of Contents
1. [Problem Statement](#problem-statement)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Class Design](#class-design)
5. [OOP Concepts Demonstrated](#oop-concepts-demonstrated)
6. [Digital Public Goods (DPG) Alignment](#digital-public-goods-dpg-alignment)
7. [How to Run](#how-to-run)
8. [Example Usage](#example-usage)
9. [Sample Output](#sample-output)
10. [Future Improvements](#future-improvements)
11. [License](#license)

---

## Problem Statement
Citizens often have no simple, transparent way to report public service problems such as uncollected rubbish, damaged roads, water shortages or broken street lights. Officials, in turn, struggle to keep track of which problems are new, which are being worked on and which are finished.

This program provides a small, reusable system where citizens submit complaints and each complaint is tracked through clear stages: **Pending → In Progress → Resolved**.

## Features
- Citizens submit complaints in four categories: Waste Collection, Road Damage, Water Supply and Street Lighting.
- Complaint IDs are generated automatically (CMP001, CMP002, and so on).
- Each complaint moves through three statuses: Pending, In Progress and Resolved.
- Complaints can be found by ID, displayed in full and summarised by status.
- Input validation rejects invalid categories, invalid statuses, duplicate IDs and empty descriptions.
- Citizens can be created from a simple line of text, with no keyboard input needed.

## Project Structure
```
citizen-complaint-system/
├── citizen_complaint_system.py   # Source code (all classes + demonstration)
└── README.md                     # Documentation
```

## Class Design

### `Citizen`
Represents a person who submits complaints.

| Attribute | Description |
|-----------|-------------|
| `citizen_id` | Anonymous ID, e.g. `C101` |
| `alias` | First name or nickname only |
| `area` | Broad area or neighbourhood only |

| Method | Type | Purpose |
|--------|------|---------|
| `display_info()` | Instance | Prints the citizen's details |
| `submit_complaint(system, category, description)` | Instance | Creates a complaint and files it in the system |
| `from_string(data)` | **Class method** | Creates a citizen from text such as `"C103, Yabom, Kissy"` |

### `Complaint`
Represents one reported problem.

| Attribute | Description |
|-----------|-------------|
| `complaint_id` | Unique ID, e.g. `CMP001` |
| `citizen_id` | Links the complaint to the citizen who filed it |
| `category` | One of the valid categories |
| `description` | What the problem is |
| `area` | Where the problem is |
| `status` | Pending, In Progress or Resolved |

| Class attribute | Type | Purpose |
|-----------------|------|---------|
| `categories` | **Tuple** | Fixed list of valid categories |
| `statuses` | **Tuple** | Fixed list of valid statuses |

| Method | Type | Purpose |
|--------|------|---------|
| `update_status(new_status)` | Instance | Changes the status after validating it |
| `display_complaint()` | Instance | Prints the complaint's details |
| `is_valid_category(category)` | **Static method** | Checks a category without needing an object |

### `ComplaintSystem`
Manages all complaints using **one data structure**: a dictionary of `{complaint_id: Complaint object}`.

| Method | Purpose |
|--------|---------|
| `generate_id()` | Produces the next complaint ID |
| `add_complaint(complaint)` | Stores a complaint and blocks duplicate IDs |
| `find_complaint(complaint_id)` | Looks up a complaint by ID (returns `None` if missing) |
| `display_complaints()` | Prints every complaint |
| `count_by_status()` | Prints a summary of complaints per status |

### How the objects interact
When a citizen calls `submit_complaint()`, the method creates a `Complaint` using the citizen's own ID and area, asks the `ComplaintSystem` for a new complaint ID, and adds the complaint to the system's dictionary. A complaint is linked back to its citizen only through `citizen_id`, so the classes stay loosely coupled.

## OOP Concepts Demonstrated
- **Classes and objects:** three classes with several objects created from them
- **Attributes and methods:** each class has its own data and behaviour
- **Instance methods:** `display_info()`, `update_status()`, `submit_complaint()` and others
- **Class method:** `Citizen.from_string()`, an alternative constructor
- **Static method:** `Complaint.is_valid_category()`, a utility function
- **Data structures:** a dictionary for storage, plus tuples for fixed values
- **Validation:** invalid data is rejected when an object is created or updated
- **Error handling:** `try/except` blocks catch `ValueError` cases

## Digital Public Goods (DPG) Alignment

| DPG Principle | How this project meets it |
|---------------|---------------------------|
| **Open-source** | The full source code is published on GitHub for anyone to read, use, adapt and improve. |
| **Inclusive and accessible** | Messages are in plain language, and the program runs on any computer with Python, with no special hardware, accounts or internet connection needed. |
| **Privacy-respecting** | Only an anonymous citizen ID, a first name or alias, and a broad area are stored. The system deliberately does **not** store phone numbers, home addresses, national ID numbers or any other sensitive personal data. |
| **Modular and reusable** | Each class has a single responsibility and can be reused alone. The demonstration code sits under `if __name__ == "__main__":`, so the classes can be imported into other projects. Categories and statuses are defined in one place, so other services (for example permits or health clinics) can adapt them easily. |

## How to Run

**Requirements:** Python 3.6 or later (no external libraries needed).

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/citizen-complaint-system.git

# 2. Move into the folder
cd citizen-complaint-system

# 3. Run the program
python citizen_complaint_system.py
```

## Example Usage

```python
from citizen_complaint_system import Citizen, ComplaintSystem

# Create the system and a citizen (using the class method)
system = ComplaintSystem("Freetown Citizen Complaint System")
citizen = Citizen.from_string("C104, Mariama, Wellington")

# The citizen submits a complaint
complaint = citizen.submit_complaint(
    system, "Water Supply", "No water in our street since Monday."
)

# An official updates the status
complaint.update_status("In Progress")

# Look it up and show a summary
system.find_complaint("CMP001").display_complaint()
system.count_by_status()
```

## Sample Output

Running `python citizen_complaint_system.py` produces:

```
--------- Citizen Information ----------
ID:    C101
Alias: Saidu
Area:  Kingtom

--------- Citizen Information ----------
ID:    C102
Alias: Abu
Area:  Congo Town

--------- Citizen Information ----------
ID:    C103
Alias: Yabom
Area:  Kissy

---------- Submitting Complaints ----------
Complaint CMP001 added successfully.
Complaint CMP002 added successfully.
Complaint CMP003 added successfully.

---------- Updating Status ----------
Complaint CMP001 status updated to 'In Progress'.
Complaint CMP002 status updated to 'Resolved'.

---------- Find Complaint ----------

---------- Complaint Information ----------
Complaint ID: CMP002
Citizen ID:   C102
Category:     Road Damage
Description:  Large pothole near the junction.
Area:         Congo Town
Status:       Resolved
CMP999 found? False

---------- Static Method Test ----------
Is 'Road Damage' valid? True
Is 'Noise' valid? False

---------- Error Handling Tests ----------
Error: Invalid category: Noise
Error: Invalid status: banana
Error: Complaint ID CMP001 already exists.
Error: Description cannot be empty.

***** Freetown Citizen Complaint System: All Complaints *****

---------- Complaint Information ----------
Complaint ID: CMP001
Citizen ID:   C101
Category:     Waste Collection
Description:  Rubbish has not been collected for two weeks.
Area:         Kingtom
Status:       In Progress

---------- Complaint Information ----------
Complaint ID: CMP002
Citizen ID:   C102
Category:     Road Damage
Description:  Large pothole near the junction.
Area:         Congo Town
Status:       Resolved

---------- Complaint Information ----------
Complaint ID: CMP003
Citizen ID:   C103
Category:     Street Lighting
Description:  Street light has been off for a week.
Area:         Kissy
Status:       Pending

---------- Summary (3 total) ----------
Pending: 1
In Progress: 1
Resolved: 1
```

## Future Improvements
- Save and load complaints from a file so data persists between runs
- Add a simple menu so users can interact without editing code
- Add more categories, such as Drainage and Public Health
- Add search and filtering by area or category
- Support multiple languages, such as Krio, to improve accessibility

## License
This project is released under the [MIT License](https://opensource.org/licenses/MIT) and is free to use, modify and share.

---
*Developed for PROG211 Object-Oriented Programming 1, Limkokwing University of Creative Technology, Sierra Leone.*
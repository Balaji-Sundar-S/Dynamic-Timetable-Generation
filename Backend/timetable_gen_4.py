import random
import time
from openpyxl import Workbook  # For Excel export

# Define constants
subjects_by_year = {
    "First Year": {
        "Engineering": {"Mathematics I": 4, "Physics I": 3, "Chemistry I": 3, "Programming Basics": 2, "English": 2},
        "Science": {"Mathematics I": 4, "Physics I": 3, "Chemistry I": 3, "Programming Basics": 2, "English": 2},
        "Arts": {"Mathematics I": 4, "Physics I": 3, "Chemistry I": 3, "Programming Basics": 2, "English": 2},
        "Commerce": {"Mathematics I": 4, "Physics I": 3, "Chemistry I": 3, "Programming Basics": 2, "English": 2},
        "Medicine": {"Mathematics I": 4, "Physics I": 3, "Chemistry I": 3, "Programming Basics": 2, "English": 2},
        "Law": {"Mathematics I": 4, "Physics I": 3, "Chemistry I": 3, "Programming Basics": 2, "English": 2}
    },
    "Second Year": {
        "Engineering": {"Mathematics II": 4, "Physics Lab": 2, "Chemistry Lab": 2, "Data Structures": 3, "Electronics": 3, "Thermodynamics": 3},
        "Science": {"Mathematics II": 4, "Biology Lab": 2, "Chemistry Lab": 2, "Environmental Science": 3, "Astrophysics": 3},
        "Arts": {"World History": 2, "Literature Analysis": 3, "Art Appreciation": 2, "Philosophy": 2, "Sociology": 3, "Modern Art": 2},
        "Commerce": {"Financial Accounting": 3, "Microeconomics": 3, "Business Statistics": 2, "Marketing": 3, "Finance": 3},
        "Medicine": {"Anatomy II": 4, "Biochemistry II": 3, "Physiology II": 3, "Pharmacology": 3, "Pathology": 3},
        "Law": {"Constitutional Law II": 3, "Criminal Law": 3, "Legal Writing": 2, "Corporate Law": 3}
    },
    "Third Year": {
        "Engineering": {"Advanced Mathematics": 4, "Machine Learning": 3, "Robotics": 3, "AI": 3, "Electrical Engineering": 3, "Mechanical Engineering": 3, "Capstone Project": 4},
        "Science": {"Quantum Mechanics": 3, "Astrophysics": 3, "Genetics": 3, "Biotechnology": 3, "Research Methods": 3, "Environmental Studies": 3, "Capstone Project": 4},
        "Arts": {"Creative Writing": 2, "Film Studies": 3, "Art History": 2, "Philosophy": 2, "Sociology": 3, "Modern Art": 2, "Capstone Project": 4},
        "Commerce": {"Strategic Management": 3, "Entrepreneurship": 3, "International Business": 3, "Economics": 3, "Finance": 3, "Capstone Project": 4},
        "Medicine": {"Surgery": 4, "Pediatrics": 3, "Internal Medicine": 3, "Radiology": 3, "Clinical Research": 3, "Capstone Project": 4, "Internship": 3},
        "Law": {"Judicial Internship": 3, "Corporate Law": 3, "Intellectual Property": 3, "Capstone Project": 4}
    },
    "Fourth Year": {
        "Engineering": {"Capstone Project": 4, "Internship": 3},
        "Science": {"Capstone Project": 4, "Internship": 3},
        "Arts": {"Capstone Project": 4, "Internship": 3},
        "Commerce": {"Capstone Project": 4, "Internship": 3},
        "Medicine": {"Capstone Project": 4, "Internship": 3},
        "Law": {"Capstone Project": 4, "Moot Court": 3}
    }
}

lab_subjects = ["Physics Lab", "Chemistry Lab", "Biology Lab", "Programming Lab"]

timeslots = ["9:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-1:00", "1:00-2:00", "2:00-3:00", "3:00-4:00"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
batches = ["First Year", "Second Year", "Third Year", "Fourth Year"]
departments = ["Engineering", "Science", "Arts", "Commerce", "Medicine", "Law"]
sections = [f"Section {i+1}" for i in range(3)]

# Multiple faculty members per subject
faculty = {
    "Mathematics I": ["Prof. A", "Prof. B"],
    "Physics I": ["Prof. E", "Prof. F"],
    "Chemistry I": ["Prof. G", "Prof. H"],
    "Programming Basics": ["Prof. I", "Prof. J"],
    "English": ["Prof. K", "Prof. L"],
    "Mathematics II": ["Prof. M", "Prof. N"],
    "Physics Lab": ["Prof. O", "Prof. P"],
    "Chemistry Lab": ["Prof. Q", "Prof. R"],
    "Data Structures": ["Prof. S", "Prof. T"],
    "Electronics": ["Prof. U", "Prof. V"],
    "Thermodynamics": ["Prof. W", "Prof. X"],
    "Biology Lab": ["Prof. Y", "Prof. Z"],
    "Art History":["Prof. K","Prof. L"],
    "Environmental Science": ["Prof. AA", "Prof. AB"],
    "Astrophysics": ["Prof. AC", "Prof. AD"],
    "World History": ["Prof. AE", "Prof. AF"],
    "Literature Analysis": ["Prof. AG", "Prof. AH"],
    "Art Appreciation": ["Prof. AI", "Prof. AJ"],
    "Philosophy": ["Prof. AK", "Prof. AL"],
    "Sociology": ["Prof. AM", "Prof. AN"],
    "Modern Art": ["Prof. AO", "Prof. AP"],
    "Financial Accounting": ["Prof. AQ", "Prof. AR"],
    "Microeconomics": ["Prof. AS", "Prof. AT"],
    "Business Statistics": ["Prof. AU", "Prof. AV"],
    "Marketing": ["Prof. AW", "Prof. AX"],
    "Finance": ["Prof. AY", "Prof. AZ"],
    "Anatomy II": ["Prof. BA", "Prof. BB"],
    "Biochemistry II": ["Prof. BC", "Prof. BD"],
    "Physiology II": ["Prof. BE", "Prof. BF"],
    "Pharmacology": ["Prof. BG", "Prof. BH"],
    "Pathology": ["Prof. BI", "Prof. BJ"],
    "Constitutional Law II": ["Prof. BK", "Prof. BL"],
    "Criminal Law": ["Prof. BM", "Prof. BN"],
    "Legal Writing": ["Prof. BO", "Prof. BP"],
    "Corporate Law": ["Prof. BQ", "Prof. BR"],
    "Advanced Mathematics": ["Prof. BS", "Prof. BT"],
    "Machine Learning": ["Prof. BU", "Prof. BV"],
    "Robotics": ["Prof. BW", "Prof. BX"],
    "AI": ["Prof. BY", "Prof. BZ"],
    "Electrical Engineering": ["Prof. CA", "Prof. CB"],
    "Mechanical Engineering": ["Prof. CC", "Prof. CD"],
    "Capstone Project": ["Prof. CE", "Prof. CF"],
    "Quantum Mechanics": ["Prof. CG", "Prof. CH"],
    "Genetics": ["Prof. CI", "Prof. CJ"],
    "Biotechnology": ["Prof. CK", "Prof. CL"],
    "Research Methods": ["Prof. CM", "Prof. CN"],
    "Environmental Studies": ["Prof. CO", "Prof. CP"],
    "Creative Writing": ["Prof. CQ", "Prof. CR"],
    "Film Studies": ["Prof. CS", "Prof. CT"],
    "Strategic Management": ["Prof. CU", "Prof. CV"],
    "Entrepreneurship": ["Prof. CW", "Prof. CX"],
    "International Business": ["Prof. CY", "Prof. CZ"],
    "Economics": ["Prof. DA", "Prof. DB"],
    "Surgery": ["Prof. DC", "Prof. DD"],
    "Pediatrics": ["Prof. DE", "Prof. DF"],
    "Internal Medicine": ["Prof. DG", "Prof. DH"],
    "Radiology": ["Prof. DI", "Prof. DJ"],
    "Clinical Research": ["Prof. DK", "Prof. DL"],
    "Internship": ["Prof. DM", "Prof. DN"],
    "Judicial Internship": ["Prof. DO", "Prof. DP"],
    "Intellectual Property": ["Prof. DQ", "Prof. DR"],
    "Moot Court": ["Prof. DS", "Prof. DT"]
}

# Faculty availability (example data)
all_faculty = set(sum(faculty.values(), []))  # Flatten the list of faculty members into a set
faculty_availability = {prof: days for prof in all_faculty}

class Timetable:
    def __init__(self):
        self.timetable = {
            batch: {
                department: {
                    section: {
                        day: {timeslot: {"subject": None, "faculty": None} for timeslot in timeslots} 
                        for day in days
                    } 
                    for section in sections
                } 
                for department in departments
            } 
            for batch in batches
        }
        self.faculty_consistency = {}  # Tracks (subject, section) -> faculty mappings

    def generate(self):
        for batch in batches:
            for department in departments:
                dept_subjects = subjects_by_year[batch][department]
                for section in sections:
                    weekly_schedule = self._generate_weekly_schedule(dept_subjects, section)
                    for day in days:
                        for timeslot in timeslots:
                            self.timetable[batch][department][section][day][timeslot] = weekly_schedule[day][timeslot]

    def _generate_weekly_schedule(self, dept_subjects, section):
        weekly_schedule = {day: {timeslot: {"subject": None, "faculty": None} for timeslot in timeslots} for day in days}
        remaining_credits = {subject: credits for subject, credits in dept_subjects.items()}

        # Track daily subject counts and faculty assignments
        daily_subject_counts = {day: {subject: 0 for subject in dept_subjects} for day in days}
        faculty_assignments = {day: {timeslot: {} for timeslot in timeslots} for day in days}

        # Fill all timeslots
        for day in days:
            for timeslot in timeslots:
                # Get valid subjects based on remaining credits and daily limits
                valid_subjects = [
                    subject for subject, credits in remaining_credits.items()
                    if credits > 0 and daily_subject_counts[day][subject] < 2
                ]

                # If no valid subjects remain, reuse completed subjects
                if not valid_subjects:
                    valid_subjects = list(dept_subjects.keys())

                # Filter out labs if lab hours exceed 3 for the day
                lab_hours_today = sum(1 for ts in timeslots if weekly_schedule[day][ts]["subject"] in lab_subjects)
                if lab_hours_today >= 3:
                    valid_subjects = [subject for subject in valid_subjects if subject not in lab_subjects]

                # Assign a subject
                subject = random.choice(valid_subjects)

                # Assign a faculty member
                if (subject, section) in self.faculty_consistency:
                    # Reuse the same faculty member for this subject-section pair
                    faculty_member = self.faculty_consistency[(subject, section)]
                else:
                    # Assign a new faculty member who hasn't already been assigned to this subject in another section
                    available_faculty = [prof for prof in faculty[subject] if prof not in faculty_assignments[day][timeslot].values()]
                    if available_faculty:
                        faculty_member = random.choice(available_faculty)
                    else:
                        faculty_member = random.choice(faculty[subject])  # Fallback if no unique faculty is available
                    
                    # Record the faculty assignment for this subject-section pair
                    self.faculty_consistency[(subject, section)] = faculty_member

                # Update schedule
                weekly_schedule[day][timeslot]["subject"] = subject
                weekly_schedule[day][timeslot]["faculty"] = faculty_member

                # Update daily subject count and faculty assignments
                daily_subject_counts[day][subject] += 1
                faculty_assignments[day][timeslot][subject] = faculty_member

                # Deduct credit only if the subject has remaining credits
                if remaining_credits[subject] > 0:
                    remaining_credits[subject] -= 1

        return weekly_schedule

    def fitness(self):
        score = 0
        for batch in batches:
            for department in departments:
                for section in sections:
                    for day in days:
                        lab_hours = 0
                        daily_subject_counts = {}
                        faculty_assignments = {}
                        for timeslot in timeslots:
                            entry = self.timetable[batch][department][section][day][timeslot]
                            subject = entry["subject"]
                            faculty_member = entry["faculty"]

                            # Check daily subject limit
                            if subject:
                                if subject in daily_subject_counts:
                                    daily_subject_counts[subject] += 1
                                    if daily_subject_counts[subject] > 2:
                                        score -= 1
                                else:
                                    daily_subject_counts[subject] = 1

                            # Check faculty consistency
                            if subject and faculty_member:
                                key = (subject, section)
                                if key in self.faculty_consistency:
                                    if faculty_member != self.faculty_consistency[key]:
                                        score -= 10  # Heavily penalize inconsistent faculty assignments
                                else:
                                    self.faculty_consistency[key] = faculty_member

                            # Check faculty availability
                            if faculty_member and day not in faculty_availability.get(faculty_member, []):
                                score -= 5  # Penalize unavailable faculty

                            # Check lab hours
                            if subject in lab_subjects:
                                lab_hours += 1
                                if lab_hours > 3:
                                    score -= 5  # Penalize exceeding lab hours

        return score


def create_population(size):
    return [Timetable() for _ in range(size)]


def crossover(parent1, parent2):
    child = Timetable()
    for batch in batches:
        for department in departments:
            for section in sections:
                for day in days:
                    for timeslot in timeslots:
                        if random.random() > 0.5:
                            entry = parent1.timetable[batch][department][section][day][timeslot]
                        else:
                            entry = parent2.timetable[batch][department][section][day][timeslot]

                        # Preserve faculty consistency
                        subject = entry["subject"]
                        faculty_member = entry["faculty"]
                        if subject and faculty_member:
                            key = (subject, section)
                            if key in child.faculty_consistency:
                                if child.faculty_consistency[key] != faculty_member:
                                    # Resolve inconsistency by reusing the existing faculty member
                                    faculty_member = child.faculty_consistency[key]
                            else:
                                child.faculty_consistency[key] = faculty_member

                        child.timetable[batch][department][section][day][timeslot] = {
                            "subject": subject,
                            "faculty": faculty_member
                        }
    return child

def mutate(timetable):
    batch = random.choice(batches)
    department = random.choice(departments)
    section = random.choice(sections)
    day = random.choice(days)
    timeslot = random.choice(timeslots)

    entry = timetable.timetable[batch][department][section][day][timeslot]
    subject = entry["subject"]

    if subject:
        # Mutate only if it doesn't break faculty consistency
        key = (subject, section)
        if key in timetable.faculty_consistency:
            faculty_member = timetable.faculty_consistency[key]
        else:
            faculty_member = random.choice(faculty[subject])
            timetable.faculty_consistency[key] = faculty_member

        timetable.timetable[batch][department][section][day][timeslot] = {
            "subject": subject,
            "faculty": faculty_member
        }

def genetic_algorithm(population_size, generations):
    population = create_population(population_size)
    for timetable in population:
        timetable.generate()

    for generation in range(generations):
        population.sort(key=lambda x: x.fitness(), reverse=True)
        if population[0].fitness() == 0:
            break

        new_population = population[:2]  # Keep top 2 timetables
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population[:10], k=2)  # Select from top 10
            child = crossover(parent1, parent2)
            if random.random() < 0.1:  # Mutation probability
                mutate(child)
            new_population.append(child)

        population = new_population

    return population[0]


def export_to_excel(timetable):
    wb = Workbook()
    wb.remove(wb.active)  # Remove the default sheet

    for batch in batches:
        ws = wb.create_sheet(title=batch)

        # Add a title row for better readability
        ws.append([f"{batch} Timetable"])
        ws.append([])  # Add an empty row for spacing

        for department in departments:
            ws.append([f"{department} Department"])
            ws.append([])  # Add an empty row for spacing

            for section in sections:
                ws.append([f"Section: {section}"])

                # Create headers: Days as rows, Timeslots as columns
                header_row = ["Day"] + timeslots
                ws.append(header_row)

                # Populate the timetable data
                for day in days:
                    row_data = [day]  # Start with the day
                    for timeslot in timeslots:
                        entry = timetable.timetable[batch][department][section][day][timeslot]
                        subject = entry["subject"]
                        faculty_member = entry["faculty"]

                        # Combine subject and faculty into one cell (e.g., "Physics - Prof. E")
                        if subject and faculty_member:
                            cell_value = f"{subject} - {faculty_member}"
                        elif subject:
                            cell_value = subject
                        else:
                            cell_value = ""  # Empty slot
                        row_data.append(cell_value)

                    ws.append(row_data)

                ws.append([])  # Add an empty row after each section for spacing

    wb.save("timetable.xlsx")
    print("\nTimetable exported to 'timetable.xlsx'.")
# Run the genetic algorithm
best_timetable = genetic_algorithm(population_size=50, generations=200)

def detect_conflicts(timetable):
    conflicts = []

    for batch in batches:
        for department in departments:
            for section in sections:
                # Track daily subject counts, lab hours, and faculty assignments
                daily_subject_counts = {day: {} for day in days}
                daily_lab_hours = {day: 0 for day in days}
                faculty_assignments = {day: {timeslot: set() for timeslot in timeslots} for day in days}

                for day in days:
                    for timeslot in timeslots:
                        entry = timetable.timetable[batch][department][section][day][timeslot]
                        subject = entry["subject"]
                        faculty_member = entry["faculty"]

                        # Check daily subject limit
                        if subject:
                            if subject in daily_subject_counts[day]:
                                daily_subject_counts[day][subject] += 1
                                if daily_subject_counts[day][subject] > 2:
                                    conflicts.append(f"Conflict: Subject '{subject}' exceeds daily limit for {batch}, {department}, {section}, {day}.")
                            else:
                                daily_subject_counts[day][subject] = 1

                        # Check lab hour constraint
                        if subject in lab_subjects:
                            daily_lab_hours[day] += 1
                            if daily_lab_hours[day] > 3:
                                conflicts.append(f"Conflict: Lab hours exceed 3 for {batch}, {department}, {section}, {day}.")

                        # Check faculty availability
                        if faculty_member and day not in faculty_availability.get(faculty_member, []):
                            conflicts.append(f"Conflict: Faculty '{faculty_member}' is unavailable on {day} for {batch}, {department}, {section}.")

                        # Check overlapping faculty assignments
                        if faculty_member:
                            if faculty_member in faculty_assignments[day][timeslot]:
                                conflicts.append(f"Conflict: Faculty '{faculty_member}' is assigned to multiple sections at {timeslot} on {day}.")
                            faculty_assignments[day][timeslot].add(faculty_member)

                        # Check faculty consistency
                        if subject and faculty_member:
                            key = (subject, section)
                            if key in timetable.faculty_consistency:
                                if faculty_member != timetable.faculty_consistency[key]:
                                    conflicts.append(f"Conflict: Inconsistent faculty assignment for {subject} in {section}. Expected {timetable.faculty_consistency[key]}, got {faculty_member}.")
                            else:
                                timetable.faculty_consistency[key] = faculty_member

    return conflicts

conflicts = detect_conflicts(best_timetable)

if conflicts:
    for i in conflicts:
        print(i)

export_to_excel(best_timetable)

import numpy as np
import pandas as pd

def generate_student_data(num_records=1000, filename="student_data.csv"):
    np.random.seed(42)  # For reproducibility

    # Student IDs
    student_ids = [f"STU{i:04d}" for i in range(1, num_records + 1)]

    # Degree Type (UG or PG)
    degree_type = np.random.choice(["UG", "PG"], size=num_records, p=[0.7, 0.3])

    # Course
    courses = []
    for dt in degree_type:
        if dt == "UG":
            courses.append(np.random.choice(["BTech", "BCA", "Others"], p=[0.6, 0.3, 0.1]))
        else:
            courses.append(np.random.choice(["MCA", "MTech", "MBA", "Others"], p=[0.4, 0.2, 0.3, 0.1]))
    courses = np.array(courses)

    # 10th Marks (percentage)
    tenth_marks = np.random.normal(loc=75, scale=12, size=num_records)
    tenth_marks = np.clip(tenth_marks, 40, 99).round(2)

    # 12th Marks (percentage)
    twelfth_marks = np.random.normal(loc=72, scale=14, size=num_records)
    twelfth_marks = np.clip(twelfth_marks, 40, 99).round(2)

    # UG CGPA (0 to 10)
    ug_cgpa = np.random.normal(loc=7.5, scale=1.2, size=num_records)
    ug_cgpa = np.clip(ug_cgpa, 4.5, 9.8).round(2)

    # PG CGPA (0 to 10)
    pg_cgpa = np.zeros(num_records)
    for i in range(num_records):
        if degree_type[i] == 'PG':
            # PG CGPA is somewhat correlated with UG CGPA
            val = ug_cgpa[i] + np.random.normal(0, 0.6)
            pg_cgpa[i] = np.clip(val, 5.0, 9.8).round(2)

    # Programming Skills Score (0 to 100)
    max_cgpa = np.maximum(ug_cgpa, pg_cgpa)
    prog_skills = (max_cgpa / 10) * 100 + np.random.normal(loc=0, scale=15, size=num_records)
    prog_skills = np.clip(prog_skills, 20, 100).round()

    # Communication Skills Score (0 to 100)
    comm_skills = np.random.normal(loc=65, scale=18, size=num_records)
    comm_skills = np.clip(comm_skills, 20, 100).round()

    # Internships (0 to 3)
    internships = np.random.choice([0, 1, 2, 3], size=num_records, p=[0.4, 0.4, 0.15, 0.05])

    # Projects (0 to 5)
    projects = np.where(prog_skills > 70, 
                        np.random.choice([2, 3, 4, 5], size=num_records, p=[0.2, 0.4, 0.3, 0.1]),
                        np.random.choice([0, 1, 2, 3], size=num_records, p=[0.3, 0.4, 0.2, 0.1]))

    # Backlogs (0 to 5)
    backlogs = np.where(max_cgpa < 6.5,
                        np.random.choice([1, 2, 3, 4, 5], size=num_records, p=[0.4, 0.3, 0.15, 0.1, 0.05]),
                        np.random.choice([0, 1, 2], size=num_records, p=[0.85, 0.1, 0.05]))

    # Course weight based on degree
    course_weight = np.where(degree_type == "PG", 5, 0) # PG students get a small boost

    # Placement Status Logic
    score = (ug_cgpa * 10) * 0.15 + (pg_cgpa * 10) * 0.2 + (prog_skills * 0.3) + \
            (comm_skills * 0.2) + (internships * 10) + (projects * 5) - (backlogs * 15) + course_weight
    
    score += np.random.normal(0, 10, size=num_records)
    threshold = np.percentile(score, 45)
    placement_status = np.where(score >= threshold, "Placed", "Not Placed")

    # Create DataFrame
    data = pd.DataFrame({
        "Student_ID": student_ids,
        "Degree_Type": degree_type,
        "Course": courses,
        "10th_Marks": tenth_marks,
        "12th_Marks": twelfth_marks,
        "UG_CGPA": ug_cgpa,
        "PG_CGPA": pg_cgpa,
        "Programming_Skills": prog_skills,
        "Communication_Skills": comm_skills,
        "Internships": internships,
        "Projects": projects,
        "Backlogs": backlogs,
        "Placement_Status": placement_status
    })

    # Save to CSV
    data.to_csv(filename, index=False)
    print(f"Successfully generated {num_records} records and saved to {filename}")

if __name__ == "__main__":
    generate_student_data(1000)

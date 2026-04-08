from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

def create_pdf_report(filename="Project_Report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - 50, "Student Performance & Placement Analysis")
    
    # Subtitle
    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2.0, height - 70, "Project Report")

    # Introduction
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 120, "1. Introduction")
    c.setFont("Helvetica", 11)
    intro_lines = [
        "This data analytics project aims to predict whether a student will be placed or not",
        "based on various academic and extracurricular factors. It analyzes metrics such as",
        "10th and 12th marks, B.Tech CGPA, programming skills, communication skills, internships,",
        "and projects."
    ]
    y_pos = height - 140
    for line in intro_lines:
        c.drawString(50, y_pos, line)
        y_pos -= 15

    # Methodology
    y_pos -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_pos, "2. Methodology")
    c.setFont("Helvetica", 11)
    y_pos -= 20
    meth_lines = [
        "- Data Generation: Synthetic data containing 1,000 student records.",
        "- Tools & Libraries: Python, Pandas, Matplotlib, Seaborn, Scikit-Learn.",
        "- Machine Learning: A Random Forest Classifier trained with an 80/20 train-test split.",
        "- Dashboard: Interactive Streamlit application."
    ]
    for line in meth_lines:
        c.drawString(50, y_pos, line)
        y_pos -= 15

    # Visualizations
    y_pos -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_pos, "3. Key Visualizations")
    y_pos -= 20

    img_path1 = "plots/cgpa_vs_placement.png"
    if os.path.exists(img_path1):
        try:
            img1 = ImageReader(img_path1)
            # Draw image in the available space
            c.drawImage(img1, 100, y_pos - 200, width=400, height=200, preserveAspectRatio=True)
            y_pos -= 220
        except Exception as e:
            c.drawString(50, y_pos, f"Could not load image: {e}")
            y_pos -= 20
    else:
        c.drawString(50, y_pos, "[Image cgpa_vs_placement.png not found. Run train_model.py first!]")
        y_pos -= 20

    img_path2 = "plots/skills_vs_placement.png"
    if os.path.exists(img_path2) and y_pos > 250:
        try:
            img2 = ImageReader(img_path2)
            c.drawImage(img2, 100, y_pos - 200, width=400, height=200, preserveAspectRatio=True)
            y_pos -= 220
        except Exception as e:
            c.drawString(50, y_pos, f"Could not load image: {e}")
            y_pos -= 20

    # Conclusion
    y_pos -= 20
    if y_pos < 100:
        c.showPage()
        y_pos = height - 50

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_pos, "4. Conclusion")
    c.setFont("Helvetica", 11)
    y_pos -= 20
    conc_lines = [
        "The model successfully identifies key predictors of student placements. Higher CGPAs",
        "and strong programming skills strongly correlate with higher placement chances. Extracurricular",
        "factors such as internships and projects also play a crucial role."
    ]
    for line in conc_lines:
        c.drawString(50, y_pos, line)
        y_pos -= 15

    c.save()
    print(f"Report saved as {filename}")

if __name__ == "__main__":
    create_pdf_report()

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph


# Function to generate the PDF
def create_pdf(pdf_file_path, transcription, generated_summary, generated_headline):
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    story = []

    # Styles for each section
    styles = getSampleStyleSheet()

    # Section 1: Generated Headline
    section1_text = f"<font color=green size=14>Generated Headline</font>\n{generated_headline}"
    section1_para = Paragraph(section1_text, styles["Normal"])
    story.append(Spacer(1, 100))  # Spacer to center-align the paragraph
    story.append(section1_para)

    # Section 2: Generated Summary
    section2_text = f"<font color=blue size=16>Generated Summary</font>\n{generated_summary}"
    section2_para = Paragraph(section2_text, styles["Normal"])
    story.append(Spacer(1, 100))  # Spacer to center-align the paragraph
    story.append(section2_para)
    story.append(Spacer(1, 12))  # Add some space between sections

    # Section 3: Transcription
    section3_text = f"<font color=red size=20>Audio Transcription</font>\n{transcription}"
    section3_para = Paragraph(section3_text, styles["Normal"])
    story.append(Spacer(1, 100))  # Spacer to center-align the paragraph
    story.append(section3_para)
    story.append(Spacer(1, 12))  # Add some space between sections

    doc.build(story)
    print("saved as pdf")

# create_pdf(output_file, text2summarize, generated_summary, generated_headline)

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch

def save_to_pdf(file_path, prompt_container):
    canvas_width, canvas_height = letter
    c = canvas.Canvas(file_path, pagesize=letter)
    style = getSampleStyleSheet()['Normal']
    style.fontName = 'Helvetica'
    style.fontSize = 12
    style.leading = 15  # Line spacing

    # Center the document title
    doc_title = prompt_container.docName
    title_width = c.stringWidth(doc_title, style.fontName, style.fontSize)
    centered_title_x = (canvas_width - title_width) / 2
    c.drawString(centered_title_x, canvas_height - 50, doc_title)

    for prompt in prompt_container.customPromptList:
        paragraph = Paragraph(prompt.prompttext, style)
        paragraph_width, paragraph_height = paragraph.wrap(canvas_width - 2 * inch, canvas_height)  # Wrap the paragraph
        centered_paragraph_x = (canvas_width - paragraph_width) / 2
        paragraph.drawOn(c, centered_paragraph_x, prompt.y - paragraph_height)

    c.save()

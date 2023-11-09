from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch

def save_to_pdf(file_path, prompt_container):
    page_width, page_height = letter
    c = canvas.Canvas(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    title_style = styles['Title']

    c.setFillColor(colors.darkblue)
    title = prompt_container.docName
    title_width = c.stringWidth(title, title_style.fontName, title_style.fontSize)
    c.setFont(title_style.fontName, title_style.fontSize)
    c.drawString((page_width - title_width) / 2, page_height - 70, title)

    prompt_text_style = styles['Title'] 
    prompt_text_style.alignment = 1  
    prompt_response_style = styles['BodyText']
    prompt_response_style.textColor = colors.black

    y_position = page_height - 150

    for prompt in prompt_container.customPromptList:
        prompttext = prompt.prompttext
        p_text = Paragraph(prompttext, prompt_text_style)
        text_width, text_height = p_text.wrap(page_width, y_position)
        p_text.drawOn(c, (page_width - text_width) / 2, y_position - text_height)
        y_position -= text_height

        promptresponse = prompt.promptresponse
        p_response = Paragraph(promptresponse, prompt_response_style)
        response_width, response_height = p_response.wrap(page_width - 2 * inch, y_position)
        p_response.drawOn(c, inch, y_position - response_height)
        y_position -= (response_height + 20)

        if y_position > 20:
            c.line(50, y_position, page_width - 50, y_position)
            y_position -= 20

    c.save()

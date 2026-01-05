from xhtml2pdf import pisa
from io import BytesIO

def create_pdf_certificate(content_html):
    result = BytesIO()
    # This turns our HTML template into a real PDF file
    pdf = pisa.pisaDocument(BytesIO(content_html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None

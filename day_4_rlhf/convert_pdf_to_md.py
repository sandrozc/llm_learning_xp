# pip install pypdf2 pdfminer.six markdown


import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import markdown


def pdf_to_text(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, "rb") as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)

    text = fake_file_handle.getvalue()

    converter.close()
    fake_file_handle.close()

    return text


def text_to_markdown(text):
    # This is a simple conversion. You might need to enhance this based on your PDF structure
    lines = text.split("\n")
    md_lines = []
    for line in lines:
        if line.strip():
            if line.isupper():
                md_lines.append(f"# {line}")
            else:
                md_lines.append(line)
    return "\n".join(md_lines)


# Usage
pdf_path = "bedrock-ug.pdf"
output_path = "bedrock-ug.md"

# Convert PDF to text
text = pdf_to_text(pdf_path)

# Convert text to markdown
md_text = text_to_markdown(text)

# Write to file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(md_text)

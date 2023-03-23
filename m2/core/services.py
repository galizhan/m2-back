import pdfkit
from dataclasses import dataclass

from django.template.loader import render_to_string
from django.template.response import SimpleTemplateResponse


@dataclass
class PDFGeneratorService:
    html_string: str

    def generate(self):
        options = {
            'encoding': "UTF-8",
            'enable-local-file-access': ""
        }

        pdf_file = pdfkit.from_string(self.html_string, False, options=options)

        return pdf_file


@dataclass
class PDFGeneratorBuilder:
    template_path: str
    data: dict

    def build(self):
        template_response = SimpleTemplateResponse(self.template_path, self.data)
        template_response.render()
        html_string = template_response.content.decode('utf-8')

        return PDFGeneratorService(html_string)

    def builds(self):
        html_string = render_to_string(self.template_path, {'objects': self.data})
        return PDFGeneratorService(html_string)

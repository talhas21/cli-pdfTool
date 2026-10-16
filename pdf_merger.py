from pypdf import PdfWriter

class PdfMerger:
    def __init__(self, pdf_list: list, merged_name: str):
        self.merger = PdfWriter()
        self.pdf_list = pdf_list
        self.merged_name = merged_name if merged_name.endswith(".pdf") else f"{merged_name}.pdf"

    def process(self):
        for pdf in self.pdf_list:
            filename = pdf if pdf.endswith(".pdf") else f"{pdf}.pdf"
            # Set import_outline=False to bypass the IndirectObject TypeError
            self.merger.append(filename, import_outline=False)

        with open(self.merged_name, "wb") as output:
            self.merger.write(output)

        # free memory
        self.merger.close()
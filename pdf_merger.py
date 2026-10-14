from pypdf import PdfWriter

class PdfMerger:
    def __init__(pdf_list: str, merged_name: list):
        self.merger = PdfWriter()
        self.pdf_list = pdf_list
        self.merged_name = merged_name

    def process(self):
        for pdf in pdf_list:
            self.merger.append(pdf)

        with open(merged_name, "wb") as output:
            self.merger.write(output)

        #free memory
        self.merger.close()
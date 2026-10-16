from pdf_merger import PdfMerger

class Program:
    def run(self):
        merger = PdfMerger(["BusinessStatementTAGS"] + ["cv"+str(6-i) for i in range (6)], "merged") #.pdf?
        merger.process()

if __name__ == "__main__":
    program = Program()
    program.run()
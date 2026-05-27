from abc import ABC, abstractmethod

class ReportGenerator(ABC):

    @abstractmethod
    def generate(self):
        pass

    
class PDFReport(ReportGenerator):

    def generate(self):
        print("Generating PDF")

class ExcelReport(ReportGenerator):

    def generate(self):
        print("Generating Excel")
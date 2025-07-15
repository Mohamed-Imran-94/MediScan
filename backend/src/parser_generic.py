import abc
import re

class MedicalDocParser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text.lower()

    @abc.abstractmethod
    def parse(self):
        pass

class GenericMedicalParser(MedicalDocParser):
    def parse(self):
        return {
            "patient_name": self.extract_field(r"(?:name|patient)[:\-]?\s*(.+)"),
            "patient_address": self.extract_field(r"(?:address)[:\-]?\s*(.+)"),
            "medicines": self.extract_medicines(),
            "directions": self.extract_field(r"(?:directions?)[:\-]?\s*(.+)"),
            "refill": self.extract_field(r"(refill)[:\-]?\s*(.+)")
        }

    def extract_field(self, pattern):
        match = re.search(pattern, self.text, flags=re.IGNORECASE)
        return match.group(1).strip().split("\n")[0] if match else None

    def extract_medicines(self):
        match = re.search(r"(?:rx|medicines?)[:\-]?\s*((?:.|\n)*?)\n(?:directions?|refill|$)", self.text)
        return match.group(1).strip() if match else None

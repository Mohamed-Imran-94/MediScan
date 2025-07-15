import re
from difflib import get_close_matches
from src.parser_generic import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        super().__init__(text)
        self.lines = [line.strip() for line in self.text.splitlines() if line.strip()]

    def parse(self):
        return {
            "patient_name": self.find_line_near("name"),
            "patient_address": self.find_line_near("address"),
            "medicines": self.extract_medicines(),
            "directions": self.extract_directions(),
            "refill": self.find_line_near("refill"),
        }

    def find_line_near(self, keyword):
        """
        Find the line that closely matches the keyword.
        If not found, fallback to lines starting with the same first letter and containing a colon.
        """
        # Step 1: Fuzzy match
        matches = get_close_matches(keyword.lower(), [line.lower() for line in self.lines], n=1, cutoff=0.4)
        if matches:
            for line in self.lines:
                if matches[0] in line.lower():
                    return line.strip()

        # Step 2: Fallback for OCR-mistyped headers like "Mame:", "aéfrene:"
        for line in self.lines:
            if line.lower().startswith(keyword.lower()[0]) and ":" in line:
                return line.strip()

        return ""

    def extract_medicines(self):
        """
        Extract lines that look like medicine names based on common dosage patterns.
        """
        meds = []
        for line in self.lines:
            if re.search(r"\b(mg|gram|tablet|capsule|me|ml)\b", line.lower()):
                meds.append(line)
        return "\n".join(meds).strip()

    def extract_directions(self):
        """
        Capture lines between 'directions' or 'take' and 'refill'
        """
        directions = []
        capture = False
        for line in self.lines:
            if not capture and ("direction" in line.lower() or "take" in line.lower()):
                capture = True
                directions.append(line)
                continue
            if capture:
                if "refill" in line.lower():
                    break
                directions.append(line)
        return "\n".join(directions).strip()

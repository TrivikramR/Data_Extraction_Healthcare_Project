import re

from backend.src.parser_generic import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_address': self.get_field('patient_address'),
            'medicine': self.get_field('medicine'),
            'directions': self.get_field('directions'),
            'refill': self.get_field('refill')
        }

    def get_field(self, field_name):
        pattern_dict ={
            'patient_name' :{'pattern':'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern':'Address:(.*)\n', 'flags': 0},
            'medicine': {'pattern': 'Address:[^\n]*(.*)Directions', 'flags':re.DOTALL},
            'directions': {'pattern': 'Directions:.*?(.*)Refill', 'flags':re.DOTALL},
            'refill': {'pattern': 'Refill:(.*)', 'flags': 0}
        }
        pattern_obj = pattern_dict.get(field_name)
        if pattern_obj:
            matches = re.findall(pattern_obj['pattern'], self.text, flags=pattern_obj['flags'])
        if len(matches) > 0:
            return matches[0].strip()

if __name__ == '__main__':
    document_text = '''
Dr John >mith, M.D

    2 Non-Important street,
    New York, Phone (900)-323- ~2222

    Name:  Virat Kohli Date: 2/05/2022

    Address: 2 cricket blvd, New Delhi

    Omeprazole 40 mg

    Directions: Use two tablets daily for three months

    Refill: 3 times
    '''
    pp = PrescriptionParser(document_text)
    print(pp.parse())

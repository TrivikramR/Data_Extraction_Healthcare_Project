from backend.src.parser_prescription import PrescriptionParser
import pytest

@pytest.fixture()
def doc_1_marta():
    document_text = '''
    Name: Marta Sharapova Date: 5/11/2022

    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg, Lialda 2.4 gram

    Directions:

    Prednisone, Taper 5 mig every 3 days,Finish in 2.5 weeks a,Lialda - take 2 pill everyday for 1 month

    Refill: 2 times
    '''
    return PrescriptionParser(document_text)
@pytest.fixture()
def doc_2_virat():
    document_text = '''
    Dr John >mith, M.D

    2 Non-Important street,
    New York, Phone (900)-323- ~2222

    Name:  Virat Kohli Date: 2/05/2022

    Address: 2 cricket blvd, New Delhi

    Omeprazole 40 mg

    Directions:
    Use two tablets daily for three months

    Refill: 3 times'''

    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_empty():
    return PrescriptionParser('')

def test_get_name(doc_1_marta, doc_2_virat,doc_empty):
    assert doc_1_marta.get_field("patient_name") == "Marta Sharapova"
    assert doc_2_virat.get_field("patient_name") == "Virat Kohli"
    assert doc_empty.get_field("patient_name") == None

def test_get_address(doc_1_marta, doc_2_virat, doc_empty):
    assert doc_1_marta.get_field("patient_address") == "9 tennis court, new Russia, DC"
    assert doc_2_virat.get_field("patient_address") == "2 cricket blvd, New Delhi"
    assert doc_empty.get_field("patient_address") == None

def test_get_medicine(doc_1_marta, doc_2_virat, doc_empty):
    assert doc_1_marta.get_field("medicine") == "Prednisone 20 mg, Lialda 2.4 gram"
    assert doc_2_virat.get_field("medicine") == "Omeprazole 40 mg"
    assert doc_empty.get_field("medicine") == None

def test_get_directions(doc_1_marta, doc_2_virat, doc_empty):
    assert doc_1_marta.get_field("directions") == "Prednisone, Taper 5 mig every 3 days,Finish in 2.5 weeks a,Lialda - take 2 pill everyday for 1 month"
    assert doc_2_virat.get_field("directions") == "Use two tablets daily for three months"
    assert doc_empty.get_field("directions") == None

def test_get_refill(doc_1_marta, doc_2_virat, doc_empty):
    assert doc_1_marta.get_field("refill") == "2 times"
    assert doc_2_virat.get_field("refill") == "3 times"
    assert doc_empty.get_field("refill") == None

def test_parse(doc_1_marta, doc_2_virat, doc_empty):
    record_marta = doc_1_marta.parse()
    assert record_marta == {
        'patient_name': 'Marta Sharapova',
        'patient_address': '9 tennis court, new Russia, DC',
        'medicine': 'Prednisone 20 mg, Lialda 2.4 gram',
        'directions': 'Prednisone, Taper 5 mig every 3 days,Finish in 2.5 weeks a,Lialda - take 2 '
 'pill everyday for 1 month',
        'refill': '2 times'
    }

    record_virat = doc_2_virat.parse()
    assert record_virat == {
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket blvd, New Delhi',
        'medicine': 'Omeprazole 40 mg',
        'directions': 'Use two tablets daily for three months',
        'refill': '3 times'
    }



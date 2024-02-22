from backend.src.patient_details_parser import PatientDetailsParser
import pytest

@pytest.fixture()
def doc_1_katy():
    document_text = '''
    17/12/2020

    Patient Medical Record . : :

    Patient Information

    Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight:
    9264 Ash Dr 95
    New York City, 10005 a
    United States Height:
    190
    In Case of Emergency
    en oe
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    Genera! Medical History
    I a
    Chicken Pox (Varicella): Measies:
    IMMUNE IMMUNE

    Have you had the Hepatitis B vaccination?

    No

    List any Medical Problems (asthma, seizures, headaches):

    Migraine
    '''
    return PatientDetailsParser(document_text)
@pytest.fixture()
def doc_2_jerry():
    document_text = '''
        a

        Patient Medical Record
        
        Patient Information
        Jerry Lucas
        
        (279) 920-8204
        4218 Wheeler Ridge Dr
        
        Buffalo, New York, 14201
        United States
        
        In Case of Emergency
        
        Birth Date
        May 2 1998
        
        Weight:
        57
        
        Height:
        170
        
        Joe Lucas
        
        Home phone
        
        General Medical History
        
        4218 Wheeler Ridge Dr
        Buffalo, New York, 14201
        United States
        
        Work phone
        
        Chicken Pox (Varicelia):
        
        IMMUNE
        
        Have you had the Hepatitis B vaccination?
        Yes
        Measles:
        
        NOT IMMUNE
        
        List any Medical Problems (asthma, seizures, headaches):
        
        N/A
           '''
    return PatientDetailsParser(document_text)

def test_get_patient_name(doc_1_katy, doc_2_jerry):
    assert doc_1_katy.get_patient_name() == 'Kathy Crawford'
    assert doc_2_jerry.get_patient_name() == 'Jerry Lucas'

def test_get_patient_phone(doc_1_katy, doc_2_jerry):
    assert doc_1_katy.get_patient_phone() == '(737) 988-0851'
    assert doc_2_jerry.get_patient_phone() == '(279) 920-8204'

def test_get_patient_vaccine(doc_1_katy, doc_2_jerry):
    assert doc_1_katy.get_patient_vaccine() == 'No'
    assert doc_2_jerry.get_patient_vaccine() == 'Yes'

def test_get_patient_medicine(doc_1_katy, doc_2_jerry):
    assert doc_1_katy.get_patient_medical_problems() == 'Migraine'
    assert doc_2_jerry.get_patient_medical_problems() == 'N/A'

def test_parse(doc_1_katy, doc_2_jerry):
    record_katy = doc_1_katy.parse()
    assert record_katy == {
        'patient_name': 'Kathy Crawford',
        'phone_number': '(737) 988-0851',
        'vaccine': 'No',
        'medical_problem': 'Migraine'
    }

    record_jerry = doc_2_jerry.parse()
    assert record_jerry == {
        'patient_name': 'Jerry Lucas',
        'phone_number': '(279) 920-8204',
        'vaccine': 'Yes',
        'medical_problem': 'N/A'
    }

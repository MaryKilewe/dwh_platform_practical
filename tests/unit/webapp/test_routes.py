from tests.unit.webapp import client


def test_landing_page(client):
    landing = client.get("/")

    assert landing.status_code == 200

def test_landing_aliases(client):
    landing = client.get("/")
    assert client.get("/index").data == landing.data


def test_add_patients_page(client):
    add_patients = client.get("/add_patients")

    assert add_patients.status_code == 200

def test_submissions_page(client):
    submissions = client.get("/submissions")

    assert submissions.status_code == 200

def test_summary_page(client):
    summary = client.get("/Nairobi Hospital/summary")

    assert summary.status_code == 200

def test_charts(client):
    gender = client.get("/get_gender_statistics")
    age = client.get("/get_age_statistics")
    registrations = client.get("/monthly_reg_stats")

    assert gender.status_code == 200
    assert age.status_code == 200
    assert registrations.status_code == 200

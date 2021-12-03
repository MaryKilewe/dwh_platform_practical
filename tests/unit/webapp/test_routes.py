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

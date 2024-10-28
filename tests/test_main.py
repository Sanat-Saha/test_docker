from fastapi.testclient import TestClient

from app.main  import app

client = TestClient(app)


def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"name": "ob-sample-fast-api", "version": "1.0.0"}
    

def test_operation_square():
    
    len_in_mtr = 2 
    response = client.get(f"/operation/area/{len_in_mtr}")
    assert response.status_code == 200
    assert response.json() == {"cal_area":4,"len_in_mtr":2}
    
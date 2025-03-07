from http import HTTPStatus


def test_should_post_lead_return_201(app_testing):
    client = app_testing.test_client()
    lead_data = {"email": "email@email.com"}
    response = client.post("/api/v1/leads/", json=lead_data)
    assert response.status_code == HTTPStatus.CREATED

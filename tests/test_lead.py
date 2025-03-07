from http import HTTPStatus

import pytest


def test_should_post_lead_return_201(app_testing):
    client = app_testing.test_client()
    lead_data = {"email": "email@email.com"}
    response = client.post("/api/v1/leads/", json=lead_data)
    assert response.status_code == HTTPStatus.CREATED


def test_should_post_lead_return_400_for_missing_email(app_testing):
    client = app_testing.test_client()
    lead_data = {}
    response = client.post("/api/v1/leads/", json=lead_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_should_post_lead_return_400_for_invalid_email(app_testing):
    client = app_testing.test_client()
    lead_data = {"email": "invalid-email"}
    response = client.post("/api/v1/leads/", json=lead_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_should_post_lead_return_400_for_empty_email(app_testing):
    client = app_testing.test_client()
    lead_data = {"email": ""}
    response = client.post("/api/v1/leads/", json=lead_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

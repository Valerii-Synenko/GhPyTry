import allure
import requests
from faker import Faker


def test_register_user():

    with allure.step("Step 1: prepare all for test"):
        faker = Faker()
        url = "http://localhost/register"
        headers = {"Content-Type": "application/json"}
        user_payload = {
            "username": faker.user_name(),
            "password": faker.password(),
            "email": faker.email(),
        }

    with allure.step("Step 2: make post request"):
        response = requests.post(
            url=url,
            headers=headers,
            json=user_payload,
        )

    with allure.step("Step 3: assert 200 OK"):
        assert response.status_code == 400
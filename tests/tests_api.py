import requests
import os
from dotenv import load_dotenv
from schemas.schema import auth_token, get_booking, create_booking, update_booking
from pytest_voluptuous import S
from utils.base_session import BaseSession
from data.user import user
import allure
from allure_commons.types import Severity

load_dotenv()
web_url = os.getenv("WEB_URL")
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


@allure.tag('API')
@allure.description('API test')
@allure.label('owner', 'andrechizh8')
@allure.severity(Severity.CRITICAL)
def test_create_booking(restful):
    """Create booking with write booking_id in txt file """
    response = restful.post(url="/booking", json={
        "firstname": user.first_name,
        "lastname": user.last_name,
        "totalprice": user.total_price,
        "depositpaid": user.deposit_paid,
        "bookingdates": {
            "checkin": user.checkin,
            "checkout": user.checkout
        },
        "additionalneeds": user.additional_needs
    })
    assert response.status_code == 200
    assert response.json()["booking"]["firstname"] == user.first_name
    booking_id = response.json()["bookingid"]
    with open("id.txt", 'w') as file:
        file.write(str(booking_id))


def test_read_id():
    """Read txt file and write it in variable"""
    with open("id.txt", "r") as file:
        booking_id = file.read()
    return booking_id


@allure.tag('API')
@allure.description('API test')
@allure.label('owner', 'andrechizh8')
@allure.severity(Severity.CRITICAL)
def test_get_created_booking(restful):
    """Check right booking create"""
    booking_id = test_read_id()
    response = restful.get(url=f"/booking/{booking_id}")
    assert response.status_code == 200
    assert S(get_booking) == response.json()


@allure.tag('API')
@allure.description('API test')
@allure.label('owner', 'andrechizh8')
@allure.severity(Severity.CRITICAL)
def test_update_booking(restful, get_token):
    """Update booking """
    booking_id = test_read_id()
    response = restful.put(url=f"/booking/{booking_id}", headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={get_token}"
    }, json={
        "firstname": user.update_first_name,
        "lastname": user.update_last_name,
        "totalprice": user.total_price,
        "depositpaid": user.deposit_paid,
        "bookingdates": {
            "checkin": user.checkin,
            "checkout": user.checkout
        },
        "additionalneeds": user.additional_needs
    }
                           )
    assert response.status_code == 200
    assert S(update_booking) == response.json()
    assert response.json()["firstname"] == user.update_first_name


@allure.tag('API')
@allure.description('API test')
@allure.label('owner', 'andrechizh8')
@allure.severity(Severity.CRITICAL)
def test_delete_booking(restful, get_token):
    """Delete booking"""
    booking_id = test_read_id()
    response = restful.delete(url=f"/booking/{booking_id}",
                              headers={
                                  "Cookie": f"token={get_token}"

                              })
    assert response.status_code == 201


@allure.tag('API')
@allure.description('API test')
@allure.label('owner', 'andrechizh8')
@allure.severity(Severity.CRITICAL)
def test_deleted_booking(restful):
    """Check  booking deleted"""
    booking_id = test_read_id()
    response = restful.get(url=f"/booking/{booking_id}")
    assert response.status_code == 404

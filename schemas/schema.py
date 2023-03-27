from voluptuous import PREVENT_EXTRA, Schema

auth_token = Schema({
    "token": str
}, extra=PREVENT_EXTRA,
    required=True)

create_booking = Schema(
    {
        "bookingid": int,
        "booking": {
            "firstname": str,
            "lastname": str,
            "totalprice": int,
            "depositpaid": True,
            "bookingdates": {
                "checkin": str,
                "checkout": str
            },
            "additionalneeds": str
        }
    }, extra=PREVENT_EXTRA,
    required=True)

get_booking = Schema(
    {
        "firstname": str,
        "lastname": str,
        "totalprice": int,
        "depositpaid": True,
        "bookingdates": {
            "checkin": str,
            "checkout": str
        },
        "additionalneeds": str
    }, extra=PREVENT_EXTRA,
    required=True)

update_booking = Schema(
    {

        "firstname": str,
        "lastname": str,
        "totalprice": int,
        "depositpaid": True,
        "bookingdates": {
            "checkin": str,
            "checkout": str
        },
        "additionalneeds": str
    }
)

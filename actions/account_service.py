import requests

account_base_url = "http://bankbot.mindorbital.com/account/"


class AccountService:
    def check_by_phone_number(phone_number):
        account_api_url = account_base_url + "check/" + phone_number
        account_json = requests.get(account_api_url).json()

        if "status" in account_json:
            return account_json["status"]

        elif account_json["message"] == "success":
            return account_json["data"]

    def send_otp_number(phone_number):
        otp_api_url = account_base_url + "otp/" + phone_number
        otp_json = requests.get(otp_api_url).json()


    def verify_otp_number(phone_number, otp_number):
        request_object = {'phone_no': phone_number, 'otp' : otp_number}
        verify_response = requests.post(account_base_url + "otp/verify", json=request_object)

        return verify_response.status_code

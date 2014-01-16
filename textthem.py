from twilio.rest import TwilioRestClient
from .twilio_settings import TOKEN, SID, TWILIO_NUMBER, CUSEC_GROUP

client = TwilioRestClient(SID, TOKEN)

BODY = "Breakfast is being served tomorrow at 9am. Registration starts at 8am. There are a limited amount of swag bags."

if __name__ == "__main__":
    for delegate in CUSEC_GROUP:
        message = client.sms.messages.create(body=BODY, to=delegate, from_=TWILIO_NUMBER)
        print message.sid

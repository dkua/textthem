from twilio.rest import TwilioRestClient
from twilio_settings import TOKEN, SID, TWILIO_NUMBER, ME, UTSC, UTSG

client = TwilioRestClient(SID, TOKEN)

CUSEC_GROUP = ME + UTSC + UTSG
BODY = "Resume roast at 12:30pm and Career Fair starts 1:30pm. Shouldn't miss either"

if __name__ == "__main__":
    for delegate in CUSEC_GROUP:
        message = client.sms.messages.create(body=BODY, to=delegate, from_=TWILIO_NUMBER)
        print message.sid

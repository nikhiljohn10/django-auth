import six
from django.conf import settings
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AccountActivation(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.email_verified))


class Gmail:

    def __init__(self):
        self.user = settings.GMAIL_USER or None
        self.flow = InstalledAppFlow.from_client_secrets_file(
            client_secrets_file=settings.GMAIL_SECRET,
            scopes=settings.GMAIL_SCOPES,
            redirect_uri=settings.GMAIL_REDIRECT)
        auth_uri, auth_state = self.flow.authorization_url()
        self.activated = False
        if auth_uri and auth_state:
            self.auth_uri = auth_uri
            self.auth_state = auth_state

    def verify(self, code):
        self.flow.fetch_token(code=code)
        self.credentials = self.flow.credentials
        self.service = build('gmail', 'v1', credentials=self.credentials)
        self.activated = True


    def create_message(self, subject, message_text, from_email, recipient_list):
        message = MIMEText(message_text)
        message['to'] = ', '.join(recipient_list)
        message['from'] = from_email
        message['subject'] = subject
        raw = urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw}

    def send_mail(self, subject, message, recipient_list):
        if self.activated:
            try:
                body = self.create_message(
                    subject,
                    message,
                    self.user,
                    recipient_list)
                sent_message = (self.service.users().messages().send(
                    userId="me",
                    body=body).execute())
                print('Message sent with id: %s' % sent_message['id'])
            except HttpError as error:
                print('An error occurred: %s' % error)
        else:
            print("Gmail not activated")

activater = AccountActivation()
mailer = Gmail()

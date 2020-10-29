import six
from django.conf import settings
from django.core import serializers
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
            client_secrets_file='client_secret.apps.googleusercontent.com.json',
            scopes=['https://www.googleapis.com/auth/gmail.send'],
            redirect_uri='http://mac.pro:8000/auth/gmail/verify')
        auth_uri, auth_state = self.flow.authorization_url()
        if auth_uri and auth_state:
            self.auth_uri = auth_uri
            self.auth_state = auth_state

    def verify(self, request, code):
        self.flow.fetch_token(code=code)
        self.credentials = self.flow.credentials
        self.session = self.flow.authorized_session()
        request.session['credentials'] = {
            'token': self.credentials.token,
            'refresh_token': self.credentials.refresh_token,
            'token_uri': self.credentials.token_uri,
            'client_id': self.credentials.client_id,
            'client_secret': self.credentials.client_secret,
            'scopes': self.credentials.scopes}
        self.service = build('gmail', 'v1', credentials=self.credentials)

    def create_message(self, message_text, subject, receivers):
        message = MIMEText(message_text)
        message['to'] = ', '.join(receivers)
        message['from'] = self.user
        message['subject'] = subject
        raw = urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw}

    def send_message(self, message, subject, receivers):
        try:
            body = self.create_message(message, subject, receivers)
            sent_message = (self.service.users().messages().send(
                userId="me", body=body).execute())
            print('Message sent with id: %s' % sent_message['id'])
        except HttpError as error:
            print('An error occurred: %s' % error)


activater = AccountActivation()
mailer = Gmail()

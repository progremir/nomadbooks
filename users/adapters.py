from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        url = '{base_url}/confirm/{key}'.format(
            base_url=settings.FRONT_URL, key=emailconfirmation.key
        )
        return url

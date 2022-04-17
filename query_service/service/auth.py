from rest_framework import authentication
from rest_framework import exceptions

class User:
    def __init__(self):
        self.is_authenticated = True

class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')


        if token != 'c8a0d2339b0eb737f303fb350694acee':
            return None
        else:
            print('Returning user')
            return (User(), None)

        # try:
        #     user = User.objects.get(username=username)
        # except User.DoesNotExist:
        #     raise exceptions.AuthenticationFailed('No such user')

        # return (user, None)
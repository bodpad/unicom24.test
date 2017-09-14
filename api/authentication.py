from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token


class TokenAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):

        # Токен пользователя переданный через url
        token = request.resolver_match.kwargs.get('token')

        try:
            # Получаем о
            token_obj = Token.objects.get(key=token)
        except:
            raise exceptions.AuthenticationFailed('Incorrect token')
        else:
            user = token_obj.user

            group = user.groups.first()
            if group is None:
                # Если пользователь не принадлежит ни к одной из групп.
                # Информацию о досутупных группах см. в документации README.md
                raise exceptions.PermissionDenied('The user does not belong to any of the groups.')

            user.group = group.name

            return (user, None)

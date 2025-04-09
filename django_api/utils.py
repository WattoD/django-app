import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone

User = get_user_model()

def generate_jwt_token(user):
    access_payload = {
        'user_id': user.id,
        'username': user.email,
        'exp': timezone.now() + timedelta(days=settings.JWT_EXPIRATION_DAYS, minutes=settings.JWT_EXPIRATION_MINUTES),
        'iat': timezone.now(),
    }
    access_token = jwt.encode(access_payload, settings.SECRET_KEY, algorithm='HS256')

    refresh_payload = {
        'user_id': user.id,
        'username': user.email,
        'iat': timezone.now(),
    }
    refresh_token = jwt.encode(refresh_payload, settings.SECRET_KEY, algorithm='HS256')
    return access_token, refresh_token


def refresh_jwt_token(refresh_token):
    payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=['HS256'])
    user = User.objects.get(id=payload['user_id'])
    new_access_token = generate_jwt_token(user)[0]
    return new_access_token

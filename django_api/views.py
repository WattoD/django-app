from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import AuthenticationFailed

from django_api.authentication import CustomJWTAuthentication
from django_api.utils import generate_jwt_token, refresh_jwt_token
from django.contrib.auth import authenticate
from courses.models import Course
from django_api.serializers import CourseSerializer

# Create your views here.
class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ['language']
    search_fields = ['title']
    ordering_fields = ['created_at']
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class CourseModelReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['language']

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'email': user.email})

@api_view(['POST'])
@permission_classes([])
def obtain_jwt(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user:
        token = generate_jwt_token(user)
        return Response({
            'access_token': token[0],
            'refresh_token': token[1],
        })
    return Response({'error': 'Invalid credentials'}, status=401)

@api_view(['POST'])
@permission_classes([])
def refresh_jwt(request):
    refresh_token = request.data.get('refresh_token')
    if not refresh_token:
        raise AuthenticationFailed('Refresh token is required')

    try:
        new_access_token = refresh_jwt_token(refresh_token)

        return Response({
            'access_token': new_access_token
        })

    except AuthenticationFailed as e:
        return Response({
            'detail': str(e)
        }, status=401)
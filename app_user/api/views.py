from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from app_user.api.serializers import RegistrationSerializer
from rest_framework.decorators import api_view

# for manually creating the JWT token
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST',])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration successfull"
            data['username'] = account.username
            data['email'] = account.email

            
            # For JWT Auth
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            
  
        else:
            data = {
                'error':'Some error occured here'
            }
            
        return Response(data, status=status.HTTP_201_CREATED)

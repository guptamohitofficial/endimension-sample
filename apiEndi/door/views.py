from apiEndi.easy import *
from rest_framework.authtoken.views import ObtainAuthToken
from door.serializers import UserSerializer

# Create your views here.
# This module represents an door or gateway for whole application
# This also take care of authentication

# Overriding default token sending functionality
OAT = ObtainAuthToken
class Login(OAT):
    # This handles an exception which occurs on invalid credentials
    def post(self, request, *args, **kwargs):
        context = {'valid':True}
        try: res = OAT.post(self, request, *args, **kwargs); context = {**res.data, **context}
        except: context['valid'] = False
        return Response(context)

    def get(self, request, *args, **kwargs):
        return Response({'detail':'End-point is not accessible'})

class ValidateToken(APIView):
    def post(self, request, *args, **kwargs):
        try:
            org = Token.objects.get(key=request.data.get('token')).user
            if org:
                return Response({
                    'valid':True,
                    'user':ShortOrganizationSerializer(org).data
                    })
        except:
            pass
        return Response({'valid':False})


class GetUser(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        context = {'valid':True}
        context['user'] = UserSerializer(request.user).data
        return Response(context)




from apiEndi.easy import *
from django.contrib.auth.models import User
from door.serializers import FullUserSerializer

class getDoctors(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        context = {'valid':True}
        context['doctors'] = FullUserSerializer(User.objects.filter(last_name='doctor'), many=True).data
        return Response(context)




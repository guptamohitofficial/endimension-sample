from apiEndi.easy import *
from hospital.serializers import RecordSerializer
from hospital.models import Record, Report

class SaveANewRecord(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        context = {'valid':True}
        data = request.data
        record = Record(name=data['name'], age=data['age'], gender=data['gender'], image=data['image'],\
            time=timezone.localtime(), doctor=getUserFromId(data['doctor']), hospital=request.user)
        record.save()
        return Response(context)

    def get(self, request, *args, **kwargs):
        return Response({'detail':'End-point is not accessible'})


class GetRecords(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        context = {'valid':True}
        if request.user.last_name=="doctor":
            context['records'] = RecordSerializer(Record.objects.filter(doctor=request.user).order_by('-id'),many=True).data
        else: 
            context['records'] = RecordSerializer(Record.objects.all().order_by('-id'),many=True).data
        return Response(context)


class GetRecord(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        context = {'valid':True}
        context['record'] = Record.objects.filter(id=self.kwargs['id']).values('id','name','image','age','time','gender')[0]
        context['record']['time'] = UTCtoITC(context['record']['time']).strftime("%-d-%b, (%I:%M%p)")
        try:
            context['report'] = Report.objects.get(patient=self.kwargs['id']).report
        except:
            context['report'] = ""
        return Response(context)


class SaveReport(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        context = {'valid':True}
        try:
            record = Record.objects.get(id=request.data['pid'])
            report = Report.objects.get(patient=record)
            report.report = request.data['report']
            report.save()    
        except:
            Report(patient=record,report=request.data['report']).save()
        return Response(context)

    

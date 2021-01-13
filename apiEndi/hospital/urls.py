from django.urls import path
from hospital.views import SaveANewRecord, GetRecords, GetRecord, SaveReport

urlpatterns = [
    path('save-a-record', SaveANewRecord.as_view()),
    path('get-records', GetRecords.as_view()),
    path('get-record-details/<id>', GetRecord.as_view()),
    path('save-patient-report', SaveReport.as_view())
]

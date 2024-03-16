from django.urls import path
from data_infer_module.views import CSVUploadView
from data_infer_module.views import FileSchemaPatchAPIView

urlpatterns = [
    path('upload-csv/', CSVUploadView.as_view(), name='upload_csv'),
    path('file_schemas/<int:pk>/patch/', FileSchemaPatchAPIView.as_view(), name='file_schema_patch'),

]
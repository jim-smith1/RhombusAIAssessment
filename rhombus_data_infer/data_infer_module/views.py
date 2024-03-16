from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from data_infer_module.serializers import CSVUploadSerializer
from data_infer_module.serializers import FileSchemaSerializer
from data_infer_module.models import FileSchema


# Create your views here.

class CSVUploadView(APIView):
    def post(self, request, format=None):
        '''
        Post method for uploading a csv file extracting it as a pandas dataframe, infering its datatypes
        and storing the schema into the database.
        :param request: incoming request body
        :param format: N/A
        :return: an HTTP Response
        '''
        serializer = CSVUploadSerializer(data=request.data)
        if serializer.is_valid():
            instances = serializer.save()
            serialized_data =  FileSchemaSerializer(instances, many=True).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileSchemaPatchAPIView(generics.UpdateAPIView):
    '''
    View for applying a patch update request against table entries for infered schema.
    '''
    queryset = FileSchema.objects.all()
    serializer_class = FileSchemaSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
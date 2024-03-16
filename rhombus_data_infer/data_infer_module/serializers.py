from rest_framework import serializers
import pandas as pd

from data_infer_module.models import FileSchema
from data_infer_module.utils.infer_data_types import infer_and_convert_data_types


class CSVUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def save(self, **kwargs):
        '''
        override the base save method to perform save operation for the csv schema attributes
        using another serializer.
        :param kwargs: additional attributes
        :return: created instances
        '''
        validated_data = self.validated_data
        file = validated_data['file']
        df = pd.read_csv(file)
        df = infer_and_convert_data_types(df)
        columns_schema = []
        for index, item in enumerate(df.columns):
            columns_schema.append({"column_name": item, "data_type": str(df[item].dtype)})
        print(columns_schema)
        schema_serializer = FileSchemaSerializer(data=columns_schema, many=True)
        if schema_serializer.is_valid(raise_exception=True):
            return schema_serializer.save()



class FileSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileSchema
        fields = '__all__'


from rest_framework.serializers import ModelSerializer
from web.models import qc_datasheet_mueller_hinton_agar


class MHserializer(ModelSerializer):
    class Meta:
        model=qc_datasheet_mueller_hinton_agar
        fields='__all__'
from rest_framework.serializers import ModelSerializer
from .models import Super

class SuperSerializer(ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']
        depth = 1
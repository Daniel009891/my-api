from django.db import IntegrityError
from rest_framework import serializers
from saved.models import Saved


class SavedSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    
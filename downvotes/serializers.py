from django.db import IntegrityError
from rest_framework import serializers
from downvotes.models import DownVote


class DownVoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    
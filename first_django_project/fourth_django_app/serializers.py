from rest_framework import serializers

from .models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ("time", "initial_val", "initial_met", "final_val", "final_met")
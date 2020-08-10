from rest_framework import serializers


class ReportInputSerializer(serializers.ModelSerializer):
    """GameServerAuthInputSerializer."""
    supplierid = serializers.CharField(help_text='Contains supplier id in website')
"""Game server  fake API."""
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from algo.serializers.report import (ReportInputSerializer)


class Report(APIView):
    """GameServerAuthView."""
    permission_classes = [AllowAny, ]

    def post(self, request):
        """Game server fake authentication."""
        input_serializer = ReportInputSerializer(data=request.data)
        print(input_serializer)
        # try:
        #     input_serializer.is_valid(raise_exception=True)
        #     output_serializer = GameServerAuthOutputSerializer({'result': 'success'})
        # except Exception:
        #     output_serializer = GameServerAuthOutputSerializer({'result': 'fail'})

        return Response(input_serializer.data)

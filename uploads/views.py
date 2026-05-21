from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UploadedFile
from .serializers import UploadedFileSerializer

class FileUploadAPIView(APIView):
    def post(self, request):

        uploaded_file = request.FILES.get('file')

        if not uploaded_file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        file_instance = UploadedFile.objects.create(
            file=uploaded_file,
            filename=uploaded_file.name
        )

        serializer = UploadedFileSerializer(file_instance)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


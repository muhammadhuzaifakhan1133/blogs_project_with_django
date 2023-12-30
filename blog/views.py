from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .models import BlogModel
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.request import Request

class BlogModelViewSet(ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        return BlogModel.objects.filter(author_id=self.request.user.id)

    def create(self, request: Request, *args, **kwargs):
        serialized = BlogSerializer(data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "author_id": request.user.id,
        })
        if serialized.is_valid():
            serialized.save()
            return Response({"message": "blog saved successfully"})
        return Response(serialized.errors)
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializers

# Create your views here.
    
class NoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
   
    

from rest_framework import serializers
from .models import Note

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','body','created_date')
        model = Note
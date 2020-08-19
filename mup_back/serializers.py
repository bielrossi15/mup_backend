from rest_framework import serializers
from .models import Boletim, General, About

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
    
    def validate(self, texts):
        if About.objects.filter(title=texts['title']):
            raise serializers.ValidationError({'title', 'There is a text with this title'})
        return super().validate(texts)

class BoletimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boletim
        fields = '__all__'

    def validate(self, texts):
        if Boletim.objects.filter(title=texts['title']):
            raise serializers.ValidationError({'title', 'There is a text with this title'})
        return super().validate(texts)

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = '__all__'

    def validate(self, texts):
        if General.objects.filter(title=texts['title']):
            raise serializers.ValidationError({'title', 'There is a text with this title'})
        return super().validate(texts)
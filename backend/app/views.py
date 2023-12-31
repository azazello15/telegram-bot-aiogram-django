import random

from django.http import HttpResponseNotFound
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Words


class WordSerializator(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ['pk', 'gender', 'word']


class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = Words.objects.all()
        random_word = random.choice(all_words)
        serialized_random_word = WordSerializator(random_word, many=False)
        return Response(serialized_random_word.data)


class NextWord(APIView):
    def get(self, request, pk, format=None):
        word = Words.objects.filter(pk__gt=pk).first()
        if not word:
            return HttpResponseNotFound
        else:
            serialized_word = WordSerializator(word, many=False)
            return Response(serialized_word.data)


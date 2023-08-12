from random import sample as sm, shuffle as sh, choice as ch
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from . models import Grup, Objec
from .serializers import GrupSerializer, ObjecSerializer
from rest_framework import status
from rest_framework.renderers import JSONRenderer


class Show_all_grups(APIView):
    queryset = Grup.objects.all()
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        grups = Grup.objects.all()
        serializer = GrupSerializer(grups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GrupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class Show_all_objecs(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        objecs = Objec.objects.all()
        serializer = ObjecSerializer(objecs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        grup_name = request.data.get('grup', None)

        if not grup_name:
            return Response({'grup': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            grup = Grup.objects.get(name=grup_name)
        except Grup.DoesNotExist:
            return Response({'grup': 'Grup with this name does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ObjecSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(grup=grup)  # Сохраняем объект с указанным группой
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailGrup(APIView):
    queryset = Grup.objects.all()
    permission_classes = [permissions.AllowAny]

    def get(self, request, slug):
        grup = Grup.objects.get(slug=slug)  # Получаем объект Grup по slug

        # Получаем все объекты Objec, связанные с этой группой
        objecs = Objec.objects.filter(grup=grup)

        serializer = ObjecSerializer(objecs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def random_objecs(request, slug, n):
    grup = Grup.objects.get(slug=slug)  # Получаем объект Grup по slug
    # Получаем все объекты Objec, связанные с этой группой
    objecs = Objec.objects.filter(grup=grup)
    one_false = ch(list(filter(lambda x: not x.ident, objecs)))
    many_true = sm(list(filter(lambda x: x.ident, objecs)), n - 1)
    many_true.append(one_false)
    sh(many_true)
    random_objecs = sm(many_true, n)
    serializer = ObjecSerializer(random_objecs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class Random_objecs(APIView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]  # Используйте соответствующий рендерер

    def get(self, request, slug, n):
        grup = Grup.objects.get(slug=slug)  # Получаем объект Grup по slug
        # Получаем все объекты Objec, связанные с этой группой
        objecs = Objec.objects.filter(grup=grup)
        one_false = ch(list(filter(lambda x: not x.ident, objecs)))
        many_true = sm(list(filter(lambda x: x.ident, objecs)), n - 1)
        many_true.append(one_false)
        sh(many_true)
        random_objecs = sm(many_true, n)
        serializer = ObjecSerializer(random_objecs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
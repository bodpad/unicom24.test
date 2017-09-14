from rest_framework import generics, filters
from .serializers import *
from .permissions import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend


class CustomerProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = CustomerProfile.objects.all()
    permission_classes = (CustomerProfilePermission,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = [field.name for field in CustomerProfile._meta.fields]  # __all__ не сработало
    ordering_fields = '__all__'


class CustomerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (CustomerProfilePermission, )


class Request2coList(generics.ListCreateAPIView):
    queryset = Request2co.objects.all()
    serializer_class = Request2coSerializer
    permission_classes = (Request2coPermission,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = [field.name for field in Request2co._meta.fields]  # __all__ не сработало
    ordering_fields = '__all__'


class Request2coDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request2co.objects.all()
    serializer_class = Request2coSerializer
    permission_classes = (Request2coPermission,)

    def get(self, request, *args, **kwargs):

        if request.user.group == 'credit_organization':
            # При просмотре заявки пользователем из группы "Кредитные организации",
            # статус заявки меняем на 'RECEIVED' (стоило бы описать зачем это делается)
            id = kwargs['pk']
            request2co = Request2co.objects.filter(id=id)
            if request2co.exists():
                request2co.status = 3
                request2co.save()

        return self.retrieve(request, *args, **kwargs)
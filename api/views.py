from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import *
from tea.models import *


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # lookup_field = 'name'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BuyerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import  viewsets
from main.models import Product, Comment
from .permissions import ProductPermission, IsCommentAuthor, IsProductAuthor
from .serializers import ProductDetailsSerializer, ProductSerializer, CommentSerializer
from .filters import ProductFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    filterset_class = ProductFilter


    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params
        print(params)
        # queryset = queryset.filter(**params)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [ProductPermission, IsProductAuthor, ]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        return ProductDetailsSerializer

    def get_serializer_context(self):
        return {'action': self.action, 'request': self.request}

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [ProductPermission, ]
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [IsCommentAuthor, ]
        return [permission() for permission in permissions]











#
# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True, context={'request': request})
#     return Response(serializer.data)
#
# # class ProductsList(APIView):
# #     def get(self, request, format=None):
# #         products = Product.objects.all()
# #         serializer = ProductSerializer(products, many=True, context={'request': request})
# #         return Response(serializer.data)
#
#
# class ProductsList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductDetails(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailsSerializer
#
#
# class CreateProduct(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = CreateProductSerializer
#     permission_classes = [ProductPermission, ]
#
#
# class UpdateProduct(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = UpdateProductSerializer
#     permission_classes = [ProductPermission, ]
#
#
# class DeleteProduct(DestroyAPIView):
#     queryset = Product.objects.all()
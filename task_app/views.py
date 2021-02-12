from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import Category, SubCategory, Product
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework import generics


# Create update delete and read for Category
@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def show_category(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response({'results':serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_category(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'results':serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response("Enter Valid data", status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category ,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'results':serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response("Enter Valid data", status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response("successfully deleted")

# CRUD FOR SUB-CATEGORY

class ListCreateSubCategory(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = (IsAuthenticated,)

class UpdateDestroySubCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = (IsAuthenticated,)

# CRUD FOR PRODUCT
class ListCreateProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

class UpdateDestroyProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

#  list out all the Products and Categories for end-user

def list_product_and_categories(request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    return render(request, 'show_data.html', context)

# show each category product
def show_category_of_product(request, pk):
    # seach product for specific category
    get_category = Category.objects.get(pk=pk)
    get_subcategory = get_category.subcategorys.all()
    product = [p.products.all()  for p in get_subcategory]
    product_dict={}
    for p1 in product:
        for p2 in p1:
            d2={
            'product_name': p2.product_name,
            'product_price': p2.product_price,
            'manufacture_date':p2.manufacture_date,
            }
            product_dict['result']=d2
    return render(request, 'show_product.html', {'product':product_dict})




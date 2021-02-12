
from django.contrib import admin
from django.urls import path
from task_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # category
    path('list-category/', views.show_category, name='list-category'),
    path('create-category/', views.create_category, name='create-category'),
    path('update-category/<int:pk>/', views.update_category , name='update-category'),
    path('delete-category/<int:pk>/', views.delete_category , name='delete-category'),
    # subcategory
    path('list-create-subcategory/', views.ListCreateSubCategory.as_view() , name='list-create-subcategory'),
    path('update-destroy-subcategory/<int:pk>/', views.UpdateDestroySubCategory.as_view() , name='update-destroy-subcategory'),

    # Product
    path('list-create-product/', views.ListCreateProduct.as_view(), name='list-create-product'),
    path('update-destroy-product/<int:pk>/', views.UpdateDestroyProduct.as_view(), name='update-destroy-product'),
    # show category and product
    path('show-category/', views.list_product_and_categories, name='show-category'),
    path('show-category-product/<int:pk>', views.show_category_of_product, name='show-category-product'),
]

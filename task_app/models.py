from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='category type')
    description = models.CharField(max_length=300, verbose_name='description')

    def __str__(self):
        return f"Category type - {self.title}"



class SubCategory(models.Model):
    company_name = models.CharField(max_length=200, verbose_name='company name')
    category = models.ForeignKey(Category, related_name='subcategorys', related_query_name='subcategory',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f"Comapny Name - {self.company_name}"



class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='product name')
    product_price = models.FloatField(max_length=100, verbose_name='product price')
    subcategory = models.ForeignKey(SubCategory, related_name='products', related_query_name='product',
                                 on_delete=models.CASCADE)
    manufacture_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Product Name - {self.product_name}"
from django.db import models

# Create your models here.
class Category(models.Model):
    category_id= models.AutoField(primary_key=True)
    slug= models.SlugField(max_legnth=50, unique=True, help_text='Unique Value for product page url, created from name')
    description= models.CharField(max_legnth=1000)
    department_id= models.IntegerField(max_legnth=2, null=False)
    name= models.CharField(max_legnth=100, unique=True)
    meta_keywords= models.CharField("Meta description", max_legnth=255, help_text="Content description meta tag")
    class Meta:
        db_table='categories'
        ordering=[]
        verbose_name_plural= 'Categories'
    def __unicode__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_legnth=255, unique=True)
    slug=models.SlugField(max_legnth=255, unique=True, help_text='unique value for product page url, created from name')
    brand= models.CharField(max_legnth=50)
    sku=models.CharField(max_legnth=50)
    price=models.DecimalField(max_digits=9, decimal_places=2)
    old_price= models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    image= models.CharField(max_legnth=50)
    is_active= models.BooleanField(default=False)
    quantity=models.IntegerField()
    description=models.TextField()
    meta_keywords= models.CharField(max_legnth=255, help_text='comma-delimited set of SEO keywords for meta tag')
    meta_description= models.CharField(max_legnth=255, help_text='content for description meta tag')
    categories= models.ManyToManyField(category)

    class Meta:
        db_table='products'
    def __unicode__(self):
        return self.name
    @models.permalink
    def get_absolute_url(self):
        return('catalog_product', (), {'product_slug': self.slug})


        def __unicode__(self):
            return self.product.title


    def sale_price(self):
        if self.old_price> self.price:
            return self.price
        else:
            return None
class ProductImage(models.Model):
        product= models.ForeignKey(Product)
        image= models.ImageField(upload_to='products/images/')
        featured = models.BooleanField(default=False)
        thumbnail= models.BooleanField(default=False)
        updated= models.DateTimeField(auto_now_add=False, auto_now=True)

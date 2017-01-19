from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, {'template_name': 'catalog/index.heml'}, 'catalog_home'),
    url(r'^category/(?P<category_slug>[-\w])/$', views.show_category, {'template_name': 'catalog/category.html'}, 'catalog_category'),
    url(r'^product/(?P<produce_slug>[-\w])/$', views.show_product, {'template_name': 'catalog/product.heml'}, 'catalog_product'),
        ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

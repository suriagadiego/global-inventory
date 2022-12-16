from product.api.rest_brand import BrandDetailAPIView
from django.urls import path, include

from . import views
from .api import rest_brand, rest_supplier, rest_warehouse, rest_unit, rest_part_no, rest_job_role, product


urlpatterns = [
    # brands
    path('brand/', rest_brand.brand_list_view,  name='brand_list'),
    path('brand/<int:pk>/', rest_brand.brand_detail_view,  name='brand-detail'),
    path('brand/create/', rest_brand.brand_create_view, name='brand_create'),
    path('brand/update/<int:pk>', rest_brand.brand_update_view, name='brand_update'),
    path('brand/search/', rest_brand.brand_search_view, name='brand_search'),

    #suppliers
    path('supplier/', rest_supplier.supplier_list_view,  name='supplier_list'),
    path('supplier/<int:pk>/', rest_supplier.supplier_detail_view,  name='supplier_detail'),
    path('supplier/create/', rest_supplier.supplier_create_view, name='supplier_create'),
    path('supplier/update/<int:pk>', rest_supplier.supplier_update_view, name='supplier_update'),
    path('supplier/search/', rest_supplier.supplier_search_view, name='supplier_search'),

    #warehouses
    path('warehouse/', rest_warehouse.warehouse_list_view,  name='warehouse_list'),
    path('warehouse/<int:pk>/', rest_warehouse.warehouse_detail_view,  name='warehouse_detail'),
    path('warehouse/create/', rest_warehouse.warehouse_create_view, name='warehouse_create'),
    path('warehouse/update/<int:pk>', rest_warehouse.warehouse_update_view, name='warehouse_update'),
    path('warehouse/search/', rest_warehouse.warehouse_search_view, name='warehouse_search'),

    #units
    path('unit/', rest_unit.unit_list_view,  name='unit_list'),
    path('unit/<int:pk>/', rest_unit.unit_detail_view,  name='unit-detail'),
    path('unit/create/', rest_unit.unit_create_view, name='unit_create'),
    path('unit/update/<int:pk>', rest_unit.unit_update_view, name='unit_update'),
    path('unit/search/', rest_unit.unit_search_view, name='unit_search'),

    #job role
    path('job_role/', rest_job_role.job_role_list_view,  name='job_role_list'),
    path('job_role/<int:pk>/', rest_job_role.job_role_detail_view,  name='job_role-detail'),
    path('job_role/create/', rest_job_role.job_role_create_view, name='job_role_create'),
    path('job_role/update/<int:pk>', rest_job_role.job_role_update_view, name='job_role_update'),
    path('job_role/search/', rest_job_role.job_role_search_view, name='job_role_search'),

    #part number
    path('part/', rest_part_no.part_no_list_view,  name='part_no_list'),
    path('part/<int:pk>/', rest_part_no.part_no_detail_view,  name='part_no-detail'),
    path('part/create/', rest_part_no.part_no_create_view, name='part_no_create'),
    path('part/update/<int:pk>', rest_part_no.part_no_update_view, name='part_no_update'),
    path('part/search/', rest_part_no.part_no_search_view, name='part_no_search'),

    # # user
    # path('user/', rest_user.user_list_view,  name='user_list'),
    # path('user/<int:pk>/', rest_user.user_detail_view,  name='user-detail'),
    # path('user/create/', rest_user.user_create_view, name='user_create'),
    # path('user/update/<int:pk>', rest_user.user_update_view, name='user_update'),
    # path('user/search/', rest_user.user_search_view, name='user_search'),

    #product
    path('product/', product.product_list_view,  name='product_list'),
    # path('product/<str:part>/', product.product_detail_view,  name='product_detail'),
    path('product/update_stock1/', product.update_product_stock,  name='product_stock_update'),
]

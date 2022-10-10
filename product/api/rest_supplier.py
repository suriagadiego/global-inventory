from rest_framework import generics
from rest_framework.decorators import api_view
from ..models import Supplier
from ..serializers import SupplierSerializer
from django.core.paginator import Paginator
import json
from rest_framework.response import Response

# class SupplierView(mixins.ListModelMixin, generics.API):
class SupplierDetailAPIView(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = 'pk'

supplier_detail_view = SupplierDetailAPIView.as_view()

class SupplierListAPIView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

supplier_list_view = SupplierListAPIView.as_view()

class SupplierCreateAPIView(generics.CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

supplier_create_view = SupplierCreateAPIView.as_view()

class SupplierUpdateAPIView(generics.UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = 'pk'

supplier_update_view = SupplierUpdateAPIView.as_view()


@api_view(['POST'])
def supplier_search_view(request, pk=None, *args, **kwargs):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    current_page = body.get('currentPage') 
    page_size = body.get('pageSize') 
    sort_by = body.get('sortBy') or '-updated_at'
    filter_by = body.get('filterBy')
    filter_id = body.get('filterById')
    filter_dict = None

    if filter_by and filter_id: filter_dict = {filter_by: filter_id}

    if filter_dict:
        queryset = Supplier.objects.filter(filter_dict).all().order_by(sort_by).values()

    else:
        queryset = Supplier.objects.filter().all().order_by(sort_by).values()

    data = SupplierSerializer(queryset, many=True).data
    p = Paginator(data, page_size)

    result = {}
    result['total'] = p.count
    result['numPages'] = p.num_pages
    result['metadata'] = p.page(current_page).object_list

    return Response(result)

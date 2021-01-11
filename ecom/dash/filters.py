import django_filters
from django_filters import DateFilter
from .models import Order

class OrderFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name='ordered_date',lookup_expr='gte')
    end_date=DateFilter(field_name='ordered_date', lookup_expr='lte')
    class Meta:
        model=Order
        fields='__all__'
        exclude=['customer','category','ordered_date']
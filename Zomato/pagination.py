from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class ProductPagination(PageNumberPagination):
    page_size=2
    page_query_param='Record'
    max_page_size=10
    page_size_query_param='size'
    last_page_string=['end']

class CustomerLimitOffsetPagination(LimitOffsetPagination):
    default_limit=3
    limit_query_param='Limit'
    offset_query_param='Record'

class OrderItemCursorPagination(CursorPagination):
    page_size=2
    cursor_query_param='Record'
    ordering='unit_price'

class OrderCursorPagination(CursorPagination):
    page_size=2
    cursor_query_param='Record'
    ordering='order_date'
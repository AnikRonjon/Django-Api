from rest_framework.pagination import LimitOffsetPagination


class MyPagination(LimitOffsetPagination):
    default_limit = 1
    limit_query_param = 'l'
    offset_query_param = 'o'

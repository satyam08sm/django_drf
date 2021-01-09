from rest_framework import pagination


class CustomPaginator(pagination.PageNumberPagination):
    page_size = 3

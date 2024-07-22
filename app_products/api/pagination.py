from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 20
    # last_page_strings = 'end' # by default is last
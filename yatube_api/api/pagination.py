from rest_framework.pagination import LimitOffsetPagination


class OptionalLimitOffsetPagination(LimitOffsetPagination):
    default_limit = None

    def paginate_queryset(self, queryset, request, view=None):
        limit = request.query_params.get(self.limit_query_param)
        offset = request.query_params.get(self.offset_query_param)

        if limit is None and offset is None:
            return None

        return super().paginate_queryset(queryset, request, view)

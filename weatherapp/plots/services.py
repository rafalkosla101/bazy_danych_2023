
def get_min_max_values(queryset, row_name):
    ordered_queryset = queryset.order_by(row_name)
    return getattr(ordered_queryset[0], row_name), getattr(ordered_queryset[len(ordered_queryset) - 1], row_name)

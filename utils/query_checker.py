from django.http import QueryDict

ALLOWED_QUERIES = ['q', 'page', 'order_by', 'type', 'status', 'rated', 'genre', 'genre_exclude', 'score', 'sort']


def get_allowed_queries(queries: QueryDict):
    new_queries = {}
    for key, value in queries.items():
        if key in ALLOWED_QUERIES:
            new_queries[key] = value

    return new_queries

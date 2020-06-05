#CELERY_ROUTES = {
#    'calculate_recommendations_task': {
#        'exchange': 'recommendation_worker',
#        'exchange_type': 'direct',
#        'routing_key': 'recommendation_worker'
#    }
#}
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
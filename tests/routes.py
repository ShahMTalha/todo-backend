base_url = "http://0.0.0.0:3000/"  # os.environ.get('BASE_URL')

routing_mapper = {
    'todo/listing': {
        'route': 'todo/listing',
        'method': 'get',
        'payload': ''
    },
    'todo/add': {
        'route': 'todo/add',
        'method': 'post',
        'payload': {'content': 'Testing content..'}
    }
}

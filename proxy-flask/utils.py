class UrlHandling:
    def __init__(self):
        pass

    @classmethod
    def parse_url(klass, url, server_route):
        print('1', url)
        if url[-1] == '/':
            url = url[:-1]

        print('2', url)
        return '{}{}/'.format(server_route, url)

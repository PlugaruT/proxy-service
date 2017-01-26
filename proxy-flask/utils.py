class UrlHandling:
    def __init__(self):
        pass

    @classmethod
    def parse_url(klass, url, request, server_route):
        args = ''
        for arg, value in request.args.items():
            args += '?{}={}'.format(arg, value)
        return '{}{}{}'.format(server_route, url, args)

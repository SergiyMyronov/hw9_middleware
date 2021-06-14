from datetime import datetime

from .models import Log


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        timestamp = str(datetime.now())

        response = self.get_response(request)
        if not request.path.lower().startswith('/admin/'):
            log = Log(path=request.path, method=request.method, timestamp=timestamp)
            log.save()

        return response

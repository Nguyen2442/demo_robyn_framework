from app import app

class CustomMiddleware:
    def __init__(self, app):
        self.app = app

    async def process_request(self, request):
        request.headers['before'] = 'before_request'
        print(100*"Middleware ")
        return await self.app(request)
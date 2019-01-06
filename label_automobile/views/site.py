from pyramid.view import view_defaults, view_config
from pyramid.response import Response

class PartView:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def list(self):
        return Response("Homepage<br><a href='user'>Users</a><br><a href='part'>Part</a>")

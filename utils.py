from auth import APIAuth

class ParseRequest:

    def parse(request, session):
        authorized_request = APIAuth.authorize(request, session)
        return authorized_request + ' + B'
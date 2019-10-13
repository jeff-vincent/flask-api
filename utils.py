from auth import APIAuth

class ParseRequest:

    def parse(request, session):
        request = APIAuth.authorize(request, session)

        if request == 'Not logged in':
            return 'Not logged in'

        return request + ' + B'
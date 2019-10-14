from auth import APIAuth

class ParseRequest:

    def parse(request, session):
        authorized_user = APIAuth.authorize(request, session)

        if authorized_user == None:
            return 'Not logged in'

        return authorized_user + ' + B'
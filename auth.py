class APIAuth:

    def authorize(request, session):
        
        try:
            if session['logged_in']:
                return 'A'
        except:
            return 'Not logged in'
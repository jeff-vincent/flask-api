from flask import session
from auth import APIAuth


class DoTask:

    def do_task(request):

        try:
            if session['logged_in']:
                return 'Task Executed'
            else: 
                return 'Please login'
                
        except Exception as e:
            return 'Task failed. Error Code: {}'.format(str(e))
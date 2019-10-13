import csv
from utils import ParseRequest


class ParseCSV:

    def parse(request, session):
        parsed_request = ParseRequest.parse(request, session)

        if parsed_request == 'Not logged in':
            return 'Not logged in'

        return parsed_request + ' + C'



import csv
from utils import ParseRequest


class ParseCSV:

    def parse(request, session):

        parsed_request = ParseRequest.parse(request, session)

        return parsed_request + ' + C'


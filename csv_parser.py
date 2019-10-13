import csv
from utils import ParseRequest


class ParseCSV:

    def parse(request):

        parsed_request = ParseRequest.parse(request)

        return parsed_request + ' + B'


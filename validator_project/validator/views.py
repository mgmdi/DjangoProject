from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from validator.forms import ValidatorForm

class IPNValidator(APIView):
    """
    View validate IPN.
    """

    def post(self, request, format=None):
        """
        Returns if IPN is valid.
        """
        comment = ValidatorForm(request.data or None)
        print(comment)
        res = 'res'
        return Response(res)
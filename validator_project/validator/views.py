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
        reqForm = ValidatorForm(request.data or None)
        print(reqForm)
        if reqForm.is_valid():
            # Si es valido hago get del usuario, hago las verificaciones y con eso hago update
            print('FORM IS VALID')

        return Response('OK')
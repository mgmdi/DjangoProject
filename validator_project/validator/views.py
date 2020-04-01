from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from validator.forms import ValidatorForm
from validator.services import get_user, update_user
from validator import validators
import datetime

class IPNValidator(APIView):
    """
    View validate IPN.
    """

    def post(self, request, format=None):
        """
        Returns if IPN is valid.
        """
        # Validates existance and format of request fields
        req_form = ValidatorForm(request.data or None)

        if req_form.is_valid():
            # User_data is a dictionary
            user_data = get_user(req_form.data['payer_id'])

            if(user_data):
                print(user_data)
                user_data = validators.validate_payment_status(req_form.data['payment_status'], user_data)
                user_data = validators.validate_plan_dates(req_form.data['item_name'], user_data)
                user_data['LAST_PAYMENT_DATE'] = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
                response = update_user(user_data)
                if(response):
                    return Response(
                        {
                        'message': 'User updated', 
                        },
                        status=status.HTTP_200_OK)
                else: 
                    return Response(
                        {
                        'message': 'Something wrong happened. Could not update user', 
                        })
            else:
                return Response(
                    {
                    'message': 'User not found', 
                    },
                    status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(
                    {
                    'message': 'Invalid form', 
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                    )

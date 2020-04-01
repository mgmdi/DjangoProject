# DjangoProject

## VALIDATIONS:

1. To the form: 
    1. It is validated that id fields have only letters, numbers and \-
    2. It is validated that charfields fields have only letters
    3. It is validated that float/integer fields are valid
    4. It is validated that currency only has 3 chars
    5. It is validated that dates have the following format H:M:S b d, Y
    6. It is validated the existence of all fields

2. To the User data:
    1. As it was indicated on the challenge, if the user downgraded/upgraded his plan then the current date is added/updated in the user object 
    2. If the payment status is different than completed, then the user subscription is set to free and the ENABLED_FEATURES to True
    3. Also, the last payment date is added to the object

## Run project:

### 1. pip install -r requirements.txt
### 2. python manage.py runserver 
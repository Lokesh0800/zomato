from django.contrib.auth import get_user_model
User = get_user_model()

def authenticate(phone,password):
    try:
        user = User.objects.get(phone_number=phone)
        success = user.check_password(password)
        if success:
            return user
    except User.DoesNotExist:
        pass
    return None
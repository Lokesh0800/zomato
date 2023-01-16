from django.contrib.auth.base_user import BaseUserManager

class mymanager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, phone_number,password,**fields):
        if not phone_number:
            raise ValueError('Phone number is required')
        user = self.model(phone_number=phone_number,**fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_number,password,**fields):
        fields.setdefault('is_staff',True)
        fields.setdefault('is_superuser',True)
        fields.setdefault('is_active',True)
    
        return self.create_user(phone_number,password,**fields)
        
    
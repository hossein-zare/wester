from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password, email, name=None, mobile_number=None, email_verified=False, is_staff=False, is_superuser=False, is_verified=False):
        """
        Create a user.
        """
        
        if not username:
            raise ValueError('Username is required')
        if not password:
            raise ValueError('Password is required')
        if not email:
            raise ValueError('Email is required')

        user = self.model(
            name = name if len(name) > 0 else None,
            username = username.lower(),
            email = self.normalize_email(email),
            email_verified = email_verified,
            mobile_number = mobile_number,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_verified = is_verified,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_staffuser(self, username, password, email):
        """
        Create a staff user.
        """

        return self.create_user(username, password, email, is_staff=True)

    def create_superuser(self, username, password, email):
        """
        Create a super user.
        """

        return self.create_user(username, password, email, is_staff=True, is_superuser=True)
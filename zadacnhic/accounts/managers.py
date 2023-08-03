from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Manager for custom `User` model."""

    use_in_migrations = True

    def create_user(self, email: str, password: str, first_name: str, last_name: str):
        if not email:
            return ValueError('Users must have an email address.')
        if not first_name:
            return ValueError('Users must have a first name.')
        if not last_name:
            return ValueError('Users must have a last name.')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email: str, password: str, first_name: str, last_name: str):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, first_name: str, last_name: str):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

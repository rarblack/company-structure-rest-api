# djangofrom django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _
# # from django.core.exceptions import ValidationError
#
#
# class CustomUserManager(BaseUserManager):
#     """
#     Custom user models manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#
#     # @classmethod
#     # def normalize_email(cls, email):
#     #     """
#     #     Normalize the email address by lowercasing the domain part of it.
#     #     """
#     #     email = email or ''
#     #     try:
#     #         email_name, domain_part = email.strip().rsplit('@', 1)
#     #     except ValueError:
#     #         pass
#     #     else:
#     #         if domain_part.lower() != 'socar-aqs.com':
#     #             raise ValidationError(
#     #                 message="'Enter a valid email. This value must end with socar-aqs.com ending'"
#     #             )
#     #         email = email_name + '@' + domain_part.lower()
#     #     return email
#
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError(_('The Email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         return self._create_user(email, password, **extra_fields)


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


# from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    """
    Custom user models manager where personal_number is the unique identifiers
    for authentication instead of usernames.
    """

    def _create_user(self, personal_number, password, **extra_fields):
        """
        Create and save a User with the given personal_number and password.
        """
        if not personal_number:
            raise ValueError(_('The personal number must be set'))
        user = self.model(personal_number=personal_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, personal_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(personal_number, password, **extra_fields)

    def create_superuser(self, personal_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(personal_number, password, **extra_fields)


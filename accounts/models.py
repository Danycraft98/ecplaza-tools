from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    """
    A class used to represent a UserManager object
    """

    def create_user(self, username, password, email=None):
        """
        Creates and saves a User with the given email and password.

        Args:
            username (str): User's username
            email (str): User's email
            password (str): User's password
        
        Returns: User

        >>> userManager = UserManager()
        >>> userManager.create_user('username', 'password', 'email@email.com')

        """
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password):
        """
        Creates and saves a staff user with the given email and password.

        Args:
            username (str): User's username
            email (str): User's email
            password (str): User's password
        
        Returns: User

        >>> userManager = UserManager()
        >>> userManager.create_staffuser('username', 'password', 'email@email.com')

        """
        user = self.create_user(
            username,
            password,
            email=email,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email and password.

        Args:
            username (str): User's username
            email (str): User's email
            password (str): User's password
        
        Returns: User

        >>> userManager = UserManager()
        >>> userManager.create_superuser('username', 'password', 'email@email.com')

        """
        user = self.create_user(
            username,
            password,
            email=email
        )
        user.staff = True
        user.admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    A class used to represent a User object
    """

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, null=True)
    active = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        """
        The user is identified by their email address

        Returns: str
        """
        return self.email

    def get_short_name(self):
        """
        The user is identified by their email address

        Returns: str
        """
        return self.email

    def __str__(self):
        """
        The string return method

        Returns: str
        """
        return self.get_full_name()

    def title(self):
        """
        The user title is returned

        Returns: str
        """
        if self.is_admin:
            return 'Admin'
        elif self.is_staff:
            return 'Staff'
        return 'User'

    @property
    def is_staff(self):
        """
        The user staff status is returned

        Returns: bool
        """
        return self.staff

    @property
    def is_admin(self):
        """
        The user admin status is returned

        Returns: bool
        """
        return self.admin


if __name__ == '__main__':
    import doctest

    doctest.testmod()

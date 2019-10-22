import hashlib
import logging
import os

CURRENT_FILE_PATH = os.path.dirname(__file__)
LOG_FILE_PATH = os.path.join(CURRENT_FILE_PATH, 'error.log')

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='w',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s')


class User:
    def __init__(self, username, password):
        """Create a new user object.

        The user password will be authenticated before storing.

        :param username: user name
        :type username: str
        :param password: users password
        :type password: str
        """

        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """Encrypt the password

        Encrypt password with the username and return the sha digest

        :param password: users password
        :type password: str
        :return: encrypted password
        :rtype: str
        """

        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Check user password

        Return true if the password is valid for this user.

        :param password: typed password
        :type password: str
        :return: if password is valid for user
        :rtype: bool
        """

        return password == self.password


class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UserNameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class Authenticator:
    def __init__(self):
        """Construct and authenticator to manage users logging in and out.
        """

        self.users = {}

    def add_user(self, username, password):
        """Add a user

        Add user if password is valid

        :param username: users name
        :type username: str
        :param password: users password
        :type password: str
        """

        if username in self.users:
            raise UserNameAlreadyExists(username)

        if len(password) < 7:
            raise PasswordTooShort(username)

        self.users[username] = User(username, password)

    def login(self, username, password):
        """ Login function

        Determine if user is logged in

        :param username: users name
        :type username: str
        :param password: users password
        :type password: str
        :return: log in status
        :rtype: bool
        """

        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass


class Authorizer:
    def __init__(self, authenticator):
        """Map permissions to users

        Should not allow a user to access to a permission if they
        are not logged in.

        :param authenticator: user log in manager
        :type authenticator: Authenticator
        """

        self.authenticator = authenticator
        self.permissions = {}

    def add_permissions(self, perm_name):
        """Adding permissions

        Create a new permission that users can be added to.

        :param perm_name: permission name
        :type perm_name: str
        """

        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            logging.ERROR("You cannot create a new permission when one exists already")
            raise PermissionError("Permission exists")

    def permit_user(self, perm_name, username):
        """Permit user

        Add user name to a permission unless the username doesn't exist
        or the permission doesn't exist.

        :param perm_name: permission name
        :type perm_name: str
        :param username: users name
        :type username: str
        """

        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        """Check user permission

        Check whether a user has a specific permission or not.

        :param perm_name: name of permission
        :type perm_name: str
        :param username: users name
        :type username: str
        :return: bool
        """

        if not self.authenticator.users[username].is_logged_in:
            logging.error("You aren't logged in!")
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError as e:
            logging.error("The permission {} really does not exist".format(e.args[0]))
            raise PermissionError("Permission doesnt exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


if __name__ == "__main__":
    print(LOG_FILE_PATH)

    authenticator = Authenticator()
    authorizer = Authorizer(authenticator)

    authenticator.add_user("yung feezy", "real deal")
    password = authenticator.users["yung feezy"].password
    authenticator.login("yung feezy", password)
    print(authenticator.users["yung feezy"].is_logged_in)
    authorizer.add_permissions("king of the forest that's why")
    authorizer.permit_user("king of the forest that's why", "yung feezy")
    authorizer.check_permission("king of the forest", "yung feezy")



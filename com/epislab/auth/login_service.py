
from com.epislab.auth.login_model import LoginModel


class LoginService:

    def __init__(self):
        pass


    def execute(self, login: LoginModel) -> LoginModel:
        username = login.username
        password = login.password
        if username == "hong" and password == "1234":
            result = "home"
        else:
            result = "intro"
        login.result = result
        return login
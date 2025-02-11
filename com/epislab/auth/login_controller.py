
from com.epislab.auth.login_model import LoginModel
from com.epislab.auth.login_service import LoginService


class LoginController:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        print("🔑username:", username)
        print("🍳password:", password)


    def getResult(self) -> LoginModel:
        service = LoginService()
        login = LoginModel()
        login.username = self.username
        login.password = self.password
        return service.execute(login)
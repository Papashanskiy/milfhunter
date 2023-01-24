
class Controller:

    def __init__(self, driver):
        self.driver = driver


class LoginController(Controller):

    def login(self, login, password):
        raise NotImplementedError


class ChatsController(Controller):

    def get_chats(self):
        raise NotImplementedError


class FilterController(Controller):

    def set(self, *args, **kwargs):
        raise NotImplementedError


class MeetController(Controller):

    def matching(self, *args, **kwargs):
        raise NotImplementedError


class MessagesController(Controller):

    def chatting(self, *args, **kwargs):
        raise NotImplementedError

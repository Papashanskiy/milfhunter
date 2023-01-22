from controllers.love_planet.login import MambaLogin
from controllers.love_planet.filter import MambaFilter
from controllers.love_planet.meet import MambaMeet
from controllers.love_planet.chats import MambaChats
from controllers.love_planet.messages import MambaMessages


class Mamba:
    login = MambaLogin
    filter = MambaFilter
    meet = MambaMeet
    chats = MambaChats
    messages = MambaMessages

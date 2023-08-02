from dataclasses import dataclass


@dataclass
class SignUp:
    serv: dict = None


@dataclass
class FeedBack:
    temp: dict = None


data_sign_up = SignUp()
data_feedback = FeedBack()

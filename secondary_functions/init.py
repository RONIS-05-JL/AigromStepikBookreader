from dataclasses import dataclass
import os
import games



@dataclass
class UserInfo:
    id: int
    name: str
    game:   dict
    message: list[str]
    administration: bool

print(os.listdir(r'U:\Repo and projects\AigromStepik\games'))



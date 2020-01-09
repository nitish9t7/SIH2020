from src.common.database import Database
from bson.binary import Binary


class User(object):
    def __init__(self,
                 username,
                 password,
                 image):
        self.username = username
        self.password = password
        self.image    = image

    # def json(self):
    #     return {
    #         "username": self.username,
    #         "password": self.password
    #     }

    def save(self):
        # print("insert")
        # avat_ctype = self.image
        # fs = GridFS(db)
        # avatar_id = fs.put(avat, content_type=avat_ctype, filename=nomfich)
        binary_image = Binary(self.image)
        Database.insert("users", {
            "username" : self.username,
            "password" : self.password,
            "image"    : binary_image
        })

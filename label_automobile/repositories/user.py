from label_automobile.models.user import User


class UserRepository:
    def __init__(self, session):
        self.session = session
        self.model = User

    def find_by_email(self, email):
        return self.session.query(User).filter(
            User.email == email).one()

    def get_all(self):
        return self.session.query(User).all()
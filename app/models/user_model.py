class User:

    def __init__(
        self,
        id,
        full_name,
        email,
        created_at
    ):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "created_at": str(self.created_at)
        }
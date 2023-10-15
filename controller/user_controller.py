from services.user_services import UserService

class UserController:
    def __init__(self):
        self.db_service = UserService()

    def get_users(self):
        users = self.db_service.find({})
        return str([user for user in users])
    
    def get_user(self, user_id):
        user = self.db_service.find_one({'_id': user_id})
        return str(user)
    
    def create_user(self, user):
        self.db_service.insert_one(user)
        return 'User created successfully'

    def update_user(self, user_id, user):
        self.db_service.update_one({'_id': user_id}, user)
        return 'User updated successfully'

    def delete_user(self, user_id):
        self.db_service.delete_one({'_id': user_id})
        return 'User deleted successfully'


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def is_user_in_group(self, user, group):
        if user is None:
            return False
        if user in group.users:
            return True
        else:
            for obj in group.groups:
                if self.is_user_in_group(user, obj):
                    return True
        return False

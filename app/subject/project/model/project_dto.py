

class ProjectDTO():
    
    def __init__(self, name, description, active, state, group_id, number_of_students) -> None:
        self.name = name
        self.description = description
        self.active = active
        self.state = state
        self.group_id = group_id
        self.number_of_students = number_of_students
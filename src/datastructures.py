
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
                "id": self._generateId(),
                "first_name": "Nicolas",
                "last_name": last_name,
                "age": 24,
                "lucky_numbers": [18,1,4]
            },
            {
                "id": self._generateId(),
                "first_name": "Katherine",
                "last_name": last_name,
                "age": 26,
                "lucky_numbers": [21,1,2]
            },
            {
                "id": self._generateId(),
                "first_name": "Jose",
                "last_name": last_name,
                "age": 3,
                "lucky_numbers": [13,11,4]
            }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return self._members
        

    def delete_member(self, id):
        for member in self._members:
            if(member["id"]==id):
                self._members.remove("id")
                return "Removido"
        return "No se encontro el miembro con el id: " + id + " por tanto, no se pudo eliminar"

    def get_member(self, id):
        for member in self._members:
            if(member["id"]==id):
                return member
        return "No se encontro el miembro con el id: " + id
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

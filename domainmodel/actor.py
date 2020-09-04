
class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleague: List[Actor] = list()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self) -> str:
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self,other) -> bool:
        if not isinstance(other, Actor):
            return False
        return other.__actor_full_name == self.__actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__colleague

class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        actor1.add_actor_colleague("Bob")
        assert ["Bob"]
        actor1.check_if_this_actor_worked_with("Bob")
        assert True
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(42)
        assert actor3.actor_full_name is None

# IAdoptable interface/abstract class
class IAdoptable(ABC):
    @abstractmethod
    def adopt(self):
        pass

# AdoptionEvent class
class AdoptionEvent:
    def __init__(self):
        self.participants = []

    def host_event(self):
        print("Adoption event hosted!")

    def register_participant(self, participant):
        self.participants.append(participant)

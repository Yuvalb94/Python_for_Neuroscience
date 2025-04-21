# Create a 'Person' class to manage the entirety of my lab's data. This class will be the base for the 'Researcher' and 'Participant' classes.
# The shared attributes are: 'first_name', 'last_name'. 'id_number', 'sex', amd 'date_of_birth'.
# Researchers also have 'title' and 'position' attributes.
# Participants also have 'weight' and 'do,inant_hand' attributes.
# Both classes need a 'get_full_name()' method to return the full name, but the Researcher class should include the title as a prefix if it is specified.
# The Participant class should also have a 'read_text()' method that reads a file that is expected to be found under /data/<id_number>.txt and returns its content.

from pathlib import Path
class Person:
    """
    Base class for ...
    """
    def __init__(self, first_name: str = 'John', last_name: str = 'Doe', id_number: int = 123456789, sex: str = 'U', date_of_birth: str = '01/01/2001'):
        """
        

        """
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.sex = sex
        self.date_of_birth = date_of_birth

    def get_full_name(self):
        """
        
        
        """
        return f"Full name: {self.first_name} {self.last_name}"


class Researcher(Person):
    """
    _summary_

    Args:
        Person (_type_): _description_
    """
    def __init__(self, first_name = 'John', last_name = 'Doe', id_number = 123456789, sex = 'U', date_of_birth = '01/01/2001', title: str = 'Mr.', position: str = 'Assistant to the regional manager'):
        super().__init__(first_name, last_name, id_number, sex, date_of_birth)
        self.title = title
        self.position = position

    def get_full_name(self):
        return f"Full name: {self.title} {self.first_name} {self.last_name}"
    

class Participant(Person):
    """
    _summary_

    Args:
        Person (_type_): _description_
    """
    def __init__(self, first_name = 'John', last_name = 'Doe', id_number = 123456789, sex = 'U', date_of_birth = '01/01/2001', weight: float = 70.0, dominant_hand: str = 'R'):
        super().__init__(first_name, last_name, id_number, sex, date_of_birth)
        self.weight = weight
        self.dominant_hand = dominant_hand
    
    def read_text(self):
        """
        Reads a text file from the data directory and returns its content.
        """
        file_path = Path(f"data/{self.id_number}.txt")
        if file_path.exists():
            with open(file_path, 'r') as file:
                return file.read()
        else:
            return f"File {file_path} does not exist."
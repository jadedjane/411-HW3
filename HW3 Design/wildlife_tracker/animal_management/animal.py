from typing import Any, Optional

class Animal:
    
    def __init__(self, animal_id: int, species: str, age: Optional[int] = None, health_status: Optional[str] = None, current_location: Optional[str] = None):
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.health_status = health_status
        self.current_location = current_location
    

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass
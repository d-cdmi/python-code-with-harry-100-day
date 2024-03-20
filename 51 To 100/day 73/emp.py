from typing import Any


class Employee:
    def __init__(self,name) -> None:
        self.name = name
        
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i
    def __str__(self) -> str:
        return f'The Employee name is {self.name} as str'
    
    def __repr__(self) -> str:
        return f'The Employee name is {self.name} as repr'
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("hey i am aboy ")
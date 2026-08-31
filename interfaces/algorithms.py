from abc import ABC, abstractmethod

class Encrypting(ABC):
    """
    Interface for krypteringsalgoritmer
    """
    @abstractmethod
    def encrypt(self, text: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, text: str) -> str:
        pass
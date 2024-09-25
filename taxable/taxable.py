from abc import ABC, abstractmethod


# abstract class


class Taxable(ABC):
    # static attribute
    __vat_pct = 14
    @staticmethod
    def get_vat_pct():
        return Taxable.__vat_pct

    @abstractmethod
    def get_tax(self, amount):
        pass

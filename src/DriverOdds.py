
from lib2to3.pgen2 import driver
from msilib.schema import ODBCDataSource


class DriverOdds:
    def __init__(self,driver,odd,id_aposta) -> None:
        self.driver = driver
        self.odd = odd
        self.id_aposta = id_aposta
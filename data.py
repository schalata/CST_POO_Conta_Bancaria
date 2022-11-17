from datetime import datetime, timedelta, timezone


class Data:

    def __init__(self):
        self.__diferenca = timedelta(hours=-3)
        self.__fuso_horario = timezone(self.__diferenca)
        self._data_atual = datetime.now().astimezone(self.__fuso_horario)

    @property
    def dia(self):
        return self._data_atual.day

    @property
    def mes(self):
        return self._data_atual.month

    @property
    def ano(self):
        return self._data_atual.year

    @property
    def hora(self):
        return self._data_atual.hour

    @property
    def minuto(self):
        return self._data_atual.minute

    def data(self):
        data = f'{self._data_atual.day}/{self._data_atual.month}/{self._data_atual.year}-/' \
               f'{self._data_atual.hour}:{self._data_atual.minute}'
        return data

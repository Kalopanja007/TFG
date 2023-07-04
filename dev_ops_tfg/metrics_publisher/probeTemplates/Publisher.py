from abc import ABC, abstractmethod
from influxdb import InfluxDBClient


class Publisher(ABC):
    pass

    def __init__(self):
        pass
    
    @abstractmethod
    def publish(self, data) -> None:
        pass




class InfluxDB(Publisher):
    pass
    PORT = 8086

    def __init__(self, db_name=None, host=None, port=PORT):

        self.db_name = db_name
        self.host    = host
        self.port    = port

        self.client = InfluxDBClient(host=self.host, port=self.port, database=self.db_name)


    def publish(self, data: list[dict[str, str | int]]) -> None:
        self.client.write_points(points=data, time_precision='ms')
        self.client.close()

    def query(self, data: str):
        lista = list(self.client.query(data).get_points())
        # To flush data
        self.client.close()
        return lista

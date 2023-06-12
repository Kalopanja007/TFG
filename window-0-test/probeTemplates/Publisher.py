from abc import ABC, abstractmethod


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
        pass
        from influxdb import InfluxDBClient

        self.db_name = db_name
        self.host    = host
        self.port    = port

        self.client = InfluxDBClient(host=self.host, port=self.port, database=self.db_name)


    def publish(self, data: list[dict[str, str | int]]) -> None:
        pass
        
        self.client.write_points(points=data)


from transport.client import Client
from transport.vehicle import Vehicle

def main():
    truck = Vehicle(capacity=10)
    client1 = Client("Иван", 3.5)
    client2 = Client("Мария", 5.0, is_vip=True)

    truck.load_cargo(client1)
    truck.load_cargo(client2)

    print(truck)

if __name__ == "__main__":
    main()

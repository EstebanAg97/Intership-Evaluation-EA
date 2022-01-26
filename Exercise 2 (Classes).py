class Client:
  def __init__(client, id, name, address1, address2, town, county, postCode, region, countryId):
    client.id = id
    client.name = name
    client.address1 = address1
    client.address2 = address2
    client.town = town
    client.county = county
    client.postCode = postCode
    client.region = region
    client.countryId = countryId

  def myfunc(client):
    print("This Client address is: " + client.address1)

class Stock:
  def __init__(car, stockId, make, model, colorId, vehicleType, mileage, purchaseDate):
    car.stockId = stockId
    car.make = make
    car.model = model
    car.colorId = colorId
    car.vehicleType = vehicleType
    car.mileage = mileage
    car.purchaseDate = purchaseDate

  def getCarInfo(car):
    print("Car Model: " + car.model + ", Car Brand:" +car.make)

class Transport:
    def __init__(transportation, name, id, location, age, model, colorId, registrationDate):
        transportation.name = name
        transportation.id = id
        transportation.location = location
        transportation.age = age
        transportation.model = model
        transportation.colorId = colorId
        transportation.registrationDate = registrationDate

    def getTransportInfo(transport):
        print("This kind of transportation is called "+ transport.name + ", is Located in "+transport.location+ ","+str(transport.age)+" years old")


car1 = Stock(1, "Rolls Royce", "Camargue", 1, "Saloon", 52500, "1/1/2012")
car1.getCarInfo()

c1 = Client(1,"Aldo Motors", "4, Scale Street", "", "Uttoxeter", "Staffs", "ST17 99RZ", "East Midlands", 1)
c1.myfunc()

t1 = Transport("Train", 4, "Texas", 14, "Railroad", 2, "1/1/2008")
t1.getTransportInfo()
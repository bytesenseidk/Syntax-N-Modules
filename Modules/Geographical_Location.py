import geocoder
import reverse_geocoder as rg


def location():
    latitude, longitude = [*geocoder.ip("me").latlng]
    city = city = rg.search((latitude, longitude), verbose=False)
    return city[0]["name"]


if __name__ == "__main__":
    print("Your current location: " + location())


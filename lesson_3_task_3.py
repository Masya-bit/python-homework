from address import Address
from mailing import Mailing

from_address = Address(
    index="101000",
    city="Москва",
    street="Тверская",
    house="15",
    apartment="45"
)

to_address = Address(
    index="190000",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="28",
    apartment="12"
)

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350.50,
    track="TRACK123456789"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
from models.item import Item
from models.brand import Brand

import repositories.item_repository as item_repo
import repositories.brand_repository as brand_repo

item_repo.delete_all()
brand_repo.delete_all()

brand1 = Brand("Fender", True)
brand_repo.save(brand1)
brand2 = Brand("Gibson", True)
brand_repo.save(brand2)


item_1 = Item("Stratocaster", brand1, "classic vibe", 2, 500, 700)
item_repo.save(item_1)

item_2 = Item("Telecaster", brand1, "with humbucker in bridge", 3, 500, 700)
item_repo.save(item_2)

item_3 = Item("Les Paul", brand2, "Pelham blue", 3, 700, 1000)
item_repo.save(item_3)
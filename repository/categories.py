from repository.category_logic import (
    Sulfuras,
    ConjuredItem,
    NormalItem,
    AgedBrie,
    Backstage,
)

categories = {
    "Sulfuras": lambda x, y, z: Sulfuras(x, y, z),
    "Conjured": lambda x, y, z: ConjuredItem(x, y, z),
    "Normal": lambda x, y, z: NormalItem(x, y, z),
    "Aged Brie": lambda x, y, z: AgedBrie(x, y, z),
    "Backstage": lambda x, y, z: Backstage(x, y, z),
}
